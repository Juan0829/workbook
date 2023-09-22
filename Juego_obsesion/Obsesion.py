#funcion enter para continuar
def continuar():
    return input("PRESIONA ENTER PARA CONTINUAR")
#clase elementos de ayuda
class Ayudas:
    def __init__(self, objeto1, objeto2, objeto3, objeto4):
        self.objeto1 = objeto1
        self.objeto2 = objeto2
        self.objeto3 = objeto3
        self.objeto4 = objeto4
    def make_acctions(self):
        pass
    #funcion uso de objetos
    correcta:()
    def uso_ayudas(self):
        
        print (f"aqui puedes usar algun objeto:\n1. {objetos.objeto1}\n2. {objetos.objeto2}\n3. {objetos.objeto3}\n4. {objetos.objeto4}")
        while True:
            eleccion =int( input ("¿cual deseas usar?"))

            if eleccion != correcta:
                print (f"Lo siento este objeto no te va a servir en esta situación\n {continuar()}")
            else:
                return f"Bien pensado, aqui puedes usar este objeto\n {continuar()}"
objetos = Ayudas("cuchillo", "llave", "cuerda", "silvato")  
#polimorfismos 
class Acciones:
    def __init__(self, accion):
        self.name = accion
 
class Cuchillo(Acciones):
    def make_acctions(self):
        return "cortando"
class Llave(Acciones):
    def make_acctions(self):
        return "abriendo puerta"
class Cuerda(Acciones):
    def make_acctions(self):
        return "trepando con la cuerda"
class Silvato(Acciones):
    def make_acctions(self):
        return "FIUU!!!"
accion_cuchillo= Cuchillo("cortar")
accion_llave= Llave("abrir")
accion_cuerda= Cuerda("trepar")
accion_silvato= Silvato("pitar")
#introduccion
print("En un oscuro y misterioso sótano, la vida de una mujer cuelga de un hilo. Ha sido secuestrada y encerrada en contra de su voluntad. Con sus habilidades y determinación como únicas aliadas, deberás asumir el papel del protagonista y adentrarte en un mundo lleno de peligros y enigmas para rescatarla antes de que sea demasiado tarde. Cada decisión que tomes será crucial, y el tiempo apremia. ¿Tienes lo que se necesita para salvarla ?")
print(continuar())

#perdir el nombre al usuario
nombre=str(input("Antes de empezar ¿como es tu nombre? "))

#presentacion de las ayudas
print (f"Hola {nombre} lamento mucho que estes en esta situación, aqui hay unos elementos que espero que te sean utiles para poder salir con vida de este desafio\n {continuar()}")
print (f"Los elementos son:\n1. Un {objetos.objeto1}: te servira para cortar objetos no muy rigidos\n2. Una {objetos.objeto2}: alguna puerta debe abrir con esta llave.\n3. Una {objetos.objeto3}: puede servir para trepar.\n4. Un {objetos.objeto4}: Un objeto que puede llamar la atención o ser usado estratégicamente.\n {continuar()}")

#inicio del juego 
print(f"Empecemos {nombre} acabas de despertar despues de ser drogada con un quimico desoconocido pero  estas amarrada y amordazada a una silla")
print(continuar())

