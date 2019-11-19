import deck as dk
#Class definition / important functions regarding the "player" object

class Player():
    # Player Initialization
    def __init__(self, hand = None, treasure = None, deck = None, handSize = None, spyglass = None):
        self._hand = hand
        self._treasure = treasure
        self._deck = deck
        self._handSize = handSize
        self._spyglass = spyglass

    # Getters/Setters
    def getHand(self): return self._hand
    def setHand(self, hand): self._hand = hand

    def getTreasure(self): return self._treasure
    def setTreasure(self, treasure): self._treasure = treasure

    def getDeck(self): return self._deck
    def setDeck(self, deck): self._deck = deck

    def getHandSize(self): return self._handSize
    def setHandSize(self, size): self._handSize = size

    def getSpyglass(self): return self._spyglass
    def setSpyglass(self, spyglass): self._spyglass = spyglass

    # Player evaluation functions
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
