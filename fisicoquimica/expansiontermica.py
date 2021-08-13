from sympy import *
import numpy as np
import matplotlib.pyplot as plt
c = 1
n = 1
Ti = 293.15
Vi = 1
R = 8.314
V = np.arange(1,500)

trabajo1 = R*Ti*n*np.log(V) - R*Ti*n*np.log(Vi)
trabajo2 = -R*V*c*n + R*Vi*c*n + R*n*(Ti + Vi*c)*np.log(V) - R*n*(Ti + Vi*c)*np.log(Vi)

plt.plot(V,trabajo1,label ='trabajo en expansion isotermica reversible')
plt.plot(V,trabajo2,label='trabajo en expansion no termica reversible')
plt.xlabel('volumen en metro cubito')                                   
plt.ylabel('trabajo en joules')                                              
plt.title('expansiontermica de los gases')     
plt.legend()    
plt.savefig('expansion termica de los gases')                                                
plt.show()  

