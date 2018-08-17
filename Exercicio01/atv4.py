# 4 Faça um Programa que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius. C = (5 * (F-
# 328 / 98.

print("Digite a temperatura em Farenheit")
tempF = float(input())

tempC = ((tempF - 32) * 5/9)

print("Farenheit : %s -- Celsius: %s" %(tempF,tempC))