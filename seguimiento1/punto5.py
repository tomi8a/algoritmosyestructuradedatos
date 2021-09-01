import pandas as pd
df = pd.read_csv('Municipality_Area_mod.csv')
busquedadep = input('ingrese el nombre del departamento :')
aux = df[df['Departamento']==busquedadep]
print(aux['Muncipio'].values)
