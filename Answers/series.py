arr_int = []
while len(arr_int) <5:
    # Prompt for 5 integers
    str_input_number = input("Input integer: ")
    ## didn't say about assumptions so check for integers at least
    try:
        input_number = int(str_input_number)
    except:
        print("##### Number not entered jackass")
    ## Positive and negative only so test for this
    if input_number == 0:
        print("###### Not zero dumbass")
    else:
        arr_int.append(input_number)

sum_positives = 0
sum_negatives = 0
# Sum the positive numbers
# Sum the negative numbers
## Testing for positivity also proves negativity if you are sneaky enough
for x in arr_int:
    if x >0:
        sum_positives += x
    else:
        sum_negatives += x
# Output the totals of both to the CLI
## Sum of postive integers: ?
## Sum of negative integers: ?
print("Sum of positive integers: {0}".format(sum_positives))
print("Sum of negative integers: {0}".format(sum_negatives))
