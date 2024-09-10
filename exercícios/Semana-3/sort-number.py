# Escreva um programa que imprima a ordem crescente dos três primeiros números

def sort_numbers(first_number, second_number, third_number):
    sorted_numbers = []

    sorted_numbers.append(first_number)
    sorted_numbers.append(second_number)
    sorted_numbers.append(third_number)

    sorted_numbers.sort()

    for number in sorted_numbers:
        print(number)

first_number = int(input("Type your first number: "))
second_number = int(input("Type your second number: "))
third_number = int(input("Type your third number: "))

sort_numbers(first_number, second_number, third_number)

