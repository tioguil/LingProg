# 1 Crie um programa que recebe uma lista de números e
# - retorne o maior elemento
# - retorne a soma dos elementos
# - retorne o número de ocorrências do primeiro elemento da lista
# - retorne a média dos elementos
# - retorne o valor mais próximo da média dos elementos
# - retorne a soma dos elementos com valor negativo
# - retorne a quantidade de vizinhos iguais


def negativo(num):
    if num < 0:
        return True

    else:
        return False

def vizinhos(num):
    if num < 0:
        return True

    else:
        return False

total_lista = 5
print("Preencha a lista com numeros")

list = []

for i in range(total_lista):
    list.append(int(input()))

media = (sum(list)// total_lista)

maisProximo = list[0]
diferenca = media - list[0]
menorDiferenca = diferenca
for num in list:
    diferenca = media - num
    if diferenca == 0:
        maisProximo = num
    if diferenca < 0:
        diferenca = diferenca * -1
    if diferenca < menorDiferenca:
        menorDiferenca = diferenca
        maisProximo = num

print("Maio elemento do Array: ", max(list))
print("Soma dos elementos: ", sum(list))
print("Primeiro elemento da lista: ",list[0])
print("Média da list: ", (sum(list)/ total_lista))
print("Valor mais próximo da média dos elementos: ", maisProximo)
soma_negativo = filter(negativo, list)
print("soma dos elementos negativos", sum(soma_negativo))
print("Quantidade de vizinhos iguais: " )