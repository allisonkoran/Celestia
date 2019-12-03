
# Testing the deck class
import deck as dk
import player as pl

newDeck = dk.Deck({
    "Diamond": 5,
    "Spade": 5,
    "Heart": 5,
    "Club": 5}, "Test"
    )


newDeck.shuffle()


player1 = pl.Player(newDeck)
player2 = pl.Player(newDeck)
player1.generateHand(newDeck)
player2.generateHand(newDeck)

print(newDeck)
print(f"Player1 Hand: {player1.getHand()} | \nPlayer1 Ratios: {player1.getExpectedDeck()} \
\n\nPlayer2 Hand: {player2.getHand()} | \nPlayer2 Ratios: {player2.getExpectedDeck()}")
