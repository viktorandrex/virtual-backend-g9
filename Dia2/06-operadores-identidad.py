# is => es
# is not => no es
frutas = ['carambola', 'guayaba', 'higo', 'melocoton']
fruta = 'carambola'

# para poder ver en que posicion de la memeoris esta siendo ubicada una variable se usa el metodo id()
print(id(frutas))
print(id(fruta))
print(fruta is frutas)
# el 'is' e 'is not' se usa mas que todo para validad si las variables a comparar estan apuntando a la misma direccion de memoria o no

# las variables que son colecciones de datos como listas, tuplas y diccionarios son variables mutables
# las otras variables (int, str, float) son variables inmutables
frutas2 = frutas
frutas2.append('fresa')
print(id(frutas2))
print(frutas)
print(frutas2 is frutas)
# Tener cuidado porque cuando ocupan el mismo espacion de memoria y se modifica una en caso de frutas2, se modifican las 2 variables, por lo tanto la comparacion es true

# las dos varianles NO COMPARTEN la misma ubicacion de memoria
print(fruta is not frutas)

# variablkes mutables e inmutables
# para hacer la copia de la lista sin que se ubique en la misma posicion de memoria hacemos uso del metodo copy (propio de las listas)

# Ej. de esta forma no se ubican en la misma posicion de momoria
frutas_variadas = frutas.copy()
print(id(frutas_variadas))
print(id(frutas))
print(frutas_variadas is frutas)


