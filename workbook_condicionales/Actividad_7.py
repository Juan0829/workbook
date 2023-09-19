#uso de for para sumar dos listas 
pesos_1=[]
pesos_2=[]
resultados=[]
print("Este programa sirve para sumar los pesos recolectados de un supermercado en dos dias diferentes del mismo cliente comprando las mismas frutas")
print("Dia 1")
for kg1 in range(0,5):
    peso_1 = int(input(f"Ingrese el resultado #{kg1+1} en kg: "))
    pesos_1.append(peso_1)
print(f"los pesos almacenados son: {pesos_1}")

print("Dia 2")
for kg2 in range(0,5):
    peso_2 = int(input(f"Ingrese el resultado #{kg2+1} en kg: "))
    pesos_2.append(peso_2)
print(f"los pesos almacenados son: {pesos_2}")

print("la suma de los pesos recolectados son los siguientes")
for kg3 in range(len(pesos_1)):
    suma = pesos_1[kg3] + pesos_2[kg3]
    resultados.append(suma)
print (resultados)