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
    return limite_de_credito


obter_limite()

# VERIFICAÇÃO SE O CLIENTE PODERA COMPRAR A VISTA OU,
# SE DEVERA PARCELAR OU AINDA SE ESTA BLOQUADO PARA A COMPRA


def verifica_produto():

    condA = (limite_de_credito * 0.6)
    condB = (limite_de_credito * 0.9)
    produto = str(input("Digite o nome do produto:\t"))
    preco_prod = float(input("Digite o preço do produto:\t"))

    if preco_prod <= condA:
        print(Fore.GREEN + "\nAprovado!\n" + Fore.RESET)
    elif preco_prod < condB:
        print(Fore.LIGHTYELLOW_EX + "\nLiberado para parcelar em 2 vezes!\n" +
              Fore.RESET)
    elif preco_prod < limite_de_credito:
        print(Fore.YELLOW + "\nLiberado para parcelar em 3 ou mais vezes!\n" +
              Fore.RESET)
    else:
        print(Fore.RED + "\nBloqueado!\n" + Fore.RESET)

    # VERIFICAÇÃO DE POSSIVEL DESCONTO DE VALOR DO PRODUTO ESTIVER ENTRE
    # NUMERO DE CARACTERES DO NOME COMPLETO E IDADE
    # NESTE CASO A VARIAVEL fullname TEM 31 CARACTERES DO ALUNO

    if preco_prod > fullname and preco_prod < idade:
        preco_prod = preco_prod - (preco_prod * (name / 100))
        print("Desconto:\t\t\t" + str(name) + '%')
        print("Valor do produto com desconto:\tR$ %.2f\n" % (preco_prod))
    else:
        print("Produto:\t\t\t" + str(produto).capitalize())
        print("Valor do produto:\t\tR$%.2f\n" % preco_prod)
    return


verifica_produto()
