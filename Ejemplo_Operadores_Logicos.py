##Muestra una instrucción al usuario
print("Dame los lados de tu triangulo y te dire cual es su tipo")

##Declaraciones de variables y solicitud de insercción de datos
lado1 = int(input("Dame el primer lado: "))
lado2 = int(input("Dame el segundo lado: "))
lado3 = int(input("Ahora el tercero: "))

##Evaluacion de condiciones utilizando operadores logicos
if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("Tu triangulo es equilátero")
else:
    if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Tu triangulo es isósceles")

    else:
        if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
            print("Tu triangulo es escaleno")