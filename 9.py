# 9-Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).



print("Digite a temperatura em Fahrenheit")
tempF = float(input())
tempC = 5*((tempF-32)/9)
print(f"A temperatura em Celcius é {tempC}")