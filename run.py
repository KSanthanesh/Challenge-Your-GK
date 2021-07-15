import time
import random

# Heading
print("\n")
print("          ***************************     ")
print("          *                         *     ")
print("          *   CHALLENGE YOUR GK     *     ")
print("          *                         *     ")
print("          ***************************     ")
time.sleep(1)
# Welcome message
print("\nWelcome to my computer quiz!\n")

confirm = input("Do you want to play a Game (yes/no): ")
confirm = confirm.upper()

if confirm in ("Y", "YES"):
    pass
else:
    print("Thank you! Come back later")
    quit()


"""
Enter Name of the user, Game doesnt start without
Name details
"""
# time delay used between displays
time.sleep(0.5)
while True:
    name = input("Please Enter your Name: ")
    if not name:
        print("please Enter your Name before start the game: ")
    else:
        print("Hi " + name + " Let's Start the Game")
        break

time.sleep(0.5)
q1 = """
Which Country is Known as the 'Land of Raising Sun'?
A. Japan
B. New Zealand
C. Fiji
D. China
"""
q2 = """
Which Country is known as the 'Playground of Europe?
A. Austria
B. holland
C. Switzerland
D. Italy
"""

q3 = """
What percentage of the human body is water?
A. 75%
B. 60%
C. 69%
D. 65%
"""

questions = {q1: 'A', q2: 'C', q3: 'B'}


def start():
    """
    Score
    """
    score = 0

    for i in questions:
        print(i)
        answer = input("Enter your Answer(A/B/C/D): ")
        if answer == questions[i]:
            print("Correct Answer!, You got 1 point")
            score += 1
        else:
            print("Incorrect Answer!")
            score -= 1
            display_score(score)


def display_score(score):

    print("Final Score is: ", score)


def play_again():
    """
    Choice given to play again
    """
    response = input("Do you want to Play again:(yes or no): ")
    response = response.upper()
    if response in ("Y", "YES"):
        return True
    elif response in ("N", "NO"):
        return False
    else:
        print("Please enter Valid answer(yes or no)")
        return play_again()


def mix_questions():
    keys = questions.keys()
    random.shuffle(keys)
    for key in keys:
        print(key, questions[key])


start()

while play_again():
    start()
    mix_questions()
