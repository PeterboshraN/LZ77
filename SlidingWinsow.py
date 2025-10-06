class SlidingWindow:
    def __init__(self, data , searchSize , lookaheadSize , cursor): #cursor is the index of the first element in lookahead buffer
        self.data = data
        self.searchSize = searchSize
        self.lookaheadSize = lookaheadSize
        self.cursor = cursor
        self.searchBuffer = data[cursor-searchSize:cursor]
        self.lookaheadBuffer = data[cursor:cursor+lookaheadSize]

    def getSearchBuffer(self):
        return self.searchBuffer
    def getLookAheadBuffer(self):
        return self.lookaheadBuffer
    def findLongestMatch(self):
        if (self.searchBuffer == ""):
            self.cursor += 1
            self.lookaheadBuffer = self.data[self.cursor:self.cursor+self.lookaheadSize]
            self.searchBuffer = self.data[self.cursor-self.searchSize:self.cursor]
            Tag = (0,0,self.lookaheadBuffer[0]) # needs edit    
            return Tag
        # else:
    # still need to implement (Think about it)
            
    
        def hasData(self):
            return self.cursor < len(self.data)


    