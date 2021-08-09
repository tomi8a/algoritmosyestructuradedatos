import csv 
#forma 1
file = open('Municipality_Area.csv',encoding='UTF-8')
lines = csv.reader(file,delimiter=',')
lines = list(lines)
print(lines[3][1])

lines = csv.DictReader(file,delimiter=',')
for aux in lines:
    print(aux)
    print(aux['Municipio'])
