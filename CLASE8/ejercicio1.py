#imprima en pantalla la fecha de nacimiento del paciente
# debe funcionar para los tres archcivos 

file = open('discharge_s_14237.txt')
alldata = file.readlines()
substring = alldata[6]
pos1= substring.index('[')
pos2= substring.index(']')
print(alldata[6][pos1+3:pos2-2])


