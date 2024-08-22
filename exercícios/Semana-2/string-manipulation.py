# Escreva um programa que conte a aparição de uma letra em específico

# First way using 'count' method:
def count_letter_1() -> str:
    user_input = input("Type a word: ")
    letter_count = user_input.count("a")
    return f"You find the letter 'a' {letter_count} times"

# Second way using pure python:
def count_letter_2() -> str:
    letter_count = 0
    user_input = input("Type a word: ")

    for letter_case in user_input:
        if letter_case == "a":
            letter_count += 1
    return f"You find the letter 'a' {letter_count} times"

print(count_letter_1())
print(count_letter_2())