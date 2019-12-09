import deck as dk
import copy as cp
import game as gm
import math
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

    def getExpectedDeckSize(self):
        total = 0
        for key, value in self._expectedEquipment.items():
            total += value
        return total

    # Player evaluation functions
    def generateHand(self, deck):
        # draw 8 cards
        for i in range(8):
            self._hand.append(deck.draw())
        self._handSize = 8

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
    def policy(self, game, policy = "standard"):
        policy = policy.lower() # converts input to lowercase
        if policy is "standard":
            self.standard_policy()
        elif policy is "risk":
            self.risk_policy()
        else:
            print(f"Policy Type {policy} not recognized")

    def standard_policy(self, game, weight = 10):
        # Calculate the value of Policy(Stay)
        currentTreasure = game.treasure[game.boatLocation]

        # If the current treasure deck is empty, then the best option is to "Go"
        if currentTreasure.getSize() is 0:
            print(f"Treasure deck at location {game.boatLocation} is empty!")
            return "stay"

        leaveValue = 0
        for key,value in currentTreasure._ratio.items():
            leaveValue += (key * value)

        leaveValue /= currentTreasure.getSize()

        # Calculate the value of Policy(Go->Go->Stay)
        # Effectivly is calculating the value associated with staying on the
        # boat until the next non-captain turn (two player game)

        # Calculate the probability that the opponent has the correct cards

        if game.getCaptain() == 1:
            otherPlayer = game.player2
        else:
            otherPlayer = game.player1


        #Probability = num of card type * (remaining card 'choose' handsize)
        survivalProb = 1
        cardCount = 0
        blanks = 0
        for die in game.currDice:
            if (die is "blank"):
                blanks += 1
                continue
            survivalProb *= self._expectedEquipment[die]
            cardCount += self._expectedEquipment[die]
        survivalProb *= (choose((self.getExpectedDeckSize() - cardCount), (otherPlayer.getHandSize() - len(game.currDice) + blanks)) / (choose(self.getExpectedDeckSize(), otherPlayer.getHandSize())))

        # Calculate the value with staying on the boat (MDP)
        # Value(t + 1) = P(Survive | Current Island, Stay on Ship) * [Reward(Two islands away) + Value(t)(Survive)]
        stayValue = 0
        expectedValue = 0

        # Calculate next island expected Value
        if(game.boatLocation >= 6):
            nextBoat = 7
        else:
            nextBoat = game.boatLocation + 1

        for key, value in game.treasure[nextBoat]._ratio.items():
            expectedValue += (key * value)

        expectedValue /= game.treasure[nextBoat].getSize()

        # Running 10 instance of policy iteration to calculate Value
        discount = weight * sigmoid(stayValue)

        for i in range(10):
            # No need to sum, as "sinking" has a reward of 0 and will always be 0
            stayValue = survivalProb * (expectedValue + (discount * stayValue))

        print(survivalProb)
        #tayValue = survivalProb * expectedValue
        print(f">>> STAY-VALUE: {stayValue} | LEAVE-VALUE: {leaveValue}\n Expected Deck: {self._expectedEquipment}<<<")

        return "leave" if (leaveValue >= stayValue) else "stay"

    def risk_policy(self, game, weight = 25):
        self.standard_policy(game,weight)
        return


    # Helper function to calculate combinatorics
def choose(n, k):
    value = 1
    for i in range(k):
        value *= (n-i) / (k-i)
    return value

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
