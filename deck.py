# Class definition/ important deck object functions
import random
class Deck():
    # initialize deck object
    # Ratio passed in as a dictionary of Card : # of Card pairs
    def __init__(self, ratio, label = None):
        self._label = label
        self._stack = []

        self._ratio = ratio

        # Generate deck
        for card, num in ratio.items():
            for i in range(num):
                self._stack.append(card)

        self._size = len(self._stack)
    def __str__(self):
        return ', '.join([str(elem) for elem in self._stack])

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
        if self._size <= 0:
            print("The deck is empty!")
            return None

        card = self._stack.pop()
        self._ratio[card] = self._ratio.get(card) - 1 # Update ratio of remaining cards
        self._size -= 1
        return card

    def shuffle(self):
        random.shuffle(self._stack)
