# Escreva um programa que peçaa temperatura atual e diga como está

def temperature(degrees) -> str:
    if(degrees > 30):
        return "It's hot"
    elif(degrees < 15):
        return "It's cold"
    return "It's pleasent"

degree = float(input("Type your temperature: "))
print(temperature(degree))