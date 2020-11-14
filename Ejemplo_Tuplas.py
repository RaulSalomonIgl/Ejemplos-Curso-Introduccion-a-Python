'''
Crea una tupla que almacene los valores numericos.
Solicita al usuario que ingrese un valor numerico y mostrar en pantalla, cuantas veces se repite
este valor dentro de la tupla
'''
##Se crea una tupla utilizando () con valores especificos no mutables
Numeros = (5,4,3,2,1,6,45,3,6,6,6,6,6)

##Se declara una variable y solicitara ingresar un dato numerico de tipo entero
Numero = int(input("Dame un numero: "))

##Declaramos una variable inicializada en 0, tendra una función de contador
Contador = 0
##Recorremos la tupla Numeros y el valor en turno se almacena dentro de la variable iterable
for iterable in Numeros:
    if Numero == iterable:
        Contador += 1
 
print ("Hay ",Contador," repeticiones")