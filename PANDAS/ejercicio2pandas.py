import pandas as pd
df = pd.read_csv('Municipality_Area.csv')
busquedamun = input('ingrese el nombre del municipio')
print(df[df.Municipio==busquedamun]['Area(km2)'])


