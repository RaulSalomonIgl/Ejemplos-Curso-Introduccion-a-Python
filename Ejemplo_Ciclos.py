##Declara una variable y pide al usuario su valor
numero = int(input("Ingresa un número: "))

Mensaje = "Hola amigos de Python"

##Sentencia For
print("Sentencia For")
for posicion in range(0,10):
    print(numero,"X",posicion+1,"=",numero*(posicion+1))

##Recorrer objetos iterables con for
print("Mensaje:",Mensaje)
for letra in Mensaje:
    print(letra)

##Sentencia While
print()
Contador = 1
print("Sentencia While")
while (Contador <= 10):
    print(numero,"X",Contador,"=",numero*(Contador))
    Contador += 1

##Creacion de Menu
Opcion = 1
while (Opcion != 0):
    print("Menu")
    print("0.- Salir")
    print("1.- Siguiente")
    Opcion = int(input(": "))
    