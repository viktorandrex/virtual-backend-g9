numero1 = 10
numero2 = 80

persona1 = "Eduardo"
persona2 = "Ricardo"

#SUMA--------------
#Nota: si las dos o mas variables son numericas entonces se realizara la suma, si por el contrario las variables son string(caracteres) se CONCATENARAN (se juntaran)
print(numero1 + numero2)
print(persona1 + persona2)
#print(numero1 + persona2) #Error no se soportan int con str
numero1_string = str(numero1)
print(numero1_string + persona2) #Error no se soportan int con str

#RESTA--------------
print(numero1 - numero2)
#print(persona1 - persona2)
#No se puede usar la resta en variables que no sean numericas

#MULTIPLICACION--------------
print(numero1 * numero2)
#print(persona1 * persona2)
print(persona1 * 2)
#En este caso persona1 se repite 2 veces

#Que salga la multiplicacion de 10 y 80 es : 800
print(f"la multiplicacion de {numero1} y {numero2} es: {numero1 * numero2}")
print("la multiplicacion de {} y {} es: {}".format(numero1, numero2, numero1*numero2))
print("la multiplicacion de {0} y {1} es: {2}".format(numero1, numero2, numero1*numero2))

#DIVISION--------------
#Toda division aun así sea entera siempre sera flotante (tiene una parte entera y una parte decimal)
print(numero2 / numero1)
print(numero1 / numero2)

#MODULO--------------
print(numero2 % numero1)
print(numero1 % numero2)

#COCIENTE
print(numero2 // numero1)
print(numero1 // numero2)
#cociente es el divisor