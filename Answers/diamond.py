padding = " "
mark = "*"

def pad(start, length):
    finish = ""
    midpoint = int(length /2)   # rounddown(7/2) = 3
    middle = int((length -(len(start) -1)) /2)
    for x in range(middle):
        finish += padding
    finish += start
    for x in range(middle -1):
        finish += padding
    return finish[:length]

# input width
width = int(input("Enter the width required: "))
# acceptable input 2-40
if width <2 or width >40:
    print("Unacceptable width!")
# appropriate message
total_width = (width * 2) -1
top = 0
for x in range(width):
    top += 1
height = (top *2) - 1

i = 1
peak = False
section = ""
for x in range(height):
    section = ""
    for y in range(i):
        section += mark + padding
    if i == width:
        peak = True
    if peak == False:
        i += 1
    else:
        i -= 1
    line = pad(section, total_width)
    print(line)
