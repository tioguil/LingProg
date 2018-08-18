# 11 Faça um programa que solicite a data de nascimento
# (dd/mm/aaaa8 do usuário e imprima a data com o nome do mês por
# extenso.
# Data de Nascimento: 29/10/1973
# Você nasceu em 29 de Outubro de 1973.
# Obs.: Não use desvio condicional nem loops.

import datetime

print("Informe sua data de nascimento ex: 01/01/2018")
nascimento = input()
ano,mes,dia = map(int, nascimento.split('/'))

tipo_date = datetime.date(dia, mes, ano)

data = tipo_date.strftime('%d/%B/%Y')
dia, mes,ano = map(str, data.split('/'))
print ("Você nasceu em %s de %s de %s" %(dia, mes,ano))