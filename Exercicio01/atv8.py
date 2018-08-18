# 8 Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do
# seu salário no referido mês, sabendo-se que são descontados 11%
# para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
# - salário bruto.
# - quanto pagou ao INSS.
# - quanto pagou ao sindicato.
# - o salário líquido.
# - calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%8 : R$
# - INSS (8%8 : R$
# - Sindicato ( 5%8 : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

print("Informe Valor ganho por hora")
valor_hora = float(input())

print("Informe horas trabalhadas no mês")
horas_trabalhadas = float(input())

salario_bruto = valor_hora * horas_trabalhadas

inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
ir = salario_bruto*0.11

total_descontos = inss+sindicato+ir

salario_liquido = salario_bruto - total_descontos



print("-------------------------------------------"
      "\n| Salario Bruto -------------      %s R$"
      "\n|                                        "
      "\n|               -------------            "
      "\n| INSS                           - %s R$"
      "\n| Sindicato                      - %s R$"
      "\n| IR                             - %s R$"
      "\n| Total Descontos                - %s R$"
      "\n|               -------------            "
      "\n|                       "
      "\n| Salario Liquido                  %s R$"
      "\n--------------------------------------------" %(salario_bruto, inss, sindicato, ir, total_descontos, salario_liquido))