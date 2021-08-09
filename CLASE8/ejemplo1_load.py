file = open('discharge_s_6893.txt')
#forma1
data = file.read()   #leer por caracteres
print(data)     

#forma2

for i in range (20):
    print(file.readline()) #leer por lineas

alldata = file.readlines()
print(alldata)   #lee las lineas en forma de lista