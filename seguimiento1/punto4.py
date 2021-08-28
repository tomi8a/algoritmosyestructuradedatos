import csv
def Departamento(nombreArchivo): 
    file = open(nombreArchivo,encoding='UTF-8')
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
    depsearch = input ('ingrese el departamento que desea saber los municipios')
    print(diccdep[depsearch])

Departamento('Municipality_Area_mod.csv')
