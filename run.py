import time

# Heading and start the time in 0.5 sec
time.sleep(0.5)
print("***************************")
print("*                         *")
print("*   CHALLENGE YOUR GK     *")
print("*                         *")
print("***************************")
# Welcome message
print("\nWelcome to my computer quiz!\n")

time.sleep(1.5)
# Confirmation before start the game
response = input("Do you want to Play the quiz(y/n): ")
time.sleep(0.5)
if response.lower() == "y":
    print("ok! let's play the quiz!:)")
elif response.lower() == "n":
    quit()
    print("Bye! Thank You!")
else:
    print("Please enter y (or) n to play the game")
