# import random
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

time.sleep(1)


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
    print("Thank you for playing! You got ", score, "/5 questions correct.")
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
    "7. ?\n": "",
    "8. ?\n": "",
    "9. ?\n": "",
    "10. ?\n": "",
    "11. ?\n": "",
    "12. ?\n": "",
    "13. ?\n": "",
    "14. ?\n": "",
    "15. ?\n": "",

}

# choices given for answers using lists
options = [
    ["A. Japan", "B. New Zealand", "C. Fiji", "D. China\n"],
    ["A. Austria", "B. holland", "C. Switzerland", "D. Italy\n"],
    ["A. 75%", "B. 60%", "C. 69%", "D. 65%\n"],
    ["A. The Carolina Reaper", "B. Ghost Pepper", "C. Pot Barrackpore",
     "D. Pot Red\n"],
    ["A. China", "B. India", "C. Africa", "D. Russia|n"],
    ["A. ", "B. ", "C. ", "D. |n"],
    ["A. ", "B. ", "C. ", "D. |n"],
    ["A. ", "B. ", "C. ", "D. |n"],
    ["A. ", "B. ", "C. ", "D. |n"],
    ["A. ", "B. ", "C. ", "D. |n"],
    ["A. ", "B. ", "C. ", "D. |n"],
    ["A. ", "B. ", "C. ", "D. |n"],
    ["A. ", "B. ", "C. ", "D. |n"],
    ["A. ", "B. ", "C. ", "D. |n"],
    ["A. ", "B. ", "C. ", "D. |n"]
    ]

start()

while play_again():
    start()

print("Thanks for playing this game!")
