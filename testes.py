import pandas as pd

salario = 1
carro = 2

data = [salario, carro],
df = pd.DataFrame(data, columns=['salario', 'carros'])
df.reset_index(index=False)
print(df)
