
#introduccion
print("En un oscuro y misterioso sótano, la vida de una mujer cuelga de un hilo. Ha sido secuestrada y encerrada en contra de su voluntad. Con sus habilidades y determinación como únicas aliadas, deberás asumir el papel del protagonista y adentrarte en un mundo lleno de peligros y enigmas para rescatarla antes de que sea demasiado tarde. Cada decisión que tomes será crucial, y el tiempo apremia. ¿Tienes lo que se necesita para salvarla y desentrañar el misterio detrás de su secuestro?")
print(input("Presiona ENTER para continuar"))
#perdir el nombre al usuario
nombre=str(input("Antes de empezar ¿como es tu nombre? "))
#inicio del juego nivel 1 del diagrama
print(f"Hola {nombre} acabas de despertar despues de ser drogada con un quimico desoconocido pero  estas amarrada y amordazada a una silla")
print(input("Presiona ENTER para continuar"))

desicionA = int(input("Tienes dos opciones:\n opcion 1: gritar por ayuda\n opcion 2: desatarte\n Seleciona una opción 1 o 2: "))

if desicionA == 1 :
    print(f"Silencio {nombre}, depronto te escucha el secuestrador. Mira arriba hay una escotilla con unos cables sueltos")
    print(input("Presiona ENTER para continuar"))
    desicionB = int(input(f"{nombre}, ¿que vas a hacer ahora?\n Opcion 1: No subir a la escotilla\n Opcion 2: Subir a la escotilla \n Seleciona una opción 1 o 2: "))
    if desicionB == 1 :
        input ("Si viste los cables al rededor de la escotilla, deben tener corriente. mira ahi hay una puerta, coge esa silla y tumba la puerta.\n presiona ENTER para continuar")
      
        desicionC = int(input(f"Muy bien {nombre}! lograste abir la puerta, ahora hay 3 pasillos\n ¿por donde vas a continuar? :\n 1. Pasillo iquierdo\n 2. Pasillo del centro\n 3. Pasillo derecho \nSelecciona 1 opcion: "))
        while True:
            if desicionC == 2:
            print("Genial otras 2 puertas. Piensa muy bien tu elección ya que una de las dos es la salida")
        
            elif desicionC == 1:
                print ("La puerta esta cerrada selecciona otra opción")
                       
            else:
                print("Era una trampa este pasillo te lleva de nuevo al cuarto del inicio. Pero ahora esta el secuestrador y te mata.")


    
    else:
        print("Te has electrocutado con los cables, lo siento HAS MUERTO :C")   
  
#    if desicion_2 == 2:
#        print("Al intentar desatarte te dislocaste el pulgar de la mano derecha, pero finalmente lograste desatarte")
#        print(f"Muy bien {nombre}, tienes que salir de aqui con vida asi que continuemos")
#        print(input("Presiona ENTER para continuar"))
    
#    desicion_2 = int(input(f"{nombre} nuevamente tienes"))

