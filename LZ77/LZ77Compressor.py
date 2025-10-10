from Tag import Tag

def rabinKarp(text, pattern):
    n = len(text)
    m = len(pattern)

    if n == 0 or m > n:
        return -1

    base = 26
    power = [1] * m
    for i in range(1, m):
        power[i] = power[i - 1] * base

    t = 0
    for i in range(n - 1, n - m - 1, -1):
        t += ord(text[i]) * power[i - n + m]

    p = 0
    for i in range(m - 1, -1, -1):
        p += ord(pattern[i]) * power[i]

    s, e = n - 1, n - m
    while e >= 0:
        if p == t:
            match = True
            for j, k in zip(range(s, s - m, -1), range(m - 1, -1, -1)):
                if text[j] != pattern[k]:
                    match = False
                    break
            if match:
                return e

        if e > 0:
            t -= ord(text[s]) * power[m - 1]
            t *= base
            t += ord(text[e - 1])

        s -= 1
        e -= 1

    return -1

def LZ77Compression(text, windowSize=12):
    result = []
    currentPosition = 0

    while currentPosition < len(text):
        length = 0
        matchPosition = 0
        windowStart = max(0, currentPosition - windowSize)
        searchingWindow = text[windowStart:currentPosition]
        innerLoopPosition = currentPosition

        for len_ in range(1, len(text) - currentPosition):
            currentWord = text[currentPosition:currentPosition + len_]
            position = rabinKarp(searchingWindow, currentWord)

            if position != -1:
                if position + len_ == innerLoopPosition - len_ + 1:
                    patternSize = len_
                    while (
                        innerLoopPosition + patternSize <= len(text)
                        and text[innerLoopPosition:innerLoopPosition + patternSize] == currentWord
                    ):
                        len_ += patternSize
                        innerLoopPosition += patternSize
                    len_ -= 1
                length = len_
                matchPosition = currentPosition - (windowStart + position)
                innerLoopPosition += 1
            else:
                break

        nextSymbol = text[currentPosition + length] if (currentPosition + length) < len(text) else '\0'
        tag = Tag(matchPosition, length, nextSymbol)
        result.append(tag)
        currentPosition += length + 1

    return result
