# escriba un código que reorganice las letras de una palabra
# empezando por las minusculas y continuando por las 
# mayúsculas.
# ejemplo: AlGoritMos queadría loritosAGM
from curses.ascii import isupper

from sympy import true


x = input('ingrese la palabra que quiere organizar: ')
arrMin = []
arrMax = []
for i in x:
    if i.isupper():
        arrMax.append(i)
    else:
        arrMin.append(i)

out = arrMin + arrMax
print (out)            