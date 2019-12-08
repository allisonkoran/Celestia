import game as gm


def playerLeaves(player):
    prize=Game.dealTreasure()
    prize=player.getTreasure()+prize
    player.setTreasure(prize)
    

    
def doesCaptainHaveResources(roll, capHand):
    capHasResources=True
    removed=False
    haveCards=True
    for die in roll:
        if die !="blank":
            if roll.count(die)>capHand.count(die) and die !="blank":
                haveCards=False
    if haveCards:
        for die in roll:
            if die !="blank":
                for card in capHand:
                    if card== die and removed==False:
                        capHand.remove(card)
                        removed=True
    else:
        capHasResources=False
            
            
    return capHasResources


def getCaptainHand():
    captain=Game.getCaptain()
    if captain==1:
        capHand=Game.player1.getHand()
    else:
        capHand=Game.player2.getHand()
    return capHand


def useSpyglass():
    used=False
    #check if human player will use spyglass
    #check if agent player will use spyglass
    return used


def decideWinner():
    if Game.player1.getTreasure()>Game.player2.getTreasure():
             print("Player 1 Wins!")
    elif Game.player2.getTreasure()>Game.player1.getTreasure(): 
              print("Player 2 Wins!")
    else:
            print("Game is a Tie")
   
    
    
    
    

Game =gm.Game()
Game.gameSetUp()

playerWon=False
firstRound=True

while not(playerWon):
    
    if not(firstRound):
        print("new round")        
        Game.newRound()       
    else:
        firstRound=False
        
    shipSunk=False 

    while not(shipSunk )and Game.getBoatLocation()<9:
        
        #get roll 
        roll=Game.rollDice()
        
        #get hand of captain to compare to dice roll
        capHand=getCaptainHand()
            
        print("cap")
        print(Game.captain)
        print("boat loc")
        print(Game.getBoatLocation())
        
        #players decide to stay or leave
        if Game.getCaptain()==1 and Game.getBoatLocation()>2 :
                print("agent disembarked")
                Game.player2.changeBoat(0)
                
        if (Game.getCaptain()==2 and Game.getBoatLocation()==Game.player1.getCityLocation()) or (Game.getCaptain()==1 and not(Game.player2.isOnBoat())):
            print("To remain on the aircraft type 'stay' to disembark at current city and redeem treasure type 'leave':" )
            humanChoice=input()
            if humanChoice == "leave":
                Game.player1.changeBoat(0)
                print ("player chose to leave")
            
        #if player gets off deal treasure
        if(not(Game.player1.isOnBoat())and Game.getBoatLocation()==Game.player1.getCityLocation()):
            playerLeaves(Game.player1)
        if(not(Game.player2.isOnBoat()) and Game.getBoatLocation()==Game.player2.getCityLocation()):
                playerLeaves(Game.player2)
    
        #check if captain has cards 
        shipSunk=not(doesCaptainHaveResources(roll, capHand))
        
        #evaluate for use of spyyglass if relevant 
        spyglass=False
        spyglass=useSpyglass();
        
        if spyglass== True:
            shipSunk=False
        
        #advance boat to next city irrelivant if boat sinks
        index=Game.getBoatLocation()+1
        while index<9:
            if Game.treasure[index].getSize()>0:
                Game.setBoatLocation(index)
                break 
        #if at last island already set boat location to 9 to break loop
        if index==9:
            Game.setBoatLocation(index)
        #advance player location if still on boat irrelivent if boat sinks 
        if Game.player1.isOnBoat():
            Game.player1.setCityLocation(Game.getBoatLocation())
        if Game.player2.isOnBoat():
            Game.player2.setCityLocation(Game.getBoatLocation())
        
        if (Game.player1.isOnBoat() or Game.player2.isOnBoat()) and not(shipSunk) :
           Game.setCaptain(False)
        else:
            shipSunk=True
            
        loc= Game.getBoatLocation()
        futDice=Game.futureDice
    
    if Game.player1.getTreasure()>=50 or Game.player2.getTreasure()>=50:  
         playerWon=True
         
decideWinner()   
print(Game.player1.getTreasure())  
print(Game.player2.getTreasure())  
    
    
    
    
    
    
  
    
    
