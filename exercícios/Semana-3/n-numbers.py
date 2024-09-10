# Escreva um programa que exiba a soma dos primeiros n números naturais de um número 

number = int(input("Enter your number: "))

total_sum = 0 

for i in range(1, number+1):
    total_sum += i

print(f"The sum of the first {number} natural numbers is {total_sum}")