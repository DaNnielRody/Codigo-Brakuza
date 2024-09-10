# Escreva um programa que calcule a área de um circulo a partir do raio oferecido pelo usuário

import math

radius = float(input("Type the radius of the circle: "))

area = math.pi * radius ** 2

print(f"The are of the circle with radius {radius} is {area:.2f}")