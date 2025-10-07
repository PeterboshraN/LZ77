def LZ77Compression(text, windowSize=12):
    result = []
    currentChar = ""
    currentPosition = 0

    while currentPosition < len(text):
        length = 0
        matchPosition = 0
        windowStart = max(0, currentPosition - windowSize)
        searchingWindow = text[windowStart:currentPosition]

        for len_ in range(1, len(text) - currentPosition):
            currentWord = text[currentPosition:currentPosition + len_]
            position = searchingWindow.find(currentWord)
            if position != -1:
                length = len_
                matchPosition = currentPosition - (windowStart + position)
            else:
                break

        nextSymbol = text[currentPosition + length] if (currentPosition + length) < len(text) else '\0'
        tag = Tag(matchPosition, length, nextSymbol)
        result.append(tag)
        currentPosition += length + 1

    return result
