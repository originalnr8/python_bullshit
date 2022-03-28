# input columns
columns = int(input("Enter the number of desired columns: "))
# input rows
rows = int(input("Enter the number of desired rows: "))
# output grid of asterisks with those details
line = ""
for x in range(columns):
    line = ""
    for y in range(rows):
        line += "* "
    print(line)
    