import random


# simulate rolling two dice
def dice_roll():
    return random.randint(1,6)

def die_roll():
    die = []
    die.append(dice_roll())
    die.append(dice_roll())
    history.append(die)
    return die

def showDie(die):
    for x in die:
        print("[{0}]".format(x), end = ' ')
    print("\tTotal Roll Count: {0}".format(total_rolls))

def dieMatch(die):
    if die[0] == die [1]:
        return True
    else:
        return False

# count how many throws until they match
total_rolls = 0
history = []
match = False
while match == False:
    roll = die_roll()
    total_rolls += 1
    showDie(roll)
    match = dieMatch(roll)
# the value of the die should be output with each roll