file = open('Medicamentos_YBVUPY.txt')
lista = file.read().split(',')
registros = len(lista)
print(f'la cantidad de registros son {registros}')