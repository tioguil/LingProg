#
# 4 Faça um programa que percorre uma lista com o seguinte
# formato: [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]],
# ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que
# cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e
# Itália, o Brasil fez 10 faltas e a Itália fez 9.
# O programa deve imprimir na tela:
# - o total de faltas do campeonato
# - o time que fez mais faltas
# - o time que fez menos faltas

list = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]

print("Pais      Faltas")
for x in range(len(list)):

    print(list[x][0], "     ", list[x][2][0])
    print(list[x][1], "     ", list[x][2][1])
    print("-------------------------")