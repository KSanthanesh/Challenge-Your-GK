# import random
import time
print("***************************")
print("*                         *")
print("*   CHALLENGE YOUR GK     *")
print("*                         *")
print("***************************")
time.sleep(1)
# Welcome message
print("\nWelcome to my computer quiz!\n")

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

        if choice == ("A", "B", "C", "D", "a", "b", "c,", "d"):
            break
        else:
            print("please Enter valid option")

        correct_choices += check_answer(questions.get(key), choice)
        question_num += 1
    display_score(correct_choices, choices)


time.sleep(1)


def check_answer(answer, choice):
    if answer == choice:
        print("\nWell done! Correct Answer\n")
        return 1
    else:
        print("\nWrong Answer\n")
        return 0


def display_score(correct_choices, choices):
    print("----------------------------")
    print("Results")
    print("----------------------------")
    print("Answers: ", end="\n")
    for i in questions:
        print(questions.get(i), end="")
        print()
    print("Choices: ", end="\n")
    for i in choices:
        print(i, end="")
        print()
    score = int(correct_choices / len(questions) * 100)
    print("Your Score is : " + str(score) + "%\n")


time.sleep(1)


def play_again():
    response = input("Do you want to Play again:(yes or no): ")
    response = response.upper()
    if response in ("Y", "YES"):
        return True
    else:
        return False


questions = {
    "1. Which Country is Known as the 'Land of Raising Sun'?\n": "A",
    "2. Which Country is known as the 'Playground of Europe'?\n": "C",
    "3. What percentage of the human body is water?\n": "B",
    "4. What is the hottest chilli pepper in the world?\n": "A",
    "5. Steel is more elastic than Rubber because:\n": "C",
}

options = [
    ["A. Japan", "B. New Zealand", "C. Fiji", "D. China\n"],
    ["A. Austria", "B. holland", "C. Switzerland", "D. Italy\n"],
    ["A. 75%", "B. 60%", "C. 69%", "D. 65%\n"],
    ["A. The Carolina Reaper", "B. Ghost Pepper", "C. Pot Barrackpore",
     "D. Pot Red\n"],
    ["A. its density is high", "B. it is a metal",
     "C. ratio of stress to strain is more",
     "D. ratio of stress to strain is less\n"]]

start()

while play_again():
    start()

print("Thanks for playing this game!")
