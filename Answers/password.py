# Input a password
password = input("Enter a password: ")
# Store a password

# Input THE password
print("Can you guess the password?")
guess = input("Try: ")

# If they match (regardless of case) output a welcome
if password.lower() == guess.lower():
    print("Well done!")
else:
    print("Incorrect")

# This is garbage as an example but has string comparisons and string modifiers.
# I don't know what the fuck the analysis is on about
