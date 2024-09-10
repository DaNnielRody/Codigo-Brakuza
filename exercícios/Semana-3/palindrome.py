# Escreva um programa que indique se a entrada é um palíndromo ou não

def palindrome_conversion(user_input):
    original_list = list(user_input)

    is_palindrome = original_list[:]
    is_palindrome.reverse()

    if original_list == is_palindrome:
        print("Is palindrome!")
    else:
        print("Isn't palindrome!")

user_input = input("Type your word: ")

palindrome_conversion(user_input)