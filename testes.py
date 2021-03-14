from datetime import datetime


curr = datetime.now()
ano = datetime.strftime(curr, "%Y")
print(ano)
