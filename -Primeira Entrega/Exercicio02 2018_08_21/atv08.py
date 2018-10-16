# 8 Escreva um programa para armazenar uma agenda de telefones
# em um dicionário. Cada pessoa pode ter um ou mais telefones e a
# chave do dicionário é o nome da pessoa. Seu programa deve ter as
# seguintes funções:
#  incluirNovoNome – essa função acrescenta um novo nome na
# agenda, com um ou mais telefones. Ela deve receber como
# argumentos o nome e os telefones.
#  incluirTelefone – essa função acrescenta um telefone em um nome
# existente na agenda. Caso o nome não exista na agenda, você̂ deve
# perguntar se a pessoa deseja inclui-lo. Caso a resposta seja
# afrmativa, use a função anterior para incluir o novo nome.
#  excluirTelefone – essa função exclui um telefone de uma pessoa
# que já está na agenda. Se a pessoa tiver apenas um telefone, ela
# deve ser excluída da agenda.
#  excluirNome – essa função exclui uma pessoa da agenda.
#  consultarTelefone –

def incluir_novo_nome(nome, telefone):
    agenda[nome] = telefone

def incluir_novo_telefone(nome,telefone):
    agenda[nome].append(telefone)

def excluir_telefone(nome,index):
    agenda[nome].pop(index)
    if len(agenda[nome]) == 0:
        excluir_nome(nome)


def excluir_nome(nome):
    agenda.pop(nome)

agenda = {}

print("Opções")
print("Incluir Nome e telefone -> 1")
print("Incluir telefone -> 2")
print("Excluir Nome -> 3")
print("Excluir telefone -> 4")

opcao = -1
while(opcao != 0):

    opcao = int(input("opcao: "))

    if(opcao == 1):
        print("Digite o nome do Fulano")
        nome = input()
        telefones = []
        tel = -1
        while(tel != "0"):
            print("Digite o telefone do ", nome, " - Para sair digite 0")
            tel = input()
            telefones.append(tel)

        incluir_novo_nome(nome, telefones)

    elif opcao == 2:
        print("Digite o nome do Fulano")
        nome = input()

        if nome not in agenda:
            print("Esse nome ainda não esta na agenda, deseja inclui-lo ? - opções S - N")
            incluir = input()
            if incluir == "S":
                print("Digite o nome do Fulano")
                nome = input()
                telefones = []
                tel = -1
                while (tel != "0"):
                    print("Digite o telefone do ", nome, " - Para sair digite 0")
                    tel = input()
                    telefones.append(tel)
                incluir_novo_nome(nome, telefones)
        else:
            tel = -1
            while (tel != 0):
                print("Digite o telefone do ", nome, " - Para sair digite 0")
                tel = input()
                if(tel != "0"):
                    incluir_novo_telefone(nome, tel)
    elif opcao == 3:
        print("Digite o nome do Fulano")
        nome = input()
        excluir_nome(nome)
    elif opcao == 4:
        print("Digite o nome do Fulano")
        nome = input()
        print("Digite o Telefone do Fulano")
        tel = input()
        if tel in agenda[nome]:
            index = agenda[nome].index(tel)
            excluir_telefone(nome,index)

    print(agenda)


