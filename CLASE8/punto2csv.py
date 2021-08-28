import csv 
file = open('Municipality_Area.csv',encoding='UTF-8')
lines = csv.DictReader(file,delimiter = ',')
diccdep = {}
listamun = []
i = 0
for aux in lines:
    if i == 0:
        depante = aux['Departamento']
    dep = aux['Departamento']
    mun = aux['Municipio']
    i = i + 1
    if dep == depante:
        listamun.append(mun)
    else:
        diccdep[depante]= listamun
        i = 0
        listamun = []






