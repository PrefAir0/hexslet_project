import prompt


ROUNDS_COUNT = 3

def run_game(game_logic, game_rule):
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")

    print(f"Hello, {name}!")
    print(game_rule)

    for i in range(ROUNDS_COUNT):
        question, correct_answer = game_logic()

        print(f"Question: {question}")

        user_answer = prompt.string("Your answer: ")



        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")

            return

    print(f"Congratulations, {name}!")