import random

def draw():
    return random.randint(1,3)

def convert(number):
    if number == 1:
        return "Rock"
    elif number == 2:
        return "Paper"
    else:
        return "Scissor"

def hands(text):
    hand = text.lower()
    if hand == "rock":
        return 1
    elif hand == "paper":
        return 2
    elif hand == "scissors":
        return 3
    else:
        print("You did not enter one of the right words ({0})".format(text))

def compare(one, two):
    if one == 1 and two == 1:
        return 0
    elif one == 1 and two == 2:
        return 2
    elif one == 1 and two == 3:
        return 1
    elif one == 2 and two == 1:
        return 1
    elif one == 2 and two == 2:
        return 0
    elif one == 2 and two == 3:
        return 2
    elif one == 3 and two == 1:
        return 2
    elif one == 3 and two == 2:
        return 1
    elif one == 3 and two == 3:
        return 0

def winner(number):
    if number ==1:
        return "You WIN"
    if number ==2:
        return "Computer WINS"
    else:
        return "Well we both tried"

def showMatch(one, two, result):
    print("[{0}] [{1}]".format(convert(one), convert(two)))
    print(winner(result))

ply1 = 0
ply2 = 0
win = False
while win == False:
    # Prompt to enter rock paper or scissors
    person = hands(input("Enter Rock or Paper or Scissors: "))
    # Generate rock paper scissors
    computer = draw()
    result = compare(person, computer)
    showMatch(person, computer, result)
    if result == 1:
        ply1 += 1
    elif result == 2:
        ply2 += 1
    else:
        i= 0    # no score for a draw
    # first to 3 not best of
    if ply1 >= 3:
        win = True
    elif ply2 >= 3:
        win = True

# output winner and scores
if ply1 >= 3:
    print("You WIN the Match")
elif ply2 >= 3:
    print("Robot uprising commencing")
