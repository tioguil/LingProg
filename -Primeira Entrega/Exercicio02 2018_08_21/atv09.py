# 9 Faça um programa que leia um arquivo texto contendo uma lista
# de endereços IP e gere um outro arquivo, contendo um relatório dos
# endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

import socket

ipsValidos = []
ipsInvalidos = []

ips = open("ips.txt")
for ip in ips:
    try:
        socket.inet_aton(ip)
        # Validos
        ipsValidos.append(ip)
    except socket.error:
        # Invalidos
        ipsInvalidos.append(ip)
        
ips.close()

saida = open("ipsvalidados.txt", "w+")

saida.write("[Endereços válidos:]\n")
for ip in ipsValidos:
    saida.write(ip)
    
saida.write("[Endereços inválidos:]\n")
for ip in ipsInvalidos:
    saida.write(ip)
    
saida.close()