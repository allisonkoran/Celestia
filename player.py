import deck as dk
#Class definition / important functions regarding the "player" object

class Player():
    # Player Initialization
    def __init__(hand = None, treasure = None, deck = None, handSize = None, spyglass = None):
        self._hand = hand
        self._treasure = treasure
        self._deck = deck
        self._handSize = handSize
        self._spyglass = spyglass

    # Getters/Setters
    def getHand(): return self._hand
    def setHand(hand): self._hand = hand

    def getTreasure(): return self._treasure
    def setTreasure(treasure): self._treasure = treasure

    def getDeck(): return self._deck
    def setDeck(deck): self._deck = deck

    def getHandSize(): return self._handSize
    def setHandSize(size): self._handSize = size

    def getSpyglass(): return self._spyglass
    def setSpyglass(spyglass): self._spyglass = spyglass

    # Player evaluation functions
    def evaluation(eval = "multiplayer"):
        eval = eval.lower() # converts input to lowercase
        if eval is "multiplayer":
            multiplayer_evaluation()
        elif eval is "single":
            single_evaluation()
        elif eval is "spyglass":
            spyglass_evaluation()
        else:
            print(f"Evaluation Type {eval} not recognized")

    def single_evaluation():
        return
    def multiplayer_evaluation():
        return
    def spyglass_evaluation():
        return

    # Player policy functions
    def policy(policy = "standard"):
        policy = policy.lower() # converts input to lowercase
        if policy is "standard":
            standard_policy()
        elif policy is "Risk":
            risk_policy()
        else:
            print(f"Policy Type {policy} not recognized")
    def standard_policy():
        return
    def risk_policy():
        return
