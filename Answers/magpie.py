# Prompt for input 
## Sanitise Input to be number or error message
### Use a try...except
## Santise to numbers you want or error message
### Simple if with a range
number = input("Enter a number for the corresponding line in a nursery rhyme: ")
try:
    integer = int(number)
except:
    print("That wasn't an integer jackass")

range_desired = range(1,7+1)
if integer not in range_desired:
    print("Number entered is outside of the quantity of lines in the nursery rhyme")

# Display garbage from that magpie song
## One for sorrow
## Two for joy
## Three for a girl
## Four for a boy
## Five for silver
## Six for gold
## Seven for a secret never to be told
### Just enumerate that shit (Enumeration is class based and way ahead of this stuff so I'm IFing)
if integer == 1:
    print("One for sorrow")
elif integer == 2:
    print("Two for joy")
elif integer == 3:
    print("Three for a girl")
elif integer == 4:
    print("Four for a boy")
elif integer == 5:
    print("ive for silver")
elif integer == 6:
    print("Six for gold")
elif integer == 7:
    print("Seven for a secret never to be told")
else:
    print("Somehow something slipped through that shouldn't")

