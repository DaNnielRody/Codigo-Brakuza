# Escreva um programa que peça dois números e exiba a operação

def calculator(number1, number2) -> float: 

    operation_sign = input("Type your operator(+, -, *, /): ")
    
    match operation_sign:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "/":
            if(number2 != 0):
                return number1 / number2
            return "Can't be 0 as denominator"
        case "*":
            return number1 * number2
        case _: # default case
            return 0

first_numer = float(input("Type your first number: "))
second_number = float(input("Type your second number: "))

print(calculator(first_numer, second_number))