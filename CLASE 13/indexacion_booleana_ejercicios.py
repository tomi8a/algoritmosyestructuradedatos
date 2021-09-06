import numpy as np
from pandas import Int32Dtype

# 1. ¿Cuantas personas tienen 18 años?
edades = np.array([18, 18, 17, 18, 20, 21, 23, 20, 18, 18, 19, 21])

ind = edades == 18
out = edades[ind]
print(f'las personas que tienen 18 años son : {len(out)}')
# 2. ¿Cuantas personas tienen 20 o más años?
ind1 = edades>= 20
out1 = edades[ind1]
print(f'las personas mayores a 20 son : {len(out1)}')

# 3. ¿Cuantas personas tienen entre 17 y 19 años?
ind2 = edades >= 17 
Ind3 = edades <= 19
indjun = ind2 & Ind3
out2 = edades[indjun]
print ('las personas entre 17 y 19 son :',len(out2))
# 4. ¿Cuál es la edad promedio de los menores de 23 años?
ind4 = edades< 23
out3 = edades[ind4]
indprom = round(np.mean(out3),2)
print ('el promedio de las edades menores a 23 es :',indprom)

# 5. A los mayores de 22 años asignarles edad igual a cero.
ind5 = edades>22
ind5 = ind5*0
out4 = edades[ind5]



# 6. A los que tengan 18 o 20 años asignarles una edad de 100.
edades = np.array([18, 18, 17, 18, 20, 21, 23, 20, 18, 18, 19, 21])
ind6 = edades == 18
ind7 = edades== 20
ind6 = ind6 == 100
ind7 = ind7 == 100
indjun2 = ind6 | ind7
out = edades[indjun2]

# 7. Genere un print que haga la función de tabla de frecuencias así:
#    cantidad 17 años: 1
#    cantidad 18 años: 5
#    cantidad 19 años: 1
#    cantidad 20 años: 2
#    cantidad 21 años: 2
#    cantidad 22 años: 0
#    cantidad 23 años: 1
edades = np.array([18, 18, 17, 18, 20, 21, 23, 20, 18, 18, 19, 21])


 