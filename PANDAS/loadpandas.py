import pandas as pd
df = pd.read_csv('Municipality_Area.csv')
# print(df.head(5))
# print(df.columns) #ver columnas
# print(df['Municipio']) # ver una columna

#slicing
# print(df[0:3])
# print(df.iloc[0:3,0,2])# escger columnas

#con condicion
# print(df[df.Departamento == 'Antioquia'].head(5))# imprime todos que tengan el dpto antioquia
print(df[df['Area(km)']])