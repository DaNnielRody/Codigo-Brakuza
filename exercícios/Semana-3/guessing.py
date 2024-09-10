# Escreva um programa onde o usuário deve adivinhar o número

import random

def guessing():
    try_count = 0
    random_number = random.randint(1, 100)
    
    while try_count < 3:
        user_input = int(input("Type your number: "))
        if user_input < random_number:
            print("Your number is smaller than")
        elif user_input > random_number:
            print("Your number is greater than")
        else:
            print(f"Your guess it's right! Random: {random_number} was Input: {user_input}")
            break
        
        try_count += 1

        if try_count == 3 and user_input != random_number:
            print(f"The random number was {random_number}")


guessing()