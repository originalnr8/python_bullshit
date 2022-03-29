# store colours in array
newton_rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]   # rainbow expressed by Isaac Newton who had a weird thing about the number 7 and so the six colours were required to be seven
real_rainbow = ["red", "orange", "yellow", "green", "blue", "violet"]    # actual rainbow
song_rainbow = ["red", "yellow", "pink", "green", "purple", "orange", "blue"]   # the "i can sing a" rainbow

rainbow = real_rainbow
# continually prompt for integer from 1-7 to -1
number = 0
while number >= 0:
    number = int(input("Enter a number from 1-{0} to obtain the corresponding colour of the rainbow: ".format(len(rainbow))))
    if number >= 1 and number <= len(rainbow):
        # output colour from rainbow
        print(rainbow[number -1])
    elif number < 0:
        exit()
    else:
        print("Not a valid number location for a rainbow colour")

