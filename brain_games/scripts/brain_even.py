import random
import prompt

def is_even(number):
    return number % 2 == 0

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds = 3
    correct_answers = 0

    while correct_answers < rounds:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")

        if is_even(number):
            correct_answer = "yes" 
        else: 
            correct_answer = "no"  

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
            correct_answers += 1

    print(f"Congratulations, {name}!")

