import random

def convertCard(value):
    range_numbers = range(2,10 +1)
    if value in range_numbers:
        return str(value)
    elif value == 1:
        return "Ace"
    elif value == 11:
        return "Jack"
    elif value == 12:
        return "Queen"
    elif value == 13:
        return "King"
    else:
        print("Card Value {0}".format(value))
        return "Joker"

def displayCards(deck):
    print("")
    for x in deck:
        #.format     - allows substitution of variables in structured responsed
        #, end = ' ' - allows you to print all on one line
        print("[{0}]".format(x), end = ' ')
    print("")
    print("")

def loopGuess():
    guess = ""
    while guess == "":  # while guess is blank the user hasn't input a guess properly
        print("Will the next card be higher or lower? ")
        guess = str(input("Type higher or lower: "))   # get the input
        if guess != "higher" and guess != "lower":  # check the input is what we want or not
            print("Your guess was not higher or lower") # if not blank it so we loop again
            guess = ""
    return guess

def drawAnotherCard():
    if len(cards) == 0: # WE've never done this before so just return a number
        return convertCard(random.randint(1,13))

    lastcard = cards[len(cards) -1]    # pick the last card
    nextcard = 0                    # zero new card
    while nextcard == 0:            # while zero keep trying
        nextcard = convertCard(random.randint(1,13)) # generate new value
        if lastcard == nextcard:        # is it the same as the last?
            # Neither higher or lower so draw again
            nextcard = 0
    return nextcard

def predictCorrectly(deck):
    cards_dealt = len(deck)
    lastcard = deck[cards_dealt -1]
    newcard = deck[cards_dealt -2]
    if accepted_guess == "higher":
        if lastcard > newcard:
            print("You guess higher correctly")
        else:
            print("You guessed badly")
    else:
        if lastcard < newcard:
            print("You guessed lower correctly")
        else:
            print("You guessed badly")

cards = []
# Part 1 - Generate random number from 1 - 13
## You can generate any numbers as long as they relate to 1-13. 
### One line of code to create the actual card

# Part 1 - Enumerate Playing Card values to numbers generated
## Enumeration allows you to change one value into another directly.
## So the 1 of Spades is actually called Ace of Spades, 2-10 are face value, 11 is Jack, 12 is Queen and 13 is King
## This is where the number generation goes from 1-13 to Playing Card values
### As enumeration is a class based thing and we are WELL away from that but would be a better method so 
cards.append(drawAnotherCard())

# Part 1 - Print Playing Card Value not the number (unless it is the face value for 2-10)
## Created a function to display all cards in a fashion
displayCards(cards)

# Part 2 - Prompt user to guess whether the next card will be higher or lower.
## If the card is equal the guess is incorrect
accepted_guess = loopGuess()

# Draw another card
cards.append(drawAnotherCard())

# Part 2 - Display the second card
## This should show the previous card too for context
displayCards(cards)

# Part 2 - Display appropriate message based upon guess accuracy
predictCorrectly(cards)

