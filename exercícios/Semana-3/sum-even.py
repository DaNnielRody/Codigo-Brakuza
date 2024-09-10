# Some todos os pares entre 1 a 100

def is_even(number)-> bool:
    if number % 2 == 0:
        return True
    return False

sum = 0

for number in range(1, 101):
    if is_even(number):
        sum += number

print(f"The sum of the numbers are: {sum}")