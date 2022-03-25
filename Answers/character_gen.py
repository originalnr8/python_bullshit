import random

traderatio = 2
attr_min = 3

## Each class has minimums (Store in an array of arrays)
### Class   Str     Int     Wis     Dex     Con
### Warrior 15      -       -       12      10
attrWarrior = [15,0,0,12,10]
### Wizard  -       15      10      10      -
attrWizard = [0,15,10,10,0]
### Thief   10      9       -       15      -
attrThief = [10,9,0,15,0]
### Necro   10      10      15      -       -
attrNecromancer = [10,10,15,0,0]

def ChooseYourHero():
    print("Choose your hero's Class:")
    print("1 - Warrior")
    print("2 - Wizard")
    print("3 - Thief")
    print("4 - Necromancer")
    strChoice = input("Make your choice with the number next to it: ")
    choice = 0
    try:
        choice = int(strChoice)
    except:
        print("You didn't enter a number")
        exit()
    return choice

def validateStat(attrPer, attrClass, index):
    if attrPer[index -1] >= attrClass[index -1]:
        return True
    else:
        return False

def validateCharacter(attrPersonal, attrClass):
    for i in range(5):
        if validateStat(attrPersonal, attrClass, i) == False:
            return False
    return True

def validateClass(attrRolled, attrClass):
    return validateCharacter(attrRolled, attrClass)

def findTradable(attr, attrClass):
    trade = []
    for i in range(5):
        minimum = 0
        if attrClass[i] == 0:
            minimum = 3
        else:
            minimum = attrClass[i]
        if attr[i] > minimum:
            excess = attr[i] - minimum
            exchanged = excess / traderatio
            tradepoints = int(exchanged)
            if excess > traderatio:
                trade.append( tradepoints )
            else:
                trade.append(0)
        else:
            trade.append(0)
    return trade

def checkTrade(trade):
    sum = 0
    for x in trade:
        sum += x
    return sum

def showTradable(trade):
    print("")
    for x in range(5):
        if trade[x] > 0:
            spare = trade[x]
            if x == 0:
                print("1 - Strength\t\t {0}pts".format(spare))
            elif x == 1:
                print("2 - Inteligence\t\t {0}pts".format(spare))
            elif x == 2:
                print("3 - Wisdom\t\t {0}pts".format(spare))
            elif x == 3:
                print("4 - Dexterity\t\t {0}pts".format(spare))
            elif x == 4:
                print("5 - Constitution\t\t {0}pts".format(spare))

def choiceToClass(number):
    if number == 1:
        return "Warrior"
    elif number == 2:
        return "Wizard"
    elif number == 3:
        return "Thief"
    elif number == 4:
        return "Necromancer"

def columnToStat(number):
    if number == 0:
        return "Strength"
    elif number == 1:
        return "Intelligence"
    elif number == 2:
        return "Wisdom"
    elif number == 3:
        return "Dexterity"
    elif number == 4:
        return "Constitution"

def showAssignable(attr, attrClass):
    print("")
    for i in range(5):
        if attr[i] < attrClass[i]:
            print("{0} - {1}".format(i+1, columnToStat(i)))

def ChooseAttrMinimum(number):
    if number == 1:
        return attrWarrior
    elif number == 2:
        return attrWizard
    elif number == 3:
        return attrThief
    elif number == 4:
        return attrNecromancer

def tradeStat(sac, ass, attr, attrClass):
    valid = validateStat(attr, attrClass, ass)
    while valid == False:
        if attr[sac -1] - traderatio >= attr_min:
            attr[sac -1] -= traderatio
            attr[ass -1] += 1
        else:
            return attr
        valid = validateStat(attr, attrClass, ass)
    return attr

def showCharacter(choice, attr):
    print("")
    print(choiceToClass(choice))
    for x in range(5):
        print("[{0}]:\t[{1}]".format(columnToStat(x), attr[x]), end = '\t')
    print("")

def showMinimum(attr):
    for x in range(5):
        print("[{0}]:\t[{1}]".format(columnToStat(x), attr[x]), end = '\t')
    print("")

# Prompt for class
## Warrior
## Wizard
## Thief
## Necromancer
chosenClass = ChooseYourHero()
choosenAttr = ChooseAttrMinimum(chosenClass)
# Generate five attributes randomly
## Store in an array
attributes = [random.randint(3,18), random.randint(3,18), random.randint(3,18), random.randint(3,18), random.randint(3,18)]

## If minimums are not reached it can be traded from non-required
### not attribute can go below 3
### trading is 2:1
### Prompt to sacrifice
### Prompt to assign
### Once unable to trade and check if valid
### If not valid tell them to re-roll the character by restarting the program
validClass = validateClass(attributes, choosenAttr)
while validClass == False:
## Compare the character array to the minimum array to check validity (if valid Output everything and leave)
    showCharacter(chosenClass, attributes)
    showMinimum(choosenAttr)
    attrTradable = findTradable(attributes, choosenAttr)
    if checkTrade(attrTradable) > 0:
### List the sacrificible columns
        showTradable(attrTradable)
        sacrifice = int(input("What will you sacrifice to become a {0}: ".format(choiceToClass(chosenClass))))
        showAssignable(attributes, choosenAttr)
        assignment = int(input("What stat would you like to increase: "))
        attributes = tradeStat(sacrifice, assignment, attributes, choosenAttr)
    else:
        print("No more stats able to sacrifice. Re-roll")
        exit()
    validClass = validateClass(attributes, choosenAttr)

### Output stats
### Output sacrifices
showCharacter(chosenClass, attributes)
showMinimum(choosenAttr)

print("")
