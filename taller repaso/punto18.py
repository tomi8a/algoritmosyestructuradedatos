numero1 = float(input("ingresa un numero : "))
numero2 = float(input("ingresa un numero : "))
numero3 = float(input("ingresa un numero : "))

if  numero1 == numero2 and numero2 == numero3:
    suma = (numero1 + numero2 + numero3)*3
    print(f"la suma de los tres numeros aumentada en 3 es {suma}")
else:
    valor = numero1 + numero2 + numero3
    print(f"la suma de los tres numeros es {valor}")