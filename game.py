import player.py
import deck.py
class game:
    
    def _init_(self):
      
        self.deck= new deck("deck");
        #list of decks
        self.tresure;
        self.boatLocation;
        #list of dice rolles for game
        self.futureDice=[];
        #list of dice for current roll
        self.currDice=[];
        #draw hands for both players first before 
        #initiallizing players so decks are consistant 
        self.p1StartHand=deck.draw();
        self.p2StartHand=deck.draw();
        self.player1= new player(p1StartHand,None,deck,8,None);
        self.player2= new player(p2StartHand,None,deck,8,None);
        self.turnHistory=[];
        self.captain;
        
        
    def rollDice:
        #access future dicerolls and send back
        #previously generated roll based 
        #on self.boatLocation
        return roll
    def newRound:
        #reset position of boat to 0 
        #and player location back on boat
        #deal new card to each player
        #generate all dice rolls for round
        return
    def setCaptain:
        #call between rounds and at start of game
        #use random .5 to choose if start of game
        #otherwise alternate players
        return 
    def getBoatLocation:
        return self.boatLocation
    def setBoatLocation(self,location):
        self.boatLocation=Location
    def endGameOutput:
        #print out turn history treasure and deck to file
        return
    def initTresure:
        #loop call to deck return list 
        #each deck asociatted with a location
        
    def dealTreasure:
        #will have to deal treasure in game loop 
        #will need access to treasure through game
        return Treasure
    def recordTurn:
        return 
    
    

    
    
    

    
