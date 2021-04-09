

def obterLimite():

    salario = float(input("Digite seu salario: "))
    idade = int(input("Digite sua idade: "))
    limite = salario/idade
    return limite, idade, salario


limite = obterLimite()
print(limite)
