import pandas as pd
df = pd.read_csv('UCI_XYCOZROR.csv')
varsobrevivvio = 0
varfallecio = 1
sobrevivio = df[df['C9']==varsobrevivvio]
porcentaje= len(sobrevivio)
print(f'el {porcentaje}% de personas sobrevivieron')