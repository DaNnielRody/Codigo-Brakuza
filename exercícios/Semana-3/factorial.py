# Escreva um programa que calcule o fatorial


def factorial_calculator(user_input):
    factorial = 1
    factors = []

    for number in range(user_input, 0, -1):
        factorial *= number
        factors.append(str(number))

    print(f"{user_input}! = {' x '.join(factors)} = {factorial}")

user_input = int(input("Type your factorial number: "))
factorial_calculator(user_input)