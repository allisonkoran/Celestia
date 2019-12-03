import game as gm


def playerLeaves(player):
    prize=Game.dealTreasure()
    prize=player.getTreasure()+prize
    player.setTreasure(prize)

def doesCaptainHaveResources(roll, capHand):
    capHasResources=True
    removed=False
    for die in roll:
        if capHand.count(die)>0:
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


Game =gm.Game()
Game.gameSetUp()
playerWon=False
firstRound=True
while not(playerWon):
    
    if not(firstRound):
        Game.newRound()
    else:
        firstRound=False
        
    shipSunk=False   
    while not(shipSunk):
        
        #get roll 
        roll=Game.rollDice()
        
        #get hand of captain to compare to dice roll
        capHand=getCaptainHand()
            
        #players decide to stay or leave
        
        
        #if player gets off deal treasure
        if(not(Game.player1.isOnBoat())):
            playerLeaves(Game.player1)
        if(not(Game.player2.isOnBoat())):
                playerLeaves(Game.player2)
    
        #check if captain has cards 
        shipSunk=doesCaptainHaveResources(roll, capHand)
    
    
    
