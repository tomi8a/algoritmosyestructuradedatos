from statistics import mean
import pandas as pd
df = pd.read_csv('UCI_XYCOZROR.csv')
edad = df[ 'C7'].tolist()
edadrango = []
for i in edad:
    if i>=45 and i<=55:
        edadrango.append(i)
prom = sum(edadrango)/len(edadrango)
print(prom)

