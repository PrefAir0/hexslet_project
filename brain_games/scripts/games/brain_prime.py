import prompt
import random

from brain_games.scripts.engine import run_game

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def get_game_data():
    number = random.randint(1, 100)

    question = str(number)

    correct_answer = "yes" if is_prime(number) else "no"

    return question, correct_answer


def main():
    run_game(get_game_data, GAME_RULE)


if __name__ == "__main__":
    main()