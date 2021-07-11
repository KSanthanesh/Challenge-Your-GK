# import random
# from random import randrange
import time

# Heading
print("***************************")
print("*                         *")
print("*   CHALLENGE YOUR GK     *")
print("*                         *")
print("***************************")
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


def start():
    """
    Game start and answer the question
    """
    choices = []
    correct_choices = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        choice = input("Enter Your Answer (A,B,C or D): ")
        choice = choice.upper()
        choices.append(choice)
        correct_choices += check_answer(questions.get(key), choice)
        question_num += 1
    display_score(correct_choices, choices)


time.sleep(0.5)


def check_answer(answer, choice):
    """
    Command given an answers
    """
    if answer == choice:
        print("\nWell done! Correct Answer!\n")
        return 1
    else:
        print("\nIncorrect Answer!\n")
        return 0


def display_score(correct_choices, choices):
    """
    Score display
    """
    print("----------------------------")
    print("Results")
    print("----------------------------")
    score = int(correct_choices)
    print("Thank you for playing! You got ", score, "/",
          len(questions), "questions correct.")
    mark = int(score/len(questions) * 100)
    print("Score is : ", str(mark) + "%\n")


time.sleep(1)


def play_again():
    """
    Choice given to play again
    """
    response = input("Do you want to Play again:(yes or no): ")
    response = response.upper()
    if response in ("Y", "YES"):
        return True
    else:
        return False


# Questions and correct answers using dictionaries
questions = {
    "1. Which Country is Known as the 'Land of Raising Sun'?\n": "A",
    "2. Which Country is known as the 'Playground of Europe'?\n": "C",
    "3. What percentage of the human body is water?\n": "B",
    "4. What is the hottest chilli pepper in the world?\n": "A",
    "5. Which Country has the biggest Land Area?\n": "D",
    "6. How many legs does a butterfly have?\n": "B",
    "7. What is the popular spice in the world?\n": "A",
    "8. What kind of tree do acorns grow on?\n": "C",
    "9. Which Country has the most Volcanoes?\n": "D",
    "10. What is the most spoken language in the world?\n": "B",
    "11. Which is the hottest planet in the Solar system?\n": "D",
    "12. Which European Country was the first to allow women to vote?\n": "A",
    "13. What is the degree of triangle?\n": "C",
    "14. What is the Chemical symbol for table salt?\n": "D",
    "15. What is the largest three digit prime number?\n": "B",

}


# choices given for answers using lists
options = [
    ["A. Japan", "B. New Zealand", "C. Fiji", "D. China\n"],
    ["A. Austria", "B. holland", "C. Switzerland", "D. Italy\n"],
    ["A. 75%", "B. 60%", "C. 69%", "D. 65%\n"],
    ["A. The Carolina Reaper", "B. Ghost Pepper", "C. Pot Barrackpore",
     "D. Pot Red\n"],
    ["A. China", "B. India", "C. Africa", "D. Russia\n"],
    ["A. Four", "B. Six ", "C. Eight", "D. Two\n"],
    ["A. Pepper", "B. Paprika ", "C. Thyme", "D. Chilli\n"],
    ["A. Ash", "B. Birch", "C. Oak", "D. Rowan\n"],
    ["A. Japan", "B. Russia ", "C. Chile", "D. Indonesia\n"],
    ["A. English", "B. Chinese", "C. German", "D. French\n"],
    ["A. Jupiter", "B. Mars", "C. Mercury", "D. Venus\n"],
    ["A. Finland", "B. Germany", "C. France", "D. Ireland\n"],
    ["A. 240 degree", "B. 360 degree", "C. 180 degree", "D. 90 degree\n"],
    ["A. Sodium hydroxide", "B. Sodium bicarbonate", "C. Sodium Carbonate",
     "D. Sodium Chloride\n"],
    ["A. 995", "B. 997", "C. 999", "D. 993\n"]
    ]

start()

while play_again():
    start()

print("Thanks for playing this game!")
