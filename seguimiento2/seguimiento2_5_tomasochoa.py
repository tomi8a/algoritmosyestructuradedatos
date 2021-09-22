file = open('Medicamentos_YBVUPY.txt')
lista = file.read()
x = lista.count('ramipril')
y = lista.count('Ramipril')
total = x+y

print('el medicamento fue escogido',total,'veces')