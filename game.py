import player as ply
import deck as dk
import random as rnd

class Game:

    def _init_(self, deck=None, boatLocation=None, player1=None, player2=None, futureDice=None, currDice=None, treasure=None, turnHistory=None,captain=None):

        self.deck= deck
        self.boatLocation=boatLocation
        self.treasure=treasure
        self.futureDice=futureDice
        self.currDice=currDice
        self.player1=player1
        self.player2= player2
        self.turnHistory=[]
        self.captain=captain

        self.RelativeTreasureValues = None


    def gameSetUp(self):

        #set up equipment deck
        ratio={"cloud":20,
               "lightning":18,
               "bird":16,
               "pirate":14
               }
        self.deck= dk.Deck(ratio,"deck")
        self.deck.shuffle()

        #start boat pos 0
        self.setBoatLocation(0)

        #init players and hands
        self.player1= ply.Player(self.deck)
        self.player2= ply.Player(self.deck)
        self.player1.generateHand(self.deck)
        self.player2.generateHand(self.deck)
        self.player1.changeBoat(1)
        self.player2.changeBoat(1)
        self.player1.setCityLocation(self.boatLocation)
        self.player2.setCityLocation(self.boatLocation)

        #init treasure decks
        self.treasure=self.initTreasure()

        #init expectedValues
        self.generateRelativeTreasureValues()

        #generate dice rolls for round
        self.generateFutureRolls()

        #set staring captain (true to indicate first round/start of game)
        self.setCaptain(True)


    def generateFutureRolls(self):
        #genearte rand num between 1 & 6 then assign string
        #1&2=blank, 3=cloud, 4=lightning, 5=bird, 6=pirate
        dice=[]
        value=0
        for i in range(35):
            value=rnd.randint(1,6)
            if value == 1 or value== 2:
                dice.append("blank")
            elif value==3:
                 dice.append("cloud")
            elif value==4:
                 dice.append("lightning")
            elif value==5:
                 dice.append("bird")
            elif value==6:
                 dice.append("pirate")
        self.futureDice=dice

    def generateRelativeTreasureValues(self):
        # Generate each island's expected values relative to the score cap

        # First, generate expected values
        expectedValues = []
        for deck in self.treasure:
            average = 0
            totalCards = 0

            for key, value in deck._ratio.items():
                average += (key * value)
                totalCards += value
            average /= totalCards
            average /= 50 # Treasure needed to win
            expectedValues.append(average)

        self.RelativeTreasureValues = expectedValues




    def rollDice(self):
        #access future dicerolls and send back
        #previously generated roll based
        #on self.boatLocation
        #1&2=blank, 3=cloud, 4=lightning, 5=bird, 6=pirate
        roll=[]
        if self.getBoatLocation()<3:
            for x in range(2):
                #rpop=self.futureDice.pop(0)
                #print(rpop)
                roll.append(self.futureDice.pop(0))

        elif 3<= self.getBoatLocation() and self.getBoatLocation()<6:
            for x in range(3):
                roll.append(self.futureDice.pop(0))
        else:
           for x in range(4):
                roll.append(self.futureDice.pop(0))
        self.currDice=roll
        return self.currDice

    def newRound(self):
        #reset position of boat to 0 or lowest value city still with treasure deck
        for index, deck in enumerate(self.treasure):
            if deck.getSize()>0:
                self.setBoatLocation(index)
                break

        #and player location back on boat and set player city location to boat location
        self.player1.changeBoat(1)
        self.player2.changeBoat(1)
        self.player1.setCityLocation(self.boatLocation)
        self.player2.setCityLocation(self.boatLocation)

        #new captain(false= not first round)
        self.setCaptain(False)

        #deal new card to each player
        self.player1._hand.append(self.deck.draw())
        self.player2._hand.append(self.deck.draw())

        #generate all dice rolls for round
        self.generateFutureRolls()

        return



    def setCaptain(self,gameStart):
        #call between rounds and at start of game
        #use random .5 to choose if start of game
        #otherwise alternate players

        if gameStart==True:
            print("setting captain randomly")
            self.captain=rnd.randint(1,2)
        elif self.captain==1 and self.player2.isOnBoat():
            self.captain=2
        elif self.captain==2 and self.player1.isOnBoat():
            self.captain=1
        return

    def getCaptain(self):
        return self.captain

    def getBoatLocation(self):
        return self.boatLocation

    def setBoatLocation(self,location):
        self.boatLocation=location

    def getDeck(self):return self.deck

    def endGameOutput(self):
        #print out turn history treasure and deck to file
        print(self.turnHistory)
        print(self.treasure)
        print(self.deck)


    def initTreasure(self):

        #hardcode ratio create deck of treasure for each city append ot list of treasure
        t=[]
        r1={0:1,1:5,2:3,4:2}
        t.append(dk.Deck(r1,"t1"))

        r2={0:1,2:5,4:3,6:2}
        t.append( dk.Deck(r2, "t2"))

        r3={0:1,4:5,6:3,9:1}
        t.append(dk.Deck(r3, "t3"))

        r4={0:1,6:5,9:3,12:1}
        t.append( dk.Deck(r4, "t4"))

        r5={9:6,12:3}
        t.append(dk.Deck(r5, "t5"))

        r6={12:6,15:3}
        t.append(dk.Deck(r6, "t6"))

        r7={15:6}
        t.append(dk.Deck(r7, "t7"))

        r8={20:6}
        t.append(dk.Deck(r8, "t8"))


        r9={25:5}
        t.append(dk.Deck(r9, "t9"))
        return t

    def dealTreasure(self):
        #will have to deal treasure in game loop
        #will need access to treasure through game
        #index by boatlocation
        #index treasure list shuffle deck at index draw card from deck
        index=self.getBoatLocation()
        while self.treasure[index].getSize()<1 and index<9:
            index=index+1
        self.treasure[index].shuffle()
        card=self.treasure[index].draw()
        return card


    def recordTurn(self,dice, cardsPlayed, treasureDealt):
        turn=[]
        turn.append(dice)
        turn.append(cardsPlayed)
        turn.append(treasureDealt)
        self.turnHistory.append(turn)

        return 
    

