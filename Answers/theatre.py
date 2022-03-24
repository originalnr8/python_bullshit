costAdult = 10.50
costChild = 7.30
costOAP = 8.40

def freeTeacher(children):
    if children >9:
        # We can discount adults
        return int(children /10) # we dont care about the remainder so cast to integer
    else:
        return 0

def discountTeacher(adult):
    subtotal = adult * costAdult
    return subtotal

def discountTenPercent(adult, children, OAP):
    subtotalAdults = adult * costAdult
    subtotalChildren = children * costChild
    subtotalOAP = OAP * costOAP
    subtotalTotal = subtotalAdults + subtotalChildren + subtotalOAP
    if subtotalTotal > 100.00:
        return subtotalTotal * 0.1
    else:
        return 0.0

# Prompt for input
## Prompt # in party
strParty = input("How many in your party: ")
try:
    intParty = int(strParty)
except:
    print("Number was not entered")
## Prompt # of adults
strAdults = input("How many adults in your party: ")
try:
    intAdults = int(strAdults)
except:
    print("Number was not entered")
## Prompt # of concessions
strOAP = input("How many concessions in your party: ")
try:
    intOAP = int(strOAP)
except:
    print("Number was not entered")

# Workout out children by omission
intChildren = intParty - intAdults - intOAP
if intChildren < 0:
    # If there are negative "children" answers to questions were stupid
    print("Numbers entered were inaccurate. Exiting")
    exit()

## Children must be chaperoned by one adult
if intChildren > 0 and intAdults == 0 and intOAP == 0:
    print("Children must be chaperoned")
    exit()

# Print in bill as itemised receipt
print("")
print("=== Receipt ===")
## Each item listed with Quantity and subtotal
# print("Total: {0}".format(intParty))
### Adults
chargeAdults = 0
if intAdults > 0:
    chargeAdults = intAdults * costAdult
    strAdults = "%.2f" % chargeAdults
    print("Adults:\t\t\t{0}\t£{1}".format(intAdults, strAdults))
### Children
chargeChildren = 0
if intChildren > 0:
    chargeChildren = intChildren * costChild
    strChildren = "%.2f" % chargeChildren
    print("Children:\t\t{0}\t£{1}".format(intChildren, strChildren))
### Concession
chargeOAP = 0
if intOAP > 0:
    chargeOAP = intOAP * costOAP
    strOAP = "%.2f" % chargeOAP
    print("Concessions:\t\t{0}\t£{1}".format(intOAP, strOAP))
## Discounts listed individually
### Every 10 children = 1 free adult
intAdultsFree = freeTeacher(intChildren)
discountedAdults = discountTeacher(intAdultsFree)
if intAdultsFree > 0:
    strAdultsFree = "-%.2f" % discountedAdults
    print("Chaperone Discount:\t{0}\t£{1}".format(intAdultsFree, strAdultsFree))
### 10% off exceeding £100 after chaperone seats have been discounted
discountTen = discountTenPercent(intAdults - intAdultsFree, intChildren, intOAP)
if discountTen > 0.00:
    strTen = "-%.2f" % discountTen
    print("Big Spender Discount:\t\t£{0}".format(strTen))
## Total
Total = chargeAdults + chargeChildren + chargeOAP - discountedAdults  - discountTen
strTotal = "%.2f" % Total
print("Total:\t\t\t\t£{0}".format(strTotal))


# This is one really really convulted expect a headache