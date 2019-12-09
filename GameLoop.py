import game as gm


def playerLeaves(player):
    prize=Game.dealTreasure()
    if prize ==0:
        player.setSpyglass(player.getSpyglass()+1)
    print("treasure dealt: %d" %(prize))
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
            removed=False
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


def agentSpyglassUsed():
    used=False
    #check if human player will use spyglass
    #check if agent player will use spyglass
    return used

def humanSpyglassUsed():
    used=False
    print("You have %d spyglasses!" %(Game.player1.getSpyglass()))
    print("Would you like to use a spyglass to advance the aircraft to the next city? Type 'yes' or 'no':")
    sg=input()
    if sg == "yes":
        used=True;
    return used

def decideWinner():
    #add in value of unused spyglass treasure cards to final score
    player1Total=Game.player1.getTreasure() + (Game.player1.getSpyglass()*2)
    player2Total=Game.player2.getTreasure() + (Game.player2.getSpyglass()*2)

    if player1Total>player2Total:
             print("Player 1 Wins!")
    elif player2Total> player1Total:
              print("Player 2 Wins!")
    else:
            print("Game is a Tie")

def printHumanPlayerInfo():
     print('\nYour hand:  {0}'.format(Game.player1.getHand()) )
     print("Your Spyglasses: %d" %(Game.player1.getSpyglass()))
     print("Your Treasure Total(w/out spyglasses): %d\n" %(Game.player1.getTreasure()))






Game =gm.Game()
Game.gameSetUp()

playerWon=False
firstRound=True
shipSunk=False
shipEmpty=False

agentCorrectCount = 0
while not(playerWon):

    if not(firstRound):
        if shipSunk:
            print("\n\nCaptain Failed Aircraft Sank\n\n")
        print("Starting New Round")
        #deal treasure is players made it to final city Location
        Game.setBoatLocation(8)
        if Game.player1.isOnBoat() and not(shipSunk):
            playerLeaves(Game.player1)
        if Game.player2.isOnBoat() and not(shipSunk):
            playerLeaves(Game.player2)

        #set up next round
        Game.newRound()
    else:
        firstRound=False

    shipSunk=False
    shipEmpty=False
    while not(shipSunk)and not(shipEmpty) and Game.getBoatLocation()<9:

        #get roll
        roll=Game.rollDice()

        #get hand of captain to compare to dice roll
        capHand=getCaptainHand()
        print("      -------------------------------------------           " )
        print("captain is: player %d" %(Game.captain))
        print("Aircraft is located at: city number %d"%(Game.getBoatLocation()))
        print('Dice results:  {0}\n'.format(roll))
        #print('for testing-> captain hand: {0}'.format(capHand))
        if(Game.captain==2 or not(Game.player2.isOnBoat())):
           printHumanPlayerInfo()

        #players decide to stay or leave

        if ((Game.getCaptain()==1 and Game.player2.isOnBoat())):
            if Game.player2.getSpyglass() > 0:
                if Game.player2.risk_policy(Game) is "leave":
                    print(">>>> Agent disembarked")
                    Game.player2.changeBoat(0)
                else:
                    print(">>>> Agent chose to stay")
            else:
                if Game.player2.standard_policy(Game) is "leave":
                    print(">>>> Agent disembarked")
                    Game.player2.changeBoat(0)
                else:
                    print(">>>> Agent chose to stay")

        elif (Game.getCaptain()==2 and not(Game.player1.isOnBoat())):
            if Game.player2.single_policy(Game) is "leave":
                print(">>>> Agent disembarked")
                Game.player2.changeBoat(0)
            else:
                print(">>>> Agent chose to stay")

        elif (Game.getCaptain()==2 and Game.player1.isOnBoat()) or (Game.getCaptain()==1 and not(Game.player2.isOnBoat())):
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
        if not((Game.player1.isOnBoat() or Game.player2.isOnBoat())):
            shipEmpty=True
            print("Captain Disembarked From Aircraft\n")
        if not(shipEmpty):

            #check if captain has cards
            shipSunk=not(doesCaptainHaveResources(roll, capHand))

            #evaluate for use of spyyglass if relevant
            spyglass=False
            if Game.player1.getSpyglass()>0 and shipSunk and Game.player1.isOnBoat():
                spyglass=humanSpyglassUsed();
            elif Game.player2.getSpyglass()>0 and shipSunk and Game.player2.isOnBoat():
                 spyglass=agentSpyglassUsed()

            #if spyglass used ship saved from sinking
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

            #only call set captain if advancing to next city otherwise it willl be called in newRound
            if (Game.player1.isOnBoat() or Game.player2.isOnBoat()) and not(shipSunk) :
               Game.setCaptain(False)
            else:
                #start new round if everyone got off ship
                shipEmpty=True

        if not(shipSunk) and not(shipEmpty):
            print("\n\nCaptian Succeeded Aircraft Continues on to next city \n\n" )

    if Game.player1.getTreasure()>=50 or Game.player2.getTreasure()>=50:
         playerWon=True

decideWinner()
print(Game.player1.getTreasure())
print(Game.player2.getTreasure())
