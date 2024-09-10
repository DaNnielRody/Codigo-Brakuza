# Escreva um programa que calcule a média de notas inseridas e pare quando o usuário digitar -1

grade_insert = 0
sum = 0

while True:
    user_input = float(input("Type your grade: "))
    if user_input != -1:
        sum += user_input
        grade_insert += 1
    else:
        break

print(f"You inserted {grade_insert} grades. Here's your avarage: {sum / grade_insert}")