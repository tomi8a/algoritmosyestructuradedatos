import csv 
def Departamento(nombre_Archivo):
    file = open(nombre_Archivo,encoding='UTF-8')
    lines = csv.DictReader(file,delimiter = ',')
    diccdep = {}
    listamun = []
    i = 0
    for aux in lines:
        if i == 0:
            depante = aux['Departamento']
        dep = aux['Departamento']
        mun = aux['Municipio']
        
        i = i+1
        if dep == depante:
            listamun.append(mun)
            mun1 = len(listamun)
        else:
            diccdep[depante]=mun1
            i = 0
            listamun = []
            listamun.append(mun)
    depbusqueda = input('ingrese departamento deseado :')
    print(diccdep[depbusqueda])

Departamento('Municipality_Area_mod.csv')