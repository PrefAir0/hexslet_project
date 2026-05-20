import prompt
import random

round_count = 3


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(round_count):
        number = random.randint(1, 100)

        print(f"Question: {number}")

        correct_answer = "yes" if is_prime(number) else "no"

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
