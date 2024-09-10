# Escreva um programa que calcule o IMC

def imc_calculator(weight, height)-> float:
    return weight / (height * height)

user_weight = float(input("Type your weight: "))
user_height = float(input("Type your height: "))

print(f"{imc_calculator(user_weight, user_height):.2f}")