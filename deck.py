# Class definition/ important deck object functions
class Deck():
    # initialize deck object
    def __init__(self, label = None, stack = None, size = None, ratio = {}):
        self._label = label
        self._stack = stack
        self._size = size
        self._ratio = ratio

    # Setter/Getter Functions
    def getLabel(self): return self._label
    def setLabel(self,label): self._label = label

    def getStack(self): return self._stack
    def setStack(self,stack): self._stack = stack

    def getSize(self): return self._size
    def setSize(self,size): self._size = size

    def getRatio(self): return self._ratio
    def setRatio(self,ratio): self._ratio = ratio

    # Deck Class general functions
    def draw(self):
        return

    def shuffle(self):
        return
