#Ejercicio de if compuesto

#Hacer un programa que pida al usuario 2 valores
#Preguntarle al usuario que quiere hacer con ellas
#Sumarlas, Restarlas o multiplicarla

##Declaramos las variables y solicitamos datos numericos enteros
Valor1 = int(input("Ingresa el valor 1: "))
Valor2 = int(input("Ingresa el valor 2: "))

print("")
print("Selecciona una opción")
print("")
print("1.- Sumar Variables")
print("2.- Restar Variables")
print("3.- Multiplicar Variables")
print("")
Opcion = int(input(": "))

##Evaluamos una condición
if Opcion == 1:
    Resultado = Valor1 + Valor2
    print(Resultado)

##Evaluamos una segunda condición si la anterior no se cumple
elif Opcion == 2:
    Resultado = Valor1 - Valor2
    print(Resultado)

elif Opcion == 3:
    Resultado = Valor1 * Valor2
    print(Resultado)

##Resultado si todas las condiciones anteriores son negativas
else:
    print("Valor ingresado no valido")
    
