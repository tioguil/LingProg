# 6 Escreva um programa que lê̂ duas notas de vários alunos e
# armazena tais notas em um dicionário, onde a chave é o nome do
# aluno. A entrada de dados deve terminar quando for lida uma string
# vazia como nome. Escreva uma função que retorna a média do
# aluno, dado seu nome.


entrada = None
dados = {}

while(entrada != ''):
    print("Digite o nome do Aluno")
    nome_aluno = input()
    entrada = nome_aluno
    if nome_aluno != '':
        print("Nota 1")
        nota1 = float(input())
        print("Nota 2")
        nota2 = float(input())
        media = (nota1 + nota2) / 2
        dados[nome_aluno] = [nota1, nota2]

entrada = None
while(entrada != ''):
    print("Ver media, digite o nome do aluno")
    nome_aluno = input()
    entrada = nome_aluno
    if nome_aluno != '':
        print((dados[nome_aluno][0] + dados[nome_aluno][1]) / 2)