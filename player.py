import deck as dk
import copy as cp
#Class definition / important functions regarding the "player" object

class Player():
    # Player Initialization
    def __init__(self, equipmentDeck, hand = None, treasure = None,  handSize = None, spyglass = None,cityLocation=None):
        self._hand = []
        if treasure== None:
            self._treasure = 0
        else:
            self._treasure = treasure
        self._handSize = handSize
        if spyglass ==None:
            self._spyglass = 0
        else:
            self._spyglass =spyglass
        self._onBoat = False
        self._cityLocation=cityLocation

        # Keeps a dictionary of what the agent expects to exist in the equipment deck
        self._expectedEquipment = cp.deepcopy(equipmentDeck.getRatio())

    # Getters/Setters
    def getHand(self): return self._hand
    def setHand(self, hand): self._hand = hand

    def getTreasure(self): return self._treasure
    def setTreasure(self, treasure): self._treasure = treasure

    def getExpectedDeck(self): return self._expectedEquipment
    def setExpectedDeck(self, deck): self._expectedEquipment = deck

    def getHandSize(self): return self._handSize
    def setHandSize(self, size): self._handSize = size

    def getSpyglass(self): return self._spyglass
    def setSpyglass(self, spyglass): self._spyglass = spyglass
    
    def setCityLocation(self, newLocation): self.cityLocation=newLocation
    def getCityLocation(self): return self.cityLocation

    # Checks if on boat
    def isOnBoat(self): return self._onBoat
    # Changes boat status
    def changeBoat(self, bool): self._onBoat = bool

    # Player evaluation functions
    def generateHand(self, deck):
        # draw 8 cards
        for i in range(8):
            self._hand.append(deck.draw())
        self._size = 8

        # Update the known equipmentDeck ratios
        for card in self._hand:
            self._expectedEquipment[card] -= 1

    def evaluation(self, eval = "multiplayer"):
        eval = eval.lower() # converts input to lowercase
        if eval is "multiplayer":
            self.multiplayer_evaluation()
        elif eval is "single":
            self.single_evaluation()
        elif eval is "spyglass":
            self.spyglass_evaluation()
        else:
            print(f"Evaluation Type {eval} not recognized")

    def single_evaluation(self):
        return
    def multiplayer_evaluation(self):
        return
    def spyglass_evaluation(self):
        return

    # Player policy functions
    def policy(self, policy = "standard"):
        policy = policy.lower() # converts input to lowercase
        if policy is "standard":
            self.standard_policy()
        elif policy is "Risk":
            self.risk_policy()
        else:
            print(f"Policy Type {policy} not recognized")
    def standard_policy(self):
        return
    def risk_policy(self):
        return
