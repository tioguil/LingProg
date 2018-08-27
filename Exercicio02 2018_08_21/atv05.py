# 5 Escreva um programa que conta a quantidade de vogais em uma
# string e armazena tal quantidade em um dicionário, onde a chave é
# a vogal considerada.

print("entre com a frase")
frase = input()

frase = frase.lower()
vogais = 'aeiou'
dicionario = {i: frase.count(i) for i in vogais if i in frase}
print(dicionario)