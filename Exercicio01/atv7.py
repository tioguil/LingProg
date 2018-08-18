# João Papo-de-Pescador, homem de bem, comprou um
# microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o
# estabelecido pelo regulamento de pesca do estado de São Paulo (50
# quilos8 deve pagar uma multa de R$ 4,00 por quilo excedente. João
# precisa que você faça um programa que leia a variável peso (peso
# de peixes8 e verifque se há excesso. Se houver, gravar na variável
# excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.

excesso =0
multa = 0.0

print("digitar peso do Peixe")
peso = float(input())

if peso > 50:
    excesso = peso - 50
    multa = excesso*4
    print("peso excedido: %s KG - valor da multa: %s R$" %(excesso, multa))
    print("peso informado: ",peso, "KG")
else:
    print("Não houve excesso de peso - peso excedido: ",excesso,"KG")
    print("Peso: %s KG- Multa %s R$" %(peso, multa))