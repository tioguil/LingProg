# 7 Defna a função pertenceQ que recebe como argumentos uma lista de números
# inteiros w e um número inteiro n e devolve True se n ocorre em w e False em
# caso contrário.
# Ex: pertenceQ([1,2,3],1) = True
# Ex: pertenceQ([1,2,3],2) = True
# Ex: pertenceQ([1,2,3],3) = True
# Ex: pertenceQ([1,2,3],4) = False



def pertenceQ(w, n):
    return True if n in w else False

print(pertenceQ([1,2,3],1))
print(pertenceQ([1,2,3],2))
print(pertenceQ([1,2,3],3))
print(pertenceQ([1,2,3],4))