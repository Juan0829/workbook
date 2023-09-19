
#introduccion
print("En un oscuro y misterioso sótano, la vida de una mujer cuelga de un hilo. Ha sido secuestrada y encerrada en contra de su voluntad. Con sus habilidades y determinación como únicas aliadas, deberás asumir el papel del protagonista y adentrarte en un mundo lleno de peligros y enigmas para rescatarla antes de que sea demasiado tarde. Cada decisión que tomes será crucial, y el tiempo apremia. ¿Tienes lo que se necesita para salvarla y desentrañar el misterio detrás de su secuestro?")
print(input("Presiona ENTER para continuar"))
#perdir el nombre al usuario
nombre=str(input("Antes de empezar ¿como es tu nombre? "))
#inicio del juego nivel 1 del diagrama
print(f"Hola {nombre} acabas de despertar despues de ser drogada con un quimico desoconocido pero  estas amarrada y amordazada a una silla")
print(input("Presiona ENTER para continuar"))

desicion1 = int(input("Tienes dos opciones:\n opcion 1: gritar por ayuda\n opcion 2: desatarte\n Seleciona una opción 1 o 2: "))
#toma de desicion desatarse o gritar
if desicion1 == 1 :
    print(f"Silencio {nombre}, depronto te escucha el secuestrador. Desatate y mira arriba hay una escotilla con unos cables sueltos")
    print(input("Presiona ENTER para continuar"))
    desicionB = int(input(f"{nombre}, ¿que vas a hacer ahora?\n Opcion 1: No subir a la escotilla\n Opcion 2: Subir a la escotilla \n Seleciona una opción 1 o 2: "))
    if desicionB == 1 :
        input ("Si viste los cables al rededor de la escotilla, deben tener corriente. mira ahi hay una puerta, coge esa silla y tumba la puerta.\n presiona ENTER para continuar")
      
        
        while True:
            desicionC = int(input(f"Muy bien {nombre}! lograste abir la puerta, ahora hay 3 pasillos\n ¿por donde vas a continuar? :\n 1. Pasillo iquierdo\n 2. Pasillo del centro\n 3. Pasillo derecho \nSelecciona 1 opcion: "))
            if desicionC == 2:
                print("Genial otras 2 puertas. Piensa muy bien tu elección ya que una de las dos es la salida")
                desicionD = int(input(f"¿Cual es tu elección {nombre}?\n 1. Puerta 1\n 2. Puerta 2\n"))
                if desicionD == 1:
                    print (f"GENIAL {nombre}, has salido con vida.\n FIN DEL JUEGO")
                    break  
                else:
                    print ("Esta muy oscuro no ves nada, entras y te tropiezas caes y te rompes el cuello.\n PERDISTE! :c")
                    break
            elif desicionC == 1:
                input ("La puerta esta cerrada selecciona otra opción\n Presiona ENTER para continuar.")
                       
            else:
                print("Era una trampa este pasillo te lleva de nuevo al cuarto del inicio. Pero ahora esta el secuestrador y te mata.\n PERDISTE :c")
                break

    
    else:
        print("Te has electrocutado con los cables, lo siento HAS MUERTO :C")   
  
else:
    print("Al intentar desatarte te dislocaste el pulgar de la mano derecha, pero finalmente lograste desatarte")
    print(f"Muy bien {nombre}, tienes que salir de aqui con vida asi que continuemos")
    print(input("Presiona ENTER para continuar"))
    
    desicion2 = int(input(f"{nombre}, no tienes mucho tiempo ¿que vas a hacer ahora?\n 1. grita pidiendo ayuda \n 2. Busca una salida \n Selecciona una opción: "))
    if desicion2 == 1:
        input (f"Grita {nombre} !! Grita muy duro pide ayuda!!. Si escuchas?, parece que hay alguien cerca.\n Presiona ENTER para continuar")
        
        desicionE = int(input(f"Parece que te escucho alguien, ¿que haces {nombre}, silencio para que no te escuchen o gritas mas duro?\n 1. Silencio\n 2. Grita mas duro\n Selecciona una opción: "))
        if desicionE == 1:
            print ("Era el secuestrador pero te alcanzo a escuchar. Te han matado\n FIN DEL JUEGO")
           
        else:
            print ("Era la policia. Te estaban buscando!! te has salvado\n FIN DEL JUEGO")

    else:
        codigo_vacio =[]
        while True:
            print(f"Hay una puerta y una ventana. Al lado de la puerta hay una pantalla para poner una clave y la ventana tiene un vidrio con unos cables al rededor\n Por donde quieres salir: \n 1. Ventana\n 2. Puerta")       
            desicionF = int(input(f"{nombre} seleciona una opcion: "))
        
            
        
            if desicionF == 2:
                print(f"La pantalla pide una clave de 4 digitos para poder abrirla la puerta. Para saber el codigo debes resolver el siguiente acertijo: ")
                print(f"Soy un número de 3 dígitos. La suma de mis dígitos es 18. ")
                print(f"Mi primer dígito es 3 menos que mi segundo dígito, el tercer dígito es igual a la suma de mis dos primeros dígitos. ¿Cuál es mi número?")
                input("Presione ENTER para iniciar: ")
                for digito in range (0,3):
                    valor = int(input(f"ingrese el digito #{digito+1}: "))
                    codigo_vacio.append(valor)
            
                codigo_correcto = [3,6,9]
            
                if codigo_vacio != codigo_correcto:
                    input ("Contraseña incorrecta, sono una alarma. Lo siento te han descubierto.\n FIN DEL JUEGO")
                else:
                    print("Contraseña correcta. Felicidades ERES LIBRE CORRE!!!")
                    break
                    
            else:
                print("Oh no te han descubierto y te han disparado\n FIN DEL JUEGO ")
                break