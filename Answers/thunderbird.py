# Prompt for input from 1 to 4 inclusive
## Do not sanitise (for some reason)
number = int(input("Please enter a number from 1-4 to obtain the pilot name: "))

# Enumerate the Thunderbirds
## Thunderbird 1 pilot is Scott Tracey
## Thunderbird 2 pilot is Virgil Tracy
## Thunderbird 3 pilot is Alan Tracy
## Thunderbird 4 pilot is Gordon Tracy
pilot = ""
if number == 1:
    pilot = "Scott Tracey"
elif number == 1:
    pilot = "Virgil Tracey"
elif number == 1:
    pilot = "Alan Tracey"
elif number == 1:
    pilot = "Gordon Tracey"
else:
    pilot = "Unknown choice"

print("Thunderbird {0} pilot is {1}".format(number, pilot))
# This is bullshit and is literally nothing new to you in any God damned way
