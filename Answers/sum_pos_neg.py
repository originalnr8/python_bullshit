input_number = []
# input 10 integers
input_number.append(int(input("Enter first integer: ")))
input_number.append(int(input("Enter second integer: ")))
input_number.append(int(input("Enter third integer: ")))
input_number.append(int(input("Enter fourth integer: ")))
input_number.append(int(input("Enter fifth integer: ")))
input_number.append(int(input("Enter sixth integer: ")))
input_number.append(int(input("Enter seventh integer: ")))
input_number.append(int(input("Enter eigth integer: ")))
input_number.append(int(input("Enter ninth integer: ")))
input_number.append(int(input("Enter tenth integer: ")))

positives = []
negatives = []
# you must use a single for loop to accomplish this
for x in input_number:
    if x > 0:
        positives.append(x)
    elif x < 0:
        negatives.append(x)
# output sum of all positive numbers and sum of all negative numbers
print("Positive Sum: {0}".format(positives))
print("Negative Sum: {0}".format(negatives))