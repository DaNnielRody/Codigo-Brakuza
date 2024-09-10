# Crie um programa que converta Celsius para Fahrenheit e Kelvin

user_input = float(input("Type your Celsius temperature: "))

fahrenheit = (user_input * 1.8) + 32
kelvin = user_input + 273.15

print(f"Your temperature in Fahrenheit is {fahrenheit}. In Kelvin is {kelvin}")                              