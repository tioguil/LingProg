# 5 Defina a função contem_parQ que recebe como argumento uma lista de números inteiros w e devolve True se w contém um número par e False em caso contrário.
# Ex: contem_parQ([2,3,1,2,3,4]) = True
# Ex: contem_parQ([1,3,5,7]) = False

def contem_parQ(w):
    return False if len(w) == 0 else False if w[len(w) - 1] % 2 != 0 and not contem_parQ(w[:-1]) else True

print(contem_parQ([2,3,1,2,3,4]))
print(contem_parQ([1,3,5,7]))
