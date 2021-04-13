from colorama import Fore
from datetime import datetime

Loja = "Compre Tudo"
Proprietario = "Thiago"
fullname = len('Thiago Felipe Farias dos Santos')
name = len(Proprietario)
print("\n\nEsta é a loja", Loja, ", bem-vindo!\nAqui quem fala é o",
      Proprietario, "!\n")
print(Fore.YELLOW + "Irei realizar sua análise de crédito.\n" + Fore.RESET)

# VERIFICAÇÃO DO LIMITE DE CREDITO DO CLIENTE


def obter_limite():

    curr = datetime.now()
    cargo = str(input("Digite seu cargo:\t\t"))
    salario = float(input("Digite seu salario:\t\t"))
    ano_nascimento = int(input("Digite seu ano de nascimento:\t"))
    ano_atual = datetime.strftime(curr, "%Y")
    idade = int(ano_atual) - int(ano_nascimento)
    limite_de_credito = (salario * (idade / 1000)) + 100

    print("\nCargo:\t\t\t\t{}".format(cargo.capitalize()))
    print('Salario:\t\t\tR$ %.2f' % float(salario))
    print("Ano de nascimento:\t\t" + str(ano_nascimento))
    print('Idade:\t\t\t\t' + str(idade) + ' anos.\n')
    print(Fore.YELLOW + 'Limite de crédito:\t\tR$ %.2f\n' %
          (limite_de_credito) + Fore.RESET)
    qtde = int(input("Quantos itens pretende informar? "))

    return limite_de_credito, idade, qtde


limite_de_credito, idade, qtde = obter_limite()

# VERIFICAÇÃO SE O CLIENTE PODERA COMPRAR A VISTA OU,
# SE DEVERA PARCELAR OU AINDA SE ESTA BLOQUADO PARA A COMPRA


def verifica_produto(limite_de_credito, cont):
    condA = (limite_de_credito * 0.6)
    condB = (limite_de_credito * 0.9)
    produto = str(input("Digite o nome do produto:\t"))
    preco_prod = float(input("Digite o preço do produto:\t"))

    if preco_prod < limite_de_credito:
        if preco_prod <= condA:
            print(Fore.GREEN + "\nAprovado!\n" + Fore.RESET)
        elif preco_prod < condB:
            print(Fore.LIGHTYELLOW_EX +
                  "\nLiberado para parcelar em 2 vezes!\n" + Fore.RESET)
        elif preco_prod < limite_de_credito:
            print(Fore.YELLOW +
                  "\nLiberado para parcelar em 3 ou mais vezes!\n" +
                  Fore.RESET)

        if preco_prod > fullname and preco_prod < idade:
            preco_prod = preco_prod - (preco_prod * (name / 100))
            print("Desconto:\t\t\t" + str(name) + '%')
            print("Valor do produto com desconto:\tR$ %.2f\n" % (preco_prod))
        else:
            print("Produto:\t\t\t" + str(produto).capitalize())
            print("Valor do produto:\t\tR$%.2f\n" % preco_prod)
            limite_de_credito = limite_de_credito - preco_prod
            cont = cont + 1
    else:
        print(Fore.RED + "\nBLOQUEADO!!!" + Fore.RESET)
        print(Fore.RED + "\nNão existe limite de credito disponível para "
              "este item")
        print("Por favor, informe um item de menor valor\n" + Fore.RESET)
    return limite_de_credito, cont


cont = 0
while cont < qtde:
    limite_de_credito, cont = verifica_produto(limite_de_credito, cont)
    print(Fore.YELLOW + 'Limite disponivel para compras:\t\tR$ %.2f\n' %
          (limite_de_credito) + Fore.RESET)
