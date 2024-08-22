# Crie um programa que encontre e imprima todos os números primos dado um intervalo

def is_prime(number) -> bool:
    if number <= 1:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def range_prime() -> str:
    range_number = int(input("Type the range to find prime numbers: "))
    prime_numbers = []

    for number in range(range_number + 1):
        if is_prime(number):
            prime_numbers.append(number)

    return f"The prime numbers in the range {range_number} are: {prime_numbers}"

print(range_prime())