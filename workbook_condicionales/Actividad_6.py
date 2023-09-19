
#uso de for e if para crear una lista y separar elementos de la lista
garaje = []
for a in range(0,5):
    carro = str(input(f"ingrese la marca de carro #{a+1}: "))
    garaje.append(carro) 

print("busca una palabra que inicie con la letra que quieras")
letra=str(input(f"ingrese una letra: "))
for palabra in garaje:
    if palabra[0].lower() == letra:
        print (palabra)


