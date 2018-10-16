#
# Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do
# seu salário no referido mês.


print("Digite valor ganho por hora")
vhora = int(input())

print("Digite as horas trabalhadas no mês")
htrabalhadas = int(input())
total = vhora * htrabalhadas
print("Salario: %s" %(total))