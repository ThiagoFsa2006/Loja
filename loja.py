from colorama import Fore
from datetime import datetime

Loja = "Compre Tudo"
Proprietario = "Thiago"
print("\n\nEsta é a loja", Loja, ", bem-vindo!\nAqui quem fala é o",
      Proprietario, "!\n")

print(Fore.YELLOW + "Irei realizar sua análise de crédito.\n" + Fore.RESET)

curr = datetime.now()
cargo = str(input("Digite seu cargo: "))
salario = float(input("Digite seu salario: "))
ano_nascimento = int(input("Digite seu ano de nascimento:"))
ano_atual = datetime.strftime(curr, "%Y")
idade = int(ano_atual) - int(ano_nascimento)
fullname = len('Thiago Felipe Farias dos Santos')
name = len(Proprietario)


print("\nCargo: ", cargo)
print('Salario: R$ %.2f' % float(salario))
print("Ano de nascimento: ", str(ano_nascimento))
print('Idade: ', idade, 'anos.\n')

limite_de_credito = (salario * (idade / 1000)) + 100
print(Fore.YELLOW + 'Limite de crédito: R$ %.2f\n' %
      (limite_de_credito) + Fore.RESET)

condA = (limite_de_credito * 0.6)
condB = (limite_de_credito * 0.9)

produto = str(input("Digite o nome do produto: "))
preco_prod = float(input("Digite o preço do produto: "))

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

if preco_prod < idade:
    preco_prod = preco_prod - (preco_prod * (name / 100))
    print("Desconto:", str(name), '%')
    print("Valor do produto com desconto: R$ %.2f\n" % (preco_prod))
else:
    print("Produto:", str(produto))
    print("Valor do produto: R$ %.2f\n" % preco_prod)
