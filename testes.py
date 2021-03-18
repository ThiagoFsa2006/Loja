import pandas as pd

cargo = "Analista"
salario = 3000
Ano_de_nascimento = 1992
idade = 29
limite_de_credito = 150

d = {"Cargo": cargo, "salario": salario, "Ano de nascimento":
     Ano_de_nascimento, "Idade": idade, "Limite de credito": limite_de_credito}

df_index = ["Cargo", "Salario", "Ano de nascimento",
            "Idade", "Limite de crédito"]

data = {"Dados": [cargo, salario, Ano_de_nascimento, idade, limite_de_credito]
        }
df = pd.DataFrame(data,  columns=["Dados"], index=df_index)

d = pd.Series(d)
print(df)

print(d)
