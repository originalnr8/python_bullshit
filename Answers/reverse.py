integers = []

while len(integers) <5:
    # prompts for 5 integers
    integers.append(int(input("Enter an integer: ")))
    # store them in an array
# print out integers in reverse order using a loop
for x in range(len(integers),0,-1):
    print(integers[x -1])