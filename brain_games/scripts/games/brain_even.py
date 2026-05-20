import random
import prompt

from brain_games.scripts.engine import run_game

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game_data():
    number = random.randint(1, 100)

    question = str(number)

    correct_answer = "yes" if is_even(number) else "no"

    return question, correct_answer


def main():
    run_game(get_game_data, GAME_RULE)


if __name__ == "__main__":
    main()