print("***************************")
print("*                         *")
print("*   CHALLENGE YOUR GK     *")
print("*                         *")
print("***************************")
# Welcome message
print("\nWelcome to my computer quiz!\n")


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter(A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(correct_guesses, guesses):
    print("----------------------------")
    print("Results")
    print("----------------------------")
    print("Answers:", end="")
    for i in questions:
        print(questions.get(i), end="")
        print()
    print("guesses:", end="")
    for i in guesses:
        print(i, end="")
        print()
    score = int(correct_guesses / len(questions) * 100)
    print("Your Score is : " + str(score) + "%")


def play_again():
    response = input("Do you want to Play again:(yes or no): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False


questions = {
    "Which Country is Known as the 'Land of Raising Sun'?": "A",
    "Which Country is known as the 'Playground of Europe'?": "C",
    "What percentage of the human body is water?": "B",
    "What is the hottest chilli pepper in the world?": "A",
    "Steel is more elastic than Rubber because:": "C",
}

options = [
    ["A. Japan", "B. New Zealand", "C. Fiji", "D. China"],
    ["A. Austria", "B. holland", "C. Switzerland", "D. Italy"],
    ["A. 75%", "B. 60%", "C. 69%", "D. 65%"],
    ["A.The Carolina Reaper", "B.Ghost Pepper", "C.Pot Barrackpore",
     "D.Pot Red"],
    ["A.its density is high", "B.it is a metal",
     "C.ratio of stress to strain is more",
     "D. ratio of stress to strain is less"]]

new_game()

while play_again():
    new_game()

print("Byeeee")
