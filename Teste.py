import pandas as pd


df_index = ["Cargo", "Salario"]
Cargo = "Analista Contábil"

df2 = pd.DataFrame(
    {
        "Dados": (str(Cargo),)

    }, index=df_index
)
df2.loc["Salario", "Dados"] = "NEW"


print(df2)
