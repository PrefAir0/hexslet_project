import random
import prompt

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')

    rounds = 3
    correct_answers = 0

    while correct_answers < rounds:

        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        operation = random.randint(1,3)
        
        

        match (operation):
            case 1:
                print(f"Question: {first_number} + {second_number}")
                final_number = str(first_number + second_number)
            case 2:
                print(f"Question: {first_number} - {second_number}")
                final_number = str(first_number - second_number)
            case 3:
                print(f"Question: {first_number} * {second_number}")
                final_number = str(first_number * second_number)

        answer = prompt.string("Your answer: ")


        # print(answer)

        if answer != final_number:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{final_number}'.")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
            correct_answers += 1

    print(f"Congratulations, {name}!")
