# 2. Faça um Programa que verifque se uma letra digitada é vogal ou
# consoante.

a = input("entre com uma letra")
list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if a in list:
    print("Vogal")
else:
    print("consoante")