
#introduccion
print("En un oscuro y misterioso sótano, la vida de una mujer cuelga de un hilo. Ha sido secuestrada y encerrada en contra de su voluntad. Con sus habilidades y determinación como únicas aliadas, deberás asumir el papel del protagonista y adentrarte en un mundo lleno de peligros y enigmas para rescatarla antes de que sea demasiado tarde. Cada decisión que tomes será crucial, y el tiempo apremia. ¿Tienes lo que se necesita para salvarla y desentrañar el misterio detrás de su secuestro?")
print(input("Presiona ENTER para continuar"))
#perdir el nombre al usuario
nombre=str(input("Antes de empezar ¿como es tu nombre? "))
#inicio del juego nivel 1 del diagrama
print(f"Hola {nombre} acabas de despertar despues de ser drogada con un quimico desoconocido pero  estas amarrada y amordazada a una silla")
print(input("Presiona ENTER para continuar"))

decisicion_1 = int(input("Tienes dos opciones:\n opcion 1: desatarte\n opcion 2: gritar por ayuda\n Seleciona una opción 1 o 2: "))

while decisicion_1 == 1 :
    print("Al intentar desatarte te dislocaste el pulgar de la mano derecha, pero finalmente lograste desatarte")
else:    
    print(2)