import csv
file = open('Municipality_Area_mod.csv',encoding='UTF-8')
lines = csv.DictReader(file,delimiter = ',')

diccmun = {}
for i in lines :
    mun = i['Municipio']
    area = i['Area (km2)']
    area = int(area)
    if area>2000:
        area = 'SI'
    else:
        area ='NO'
    diccmun[mun]= area
print(diccmun)

