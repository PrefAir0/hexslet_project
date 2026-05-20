import random 
import prompt
from brain_games.scripts.engine import run_game

GAME_RULE = "What number is missing in the progression?"

PROGRESSION_LENGTH = 10


def generate_progression(start, step, length):
    progression = []

    for index in range(length):
        current_element = start + index * step
        progression.append(current_element)

    return progression


def get_game_data():
    start = random.randint(1, 50)
    step = random.randint(1, 10)

    progression = generate_progression(
        start,
        step,
        PROGRESSION_LENGTH,
    )

    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer


def main():
    run_game(get_game_data, GAME_RULE)


if __name__ == "__main__":
    main()