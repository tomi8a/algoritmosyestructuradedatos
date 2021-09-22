# escriba un código que reciba un string como input y cambie por $
# todas las ocurrencias de su primera letra, excepto ella misma
# que no debe cambiar.
# primero pruebe que funcione con todas minusculas,
# ejemplo: araña quedaría ar$ñ$
# luego pruebe que funcione con la primera en mayúscula,
# ejemplo: Araña quedaría Ar$ñ$

from dataclasses import replace


x = input('ingrese la palabra que desea modificar:  ')
firschar = x[0]
charaux = firschar.lower()
word = x.replace(charaux,'$')
word = firschar+ word[1:]
print(word)