import random 

import prompt

rounds_count = 3
lenght_progression = 10


def generate_progression(start, step, length):
    progression = []

    for index in range(length):
        current_element = start + index * step
        progression.append(current_element)

    return progression


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print("What number is missing in the progression?")

    for _ in range(rounds_count):
        start = random.randint(1, 50)
        step = random.randint(1, 10)

        progression = generate_progression(
            start,
            step,
            lenght_progression,
        )

        lost_index = random.randint(0, lenght_progression - 1)

        correct_answer = progression[lost_index]

        progression[lost_index] = ".."

        progression_string = " ".join(map(str, progression))

        print(f"Question: {progression_string}")

        user_answer = int(prompt.string("Your answer: "))

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
