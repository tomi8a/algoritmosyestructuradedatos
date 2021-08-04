lista = ['tomas','camilo','juan fernando caicedo','elmillor','ibai','juan fernando caicedo']
n = 0
x = input('ingrese nombre: ')
x = x.capitalize()
for i in lista:
    if i.capitalize == x:
        n = n + 1
print (f"hay {n} nombres como juan fernando caicedo")