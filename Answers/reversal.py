lower = 10
upper = 10000000000
attempt = 0
while attempt >= 0:
    # prompt for an integer >1 and <11 or 10-9,999,999,999
    try:
        attempt = int(input("Enter an integer above 10 and below 10 million (or negative to exit): "))
    except:
        print("An integer dumbass")
    # moan if that doesn't happen
    if attempt <0:
        exit()
    elif attempt < lower or attempt > upper:
        print("Did you read the instructions?")

    # output the reverse of that number
    reversed = 0
    while attempt != 0:
        digit = attempt % 10                # Find remainder of number
        reversed = reversed * 10 + digit    # Multiply current by 10 and add remainder
        attempt //= 10                      # Divide by 10 and rounddown to remove last digit

    print("Reversed Number: " + str(reversed))
    # prompt for another number
    # exit when negative number is input


