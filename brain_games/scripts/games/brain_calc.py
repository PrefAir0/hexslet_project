import random

from brain_games.scripts.engine import run_game

GAME_RULE = "What is the result of the expression?"

OPERATORS = ["+", "-", "*"]


def calculate(number1, number2, operator):
    match operator:
        case "+":
            return number1 + number2

        case "-":
            return number1 - number2

        case "*":
            return number1 * number2


def get_game_data():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    operator = random.choice(OPERATORS)

    question = (
        f"{first_number} "
        f"{operator} "
        f"{second_number}"
    )

    correct_answer = str(
        calculate(
            first_number,
            second_number,
            operator,
        )
    )

    return question, correct_answer


def main():
    run_game(get_game_data, GAME_RULE)


if __name__ == "__main__":
    main()