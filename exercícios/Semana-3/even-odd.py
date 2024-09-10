# Escreva um programa para retornar se é par ou ímpar

def even_or_odd(user_input)-> str:
    if user_input % 2 == 0:
        return "Even"
    return "Odd"

user_input = int(input("Type your number to be checked: "))
print(even_or_odd(user_input))