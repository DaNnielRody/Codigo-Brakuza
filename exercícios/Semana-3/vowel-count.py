# Escreva um programa que conte as vogais de uma frase do usuário

vowels = {"a", "e", "i", "o", "u"}
vowels_count = 0
user_input = input("Type your phrase: ")

for letter in user_input:
    if letter in vowels:
        vowels_count += 1

print(f"Vowels counted: {vowels_count}")