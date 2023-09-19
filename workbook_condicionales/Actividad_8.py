#uso de for para crear una tabla de multiplicar
numero = int(input("ingrese el numero del cual desea visualizar la tabla de multiplicar: "))
for i in range(0,10):
    multiplicacion = numero * i
    print (f"{numero} x {i} = {multiplicacion}")