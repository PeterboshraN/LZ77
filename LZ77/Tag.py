class Tag:
    def __init__ (self, offset , length , nextSymbol) :
        self.offset = offset
        self.length = length
        self.nextSymbol = nextSymbol

    def __repr__(self):
        return f"({self.offset},{self.length},{self.nextSymbol})"
    
    
    
