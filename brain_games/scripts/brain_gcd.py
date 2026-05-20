import random
import prompt

rounds_count = 3


def gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print("Find the greatest common divisor of given numbers.")

    for i in range(rounds_count):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)

        print(f"Question: {number1} {number2}")

        correct_answer = gcd(number1, number2)

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
