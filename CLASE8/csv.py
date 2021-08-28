import pandas as pd
import csv 
file = open('Municipality_Area.csv',encoding='UTF-8')
lines = csv.DictReader(file,delimiter = ',')
diccareas = {}

for aux in lines:
    mun = aux['Municipio']
    area = aux['Area (km2)']
    diccareas[mun]= area

busquedamun = input('ingrese el nombre del municipio')
print(diccareas[busquedamun])

