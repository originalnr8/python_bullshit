import random
from xml.dom import ValidationErr

cards_available = [2,3,4,5,6,7,8,9,10,11,12,13,1]
card_count = 4      # How many different cards
columns = 10         # X grid dimension
rows = 4            # Y grid dimension
card_facedown = "[ ]"
card_found = "[X]"

def createDeck():
    # Calculate pairs within grid
    total_cards = columns * rows                    # 16 = 4x4
    if total_cards % 2 > 0:
        print("Odd number of cards present so you cannot play snap")
        exit()
    pairs_count = total_cards // (card_count *2)    # 1 = 16 / (5 *2)
    deck = []
    for x in range(card_count):
        deck.append(pairs_count)                    # [1,1,1,1,1]
    
    # Check there are no left over pairs
    all_cards = card_count * pairs_count * 2        # 10 = 5 * 1 * 2
    leftover_pairs = int((total_cards - all_cards) / 2)
    if leftover_pairs == 0:
        return deck
    for x in range(leftover_pairs):
        deck[x] += 1
    
    return deck

def num2card(number):
    range_numbers = range(2,10 +1)
    if number in range_numbers:
        return str(number)
    elif number == 1:
        return "A"
    elif number == 11:
        return "J"
    elif number == 12:
        return "Q"
    elif number == 13:
        return "K"
    else:
        return str(number)

def card2num(card):
    if card == "A":
        return 1
    elif card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    else:
        return int(card)

# Populate 4x4 array with 4 cards (Jack, Queen King Ace) randomly placed
def genGrid(thing):
    grid = []
    for x in range(columns):
        line = []
        for y in range(rows):
            line.append(thing)
        grid.append(line)
    return grid

def genCardValues():
    values = cards_available[-card_count:]
    return values

def genCard():
    return random.randint(1,card_count)

def genLocation():
    loc = []
    loc.append(random.randint(0,columns -1))
    loc.append(random.randint(0,rows -1))
    return loc

def genPair(card):
    generated = False
    while generated == False:
        location = genLocation()
        if gridCards[location[0]][location[1]] == 0:
            gridCards[location[0]][location[1]] = card
            gingerated = False
            while gingerated == False:
                location_new = genLocation()
                if gridCards[location_new[0]][location_new[1]] == 0:
                    gridCards[location_new[0]][location_new[1]] = card
                    gingerated = True
                    generated = True

def popPairs(card, pairs):
    for x in range(pairs):
        genPair(card)

def popGrid():
    values = genCardValues()
    quantity = createDeck()
    for x in range(len(values)):
        popPairs(values[x], quantity[x])

def mergeGridtoGame(grid):
    # Setup the headers to the deck
    headers_columns =[]
    #headers_columns.append(" ")
    for x in range(columns):
        headers_columns.append(str(x))

    headers_rows =[]
    headers_rows.append(" ")
    for y in range(rows):
        headers_rows.append(str(y))

    # Setup the top header
    game = []
    line = []
    #for y in range(len(headers_rows)):
    #    line.append(headers_rows[y])
    #game.append(line)
    game.append(headers_rows)

    # Setup the rest
    for x in range(len(headers_columns)):
        line = []
        for y in range(len(headers_rows)):
            if y == 0:
                line.append(headers_columns[x])
            else:
                line.append(grid[x][y -1])
        game.append(line)

    return game

def displayGameGrid(game):
    padding = "\t"
    for y in range(rows +1):
        for x in range(columns +1):
            print(num2card(game[x][y]), end = padding)
        print("")
    print("############################")

def askforPosition():
    position = []
    # Prompt for row position
    ok_y = False
    while ok_y == False:
        try:
            position_y = int(input("Enter row integer: "))
        except:
            print("Integer not entered")
        if position_y < 0 or position_y > rows -1:
            print("Integer not in range")
        ok_y = True
    # Prompt for column position
    ok_x = False
    while ok_x == False:
        try:
            position_x = int(input("Enter column integer: "))
        except:
            print("Integer not entered")
        if position_x < 0 or position_x > columns -1:
            print("Integer not in range")
        ok_x = True
    position.append(position_x)
    position.append(position_y)
    return position

def fetchCard(location):
    return gridCards[location[0]][location[1]]

def displayGuess(location):
    if gridGuessing[location[0]][location[1]] == card_facedown:
        print("Card is facedown")
        gridGuessing[location[0]][location[1]] = fetchCard(location)
    elif gridGuessing[location[0]][location[1]] == card_found:
        print("Card already found")
        return False
    else:
        print("Card is faceup")
        return False
    return True

def hideCards(loc1, loc2, infill):
    gridGuessing[loc1[0]][loc1[1]] = infill
    gridGuessing[loc2[0]][loc2[1]] = infill

def checkGrid(grid):
    for y in range(columns -1):
        for x in range(rows -1):
            if grid[x][y] == card_facedown:
                return False
    return True

# Create hidden card grid
gridCards = genGrid(0)
popGrid()

# Create Guessing grid
gridGuessing = genGrid(card_facedown)

# Display a guessing grid
showtime = mergeGridtoGame(gridGuessing)
displayGameGrid(showtime)

total_guesses = 0
grid_Complete = False
while grid_Complete == False:
    # Display card at position
    valid_pick = False
    while valid_pick == False:
        first_choice = askforPosition()
        valid_pick = displayGuess(first_choice)
    # Display a guessing grid
    showtime = mergeGridtoGame(gridGuessing)
    displayGameGrid(showtime)

    # Prompt for second card position
    valid_pick = False
    while valid_pick == False:
        second_choice = askforPosition()
        valid_pick = displayGuess(second_choice)
    showtime = mergeGridtoGame(gridGuessing)
    displayGameGrid(showtime)

    if gridCards[first_choice[0]][first_choice[1]] == gridCards[second_choice[0]][second_choice[1]]:
        ## If Match print a message
        print("SNAP!! Well done")
        # Found Pair should be an X
        hideCards(first_choice, second_choice, card_found)
    else:
        ## If not match print message
        print("Try again")
        hideCards(first_choice, second_choice, card_facedown)
    showtime = mergeGridtoGame(gridGuessing)
    displayGameGrid(showtime)
    total_guesses += 1
    grid_Complete = checkGrid(gridGuessing)
# Upon no pairs left display number of guesses
print("All Pairs Found Bye")