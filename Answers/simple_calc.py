# Prompt for first integer, second integer, operator delimited by spaces
print("Integers are numbers without decimal point numbers such as 2 but not 2.1")
print("Operators are mathematical symbols that do things such as + - * /")
print("Delimit with spaces")
input_string = input("Enter an integer, another integer and an operator:")
## Delimit entry
### delimit and wedge into an array
input_array = input_string.split()
## Check for three things input
input_length = len(input_array)
if input_length != 3:
    print("You didn't do what was asked")
    exit()
integer_first = int(input_array[0])
integer_second = int(input_array[1])
operator = input_array[2]

## Check first two are numbers and then positive
### do each check separately for ease
if integer_first <= 0:
    print("Only positivity allowed")
    exit()
if integer_second <= 0:
    print("Only positivity allowed")
    exit()
## Check final is an operator
### string comparison maybe a switch statement
if operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("You didn't supply an operator")
    exit()

# Output the calculation result as text
## Your sum is <blah> and the answer is <answer>
### Fucking stupid terminology and inaccurate to boot
result = 0
if operator == "+":
    result = integer_first + integer_second
elif operator == "-":
    result = integer_first - integer_second
elif operator == "*":
    result = integer_first * integer_second
elif operator == "/":
    result = integer_first / integer_second

calculation = str(integer_first) + " " + operator + " " + str(integer_second)
print("Your sum is {0} and the answer is {1}".format(calculation, result))
