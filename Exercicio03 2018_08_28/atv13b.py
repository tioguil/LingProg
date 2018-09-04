# 13. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome: ")
idade = int(input("entre com sua Idade: "))
salario = float(input("Salario: "))
sexo = input("sexo: ")
estado_civil = input("Estado Civil:")

if len(nome) > 3 :
    print("Nome Valido!")
else:
    print("Nome Invalido")

if idade > 0 and idade < 150 :
    print("Idade Valido!")
else:
    print("Idade Invalido")

if salario > 0:
    print("Salario Valido!")
else:
    print("Salario Invalido")

if sexo == "f" or sexo == 'm':
    print("Sexo Valido!")
else:
    print("Sexo Invalido")

if estado_civil in ['s', 'c', 'v', 'd']:
    print("Estado Civil Valido!")
else:
    print("Estado Civil Invalido")