#toma de desicion desatarse o gritar
desatarte = int(input("Tienes dos opciones:\n opcion 1: gritar por ayuda\n opcion 2: desatarte\n Seleciona una opción 1 o 2: "))
if desatarte == 1 :
    print(f"Silencio {nombre}, depronto te escucha el secuestrador. Desatate y mira arriba hay una escotilla con unos cables sueltos")
    print(continuar())
    #toma de desicion subir o no a la escotilla
    escotilla = int(input(f"{nombre}, ¿que vas a hacer ahora?\n Opcion 1: No subir a la escotilla\n Opcion 2: Subir a la escotilla \n Seleciona una opción 1 o 2: "))
    if escotilla == 1 :
        print ("Si viste los cables al rededor de la escotilla, deben tener corriente. mira ahi hay una puerta, coge esa silla y tumba la puerta.\n ")
        print(continuar())
      
        #toma de desicion pasillos
        while True:
            pasillo = int(input(f"Muy bien {nombre}! lograste abir la puerta, ahora hay 3 pasillos\n ¿por donde vas a continuar? :\n 1. Pasillo iquierdo\n 2. Pasillo del centro\n 3. Pasillo derecho \nSelecciona 1 opcion: "))
            if pasillo == 2:
                print("Genial ahora hay 2 puertas. Piensa muy bien tu elección ya que una de las dos es la salida")
                #toma de desicion puertas
                puerta = int(input(f"¿Cual es tu elección {nombre}?\n 1. Puerta 1\n 2. Puerta 2\n"))
                
                if puerta == 1:
                    correcta=2
                    print(objetos.uso_ayudas())
                    print(accion_llave.make_acctions())
                    print (f"GENIAL {nombre}, has salido con vida.\n FIN DEL JUEGO")
                    break  
                else:
                    correcta=2
                    print(objetos.uso_ayudas())
                    print(accion_llave.make_acctions())
                    print ("Esta muy oscuro no ves nada, entras y te tropiezas caes y te rompes el cuello.\n PERDISTE! :c")
                    break
            elif pasillo == 1:
                input ("La puerta esta cerrada selecciona otra opción\n Presiona ENTER para continuar.")
                       
            else:
                print("Era una trampa este pasillo te lleva de nuevo al cuarto del inicio. Pero ahora esta el secuestrador y te mata.\n PERDISTE :c")
                break

    
    else:
        correcta=3
        print(objetos.uso_ayudas())
        print(accion_cuerda.make_acctions())
        print("Lograste subir, pero te has electrocutado con los cables, lo siento HAS MUERTO :C")   
  
else:
    correcta=1
    print(objetos.uso_ayudas())
    print(accion_cuchillo.make_acctions())
    print("Genial pudiste desatarte con el cuchillo")
    print(f"Muy bien {nombre}, tienes que salir de aqui con vida asi que continuemos")
    print(input("Presiona ENTER para continuar"))
    
    desatarte = int(input(f"{nombre}, no tienes mucho tiempo ¿que vas a hacer ahora?\n 1. grita pidiendo ayuda \n 2. Busca una salida \n Selecciona una opción: "))
    if desatarte == 1:
        input (f"Grita {nombre} !! Grita muy duro pide ayuda!!. Si escuchas?, parece que hay alguien cerca.\n Presiona ENTER para continuar")
        #toma de desicion gritar mas o hacer silencio
        silencio = int(input(f"Parece que te escucho alguien, ¿que haces {nombre}, silencio para que no te escuchen o gritas mas duro?\n 1. Silencio\n 2. Grita mas duro\n Selecciona una opción: "))
        if silencio == 1:
            print ("Era el secuestrador pero te alcanzo a escuchar. Te han matado\n FIN DEL JUEGO")
           
        else:
            correcta=4
            print(objetos.uso_ayudas())
            print(accion_silvato.make_acctions())
            print ("Era la policia. Te estaban buscando!! te has salvado\n FIN DEL JUEGO")

    else:
        codigo_vacio =[]
        while True:
            print(f"Hay una puerta y una ventana. Al lado de la puerta hay una pantalla para poner una clave y la ventana tiene un vidrio con unos cables al rededor\n Por donde quieres salir: \n 1. Ventana\n 2. Puerta")       
            desicionF = int(input(f"{nombre} seleciona una opcion: "))
       #ciclo clave correcta
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
                    input ("Contraseña incorrecta, vuelve a intentarlo")
                    
                else:
                    print("Contraseña correcta. Abrio la puerta, felicidades ERES LIBRE... CORRE!!!")
                    break
                    
            else:
                print("Oh no te han descubierto y te han disparado\n FIN DEL JUEGO ")
                break

