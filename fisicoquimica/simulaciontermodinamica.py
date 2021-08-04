#tomas ochoa y geronimo buitrago fisico quimica
import numpy as np
import math
import matplotlib.pyplot as plt
m_N2 = 4.65 * 10 **-26
k_B = 1.38e-23 
T = 350
T1= 292.15
T2= 250
v = np.arange(10, 3000, 20)
n_N2 = 4 * math.pi * (m_N2 / (2 * math.pi * k_B * T)) ** (3 / 2) * (v**2) * np.exp(-m_N2 * v**2 / (2 * k_B * T))
n1_N2 = 4 * math.pi * (m_N2 / (2 * math.pi * k_B * T1)) ** (3 / 2) * (v**2) * np.exp(-m_N2 * v**2 / (2 * k_B * T1))
n2_N2 = 4 * math.pi * (m_N2 / (2 * math.pi * k_B * T2)) ** (3 / 2) * (v**2) * np.exp(-m_N2 * v**2 / (2 * k_B * T2))
plt.plot(v, n_N2, label = "Gas N2 a 350 k")
plt.plot(v, n1_N2, label = "Gas N2 a 292.15 k")
plt.plot(v, n2_N2, label = "Gas N2 a 250 k")
plt.xlabel('Velocidad (m/s)')                                   
plt.ylabel('n(v)')                                              
plt.title('Distribución de Velocidad de Maxwell-Boltzmann del N2 a diferentes temperaturas')     
plt.legend()    
plt.savefig('Distribución de Velocidad de Maxwell-Boltzmann del N2 a diferentes temperaturas')                                                
plt.show()  