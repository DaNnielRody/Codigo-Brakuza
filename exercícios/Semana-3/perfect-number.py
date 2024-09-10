# Escreva um programa que verifique o número perfeito

number = int(input("Enter a number: "))

sum_divisors = 0

for i in range(1, number):
    if number % i == 0:
        sum_divisors += i

if sum_divisors == number:
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")