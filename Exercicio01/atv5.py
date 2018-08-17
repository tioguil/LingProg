# 5 Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Farenheit.

print("Digite a temperatura em Celsius")
tempC = float(input())

tempF = (tempC * 1.8 + 32)

print("Celsius : %s -- Farenheit: %s" %(tempC, tempF))