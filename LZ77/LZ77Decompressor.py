def LZ77Decompression(tags):
    result = ""
    for tag in tags:
        offset, length, nextSymbol = tag.offset, tag.length, tag.nextSymbol
        if offset == 0 and length == 0:
            result += nextSymbol
        else:
            start = len(result) - offset
            for i in range(length):
                result += result[start + i]
            if nextSymbol != '\0':
                result += nextSymbol
    return result
