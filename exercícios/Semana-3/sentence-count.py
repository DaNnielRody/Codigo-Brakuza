# Escreva um programa que conte o número de palavras do usuário

sentence = input("Enter your sentence: ")

words = sentence.split()

word_count = len(words)

print(f"There are {word_count} words in your sentence {sentence}")