# es el punto 6 del taller normal 
import pandas as pd
df = pd.read_csv('Municipality_Area_mod.csv')
inDep = input('ingrese el departamento')
inArea = int(input('indique el valor minimo de area deseado'))

dep = df[df['Departamento']== inDep]
munArea = dep[dep['Area (km2)']> inArea]
mun = munArea['Municipio']
print(f'estos son los municipios que tienen un area mayor {inArea} en {inDep}')
print(mun)