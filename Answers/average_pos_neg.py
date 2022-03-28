# Using code from Task 1 as a guide
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
positive_sum = 0
negatives = []
negative_sum = 0

for x in input_number:
    if x > 0:
        positive_sum += x
        positives.append(x)
    elif x < 0:
        negative_sum += x
        negatives.append(x)

# Appropriate messages if:
## no positives are entered
## no negatives are entered
if len(positives) < 1:
    print("No positive values entered")
if len(negatives) < 1:
    print("No negative values entered")

# Sum posititve values
# Average positive values
# Sum negative values
# Average negative values
print("Positive Sum: {0}".format(positive_sum))
print("Positive Average: {0}".format(positive_sum / len(positives)))
print("Negative Sum: {0}".format(negative_sum))
print("Negative Average: {0}".format(negative_sum / len(negatives)))