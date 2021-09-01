
# 1. Imprima las primeras 5 posiciones pares de la siguiente variable (es decir, la 0,2,4,6,8)
from textwrap import indent


var = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
print(var[0:10:2])

import numpy as np
# 2. Escriba un código que imprima: [100, 90, 80, 70] (observe el orden!)
var = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

print(var[-3:-7:-1])




# 3. Escriba un código que guarde en var2 lo que hay en var pero invertido.
#    Es decir, la última posición ahora es la primera y así sucesivamente.
var = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
var2 = var[::-1]
print(var2)
# 4. Genere la variable ind con un np.arange que empiece en 0,
#    llegue hasta el tamaño de var y tenga incrementos de a 2. Imprima var en ind.
import numpy as np
var = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
ind = np.arange(0, len(var), 2)
print(var[ind])

# 5. Genere un ndarray que empiece en 5, termine en 29, con incrementos de a 3.
#    Imprima la primera posición, la última y la del medio, es ese orden. 

array = np.arange(5,30,3)
print(array[0],array[-1],array[round(len(array)/2)])
