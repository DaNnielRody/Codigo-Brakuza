# Crie uma função para retornar par ou ímpar

def is_even_or_odd(number) -> str:
    return "Is even" if number % 2 == 0 else "Is odd"

number_input = int(input("Type an int number, odd or even: "))

print(is_even_or_odd(number_input))