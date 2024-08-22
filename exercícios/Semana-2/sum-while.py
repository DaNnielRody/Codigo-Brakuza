# Escreva um programa com while que faça a soma dos inputs.

stop = True
sum = 0

while stop:
    number = int(input("Type a integer number to sum, or 0 to leave: "))
    sum += number
    if number == 0:
        stop = False

print(f"The sum result is: {sum}")