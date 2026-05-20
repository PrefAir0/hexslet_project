import random
from brain_games.scripts.engine import run_game

GAME_RULE = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a


def get_game_data():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)

    question = f"{number1} {number2}"

    correct_answer = str(gcd(number1, number2))

    return question, correct_answer


def main():
    run_game(get_game_data, GAME_RULE)
