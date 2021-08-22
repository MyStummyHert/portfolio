def new_game():
    guesses = []  # answers - user input.
    correct_guesses = 0  # right answers.
    question_num = 1  # current question.

    # loop to go throught the questions and print them.
    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -----------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


# -----------------------------------------------
def display_score(correct_guesses, guesses):
    print("------------------------------------")
    print("RESULTS")
    print("------------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in Guesses:
        print(i, end="")
    print()


# -----------------------------------------------
def play_again():
    pass


# -----------------------------------------------
# making a dictionary with the game's questions - while the.
questions = {"what's the capital of france?: ": "C",
             "what's the capital of england?: ": "D",
             "what's the capital of japan?": "A",
             "what's the capital of the USA?: ": "D"
