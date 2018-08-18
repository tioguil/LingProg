# 12 Leet é uma forma de se escrever o alfabeto latino usando outros
# símbolos em lugar das letras, como números por exemplo. A própria
# palavra leet admite muitas variações, como l33t ou 1337. O uso do
# leet reflete uma subcultura relacionada ao mundo dos jogos de
# computador e internet, sendo muito usada para confundir os
# iniciantes e afrmar-se como parte de um grupo. Pesquise sobre as
# principais formas de traduzir as letras. Depois, faça um programa
# que peça uma texto e transforme-o para a grafa leet speak.
# Desafo: não use loops nem desvios condicionais.


from utilitybelt import change_charset

print("Informe uma frase")
frase = input()

origspace = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
keyspace  = "4bcd3fgh1?k£mnopqr57uvwxyz4BCD3FGHI?KLMNOPQR57UVWXYZ_"

trad = change_charset(frase,origspace, keyspace)
print(trad)