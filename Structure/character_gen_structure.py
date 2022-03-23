# Prompt for class
## Warrior
## Wizard
## Thief
## Necromancer

# Generate five attributes randomly
## Store in an array
## Each class has minimums (Store in an array of arrays)
### Class   Str     Int     Wis     Dex     Con
### Warrior 15      -       -       12      10
### Wizard  -       15      10      10      -
### Thief   10      9       -       15      -
### Necro   10      10      15      -       -

## If minimums are not reached it can be traded from non-required
### not attribute can go below 3
### trading is 2:1
### Prompt to sacrifice
### Prompt to assign
### Once unable to trade and check if valid
### If not valid tell them to re-roll the character by restarting the program

## Compare the character array to the minimum array to check validity (if valid Output everything and leave)
### List the sacrificible columns
### Output stats
### Output sacrifices


