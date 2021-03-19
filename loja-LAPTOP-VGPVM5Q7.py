from colorama import Fore
from datetime import datetime
import pandas as pd

Loja = "Compre Tudo"
Proprietario = "Thiago Felipe!"
print("\n\nEsta é a loja", Loja, ", bem-vindo!\nAqui quem fala é o",
      Proprietario, "\n")

print(Fore.YELLOW + "Irei realizar sua análise de crédito.\n" + Fore.RESET)

curr = datetime.now()
cargo = str(input("Digite seu cargo: "))
salario = float(input("Digite seu salario: "))
ano_nascimento = int(input("Digite seu ano de nascimento:"))
ano_atual = datetime.strftime(curr, "%Y")
idade = int(ano_atual) - int(ano_nascimento)


print("\nCargo: ", cargo)
print('Salario: R$ %.2f' % float(salario))
print("Ano de nascimento: ", str(ano_nascimento))
print('Idade: ', idade, 'anos.\n')

limite_de_credito = (salario * (idade / 1000)) + 100
print(Fore.YELLOW + 'Limite de crédito: R$ %.2f\n' %
      (limite_de_credito) + Fore.RESET)


d = {"Cargo": cargo, "salario": salario, "Ano de nascimento":
     ano_nascimento, "Idade": idade, "Limite de credito":   limite_de_credito}

d = pd.Series(d)

print(d)
