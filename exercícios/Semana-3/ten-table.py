# Escreva um programa que exiba a tabuada de 10 do número inserido

def ten_table(user_input):
    for number in range(1, 11):
        print(f"{user_input} x {number} = {user_input * number}")

user_input = int(input("Type your number: "))
ten_table(user_input)