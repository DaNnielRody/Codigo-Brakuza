# Escreva um programa que exbia o maior, menor e a média dos números inseridos

def get_numbers():
    numbers = []
    print("Enter numbers (type 'exit' to finish):")
    
    while True:
        entry = input("Enter a number: ")
        
        if entry.lower() == 'exit':
            break
        
        numbers.append(float(entry))
    
    return numbers

def calculate_statistics(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    average = sum(numbers) / len(numbers)
    
    print(f"\nLargest number: {largest}")
    print(f"Smallest number: {smallest}")
    print(f"Average: {average:.2f}")

def main():
    numbers = get_numbers()
    if numbers:
        calculate_statistics(numbers)
    else:
        print("No numbers were entered.")
