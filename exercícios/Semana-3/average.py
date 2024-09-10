# Escreva um programa que conte a média ponderada

def average(first_grade, second_grande, third_grade):
    return (first_grade * 2 + second_grande * 3 + third_grade * 5) / (2 + 3 + 5)

my_average = input("Enter your grades, spaced by a space: ")

grades = my_average.split()
grade1 = float(grades[0])
grade2 = float(grades[1])
grade3 = float(grades[2])

weighted_average = average(grade1, grade2, grade3)

print(f"Your weighted average is: {weighted_average:.2f}")