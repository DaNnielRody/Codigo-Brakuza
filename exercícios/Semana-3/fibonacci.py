# Escreva um programa que mostre os primeiros números da sequência de fibonacci

number = int(input("Enther the n number of Fibonacci: "))

a,b = 0, 1

for _ in range(number):
    print(a, end=" ")
    a, b = b, a + b