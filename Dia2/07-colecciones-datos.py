# los array en Python se les conoce como "listas"

# List => listas
# ordenadas, y modificables
colores = ['morado', 'azul', 'rosado', 'amarillo']
mezclada =['otoño', 14, False, 15.2, [1, 2, 3]]

# imprimir la primera posicion
print(colores[0])

# Este ejemplo en JS no da error, 
# en Python si la posicion no existe lanzará un error que indicara (no definido)
# print(colores[10]) 

# Al usar valores negativos en las posiciones de la lista, se 'invertira' y podremos recorrer dicha lista
# -1 comienza desde el final => amarillo
# -2 es el siguiente => rosado
# nota: esto no se puede hacer en JS
print(colores[-2])
# trae de la posicion numero 1 hasta la posicion menor de 2, osea solo 1
print (colores[1:2])
# desde la posicion 1 hasta la posicion menor que 3, osea 1 y 2
print (colores[1:3])
# trae de la posicion 1 hasta el final
print (colores[1:])
# trae hasta la posicion menor que 2
print (colores[:2])

# para copiar El CONTENIDO de la lista mas no su ubicacion de memoria
colores_2 = colores[:]
print(id(colores_2))
print(id(colores))


print (colores[0:-1])

# metodo para agregar un elemento a una lista
colores.append('naranja')
print(colores)

# metodo para eliminar un valor
# 1. solamente si existe lo eliminara, sino lanzara un error
colores.remove('azul')
print(colores)
#Aqui da error porque no puede eliminarse 2 veces
#colores.remove('azul')
#print(colores)

# 2. si queremos eliminarlo y ADEMAS guardar el valor eliminado en una variable
color_eliminado = colores.pop(0)
print(colores)
print(color_eliminado)

# 3. el metodo para eliminar el valor
# este metodo tambien sirve para eliminar variables
#nombre = "eduardo"
#del nombre
#print(nombre)

# eliminar de la lista solo la posicion 0
del colores[0]
print(colores)

# len: longitud de la lista
print(len(colores))

# TUPLAS
# la tupla a diferencia de la lista es una coleccion de datos ordenada PERO que una vez creada no se puede editar

# Aqui se guarda contraseñas, igv, etc
# se puede eliminar toda la tupla pero no un elemento

notas = (10, 15, 20, 9, 17,10)
#notas.append(10) #error: no soporta agregar
#notas[0] = 20 # error: no soporta asignacion
#del notas[0] # error: no puede eliminarse

print(notas[0])
print(len(notas))
print (notas.count(10)) #cuantas veces existe 10

# DICCIONARIOS (JSON)
# coleccion de datos ordenada PERO no por indices ya que se maneja un ordenamiento segun su clave-valor, se puede modificar
persona = {
    'nombre': 'Eduardo', #Cuando hay doble nombre el primero se chanca
    'nombre': 'Victor',
    'apellido': 'Ccorimanya',
    'correo': 'correo@correo.com',
    'edad': 28,
    'donacion_organos': True,
    'hobbies': [
        {
            'nombre': 'Volar Drones',
            'conocimiento': 'Avanzado'
        },
        {
            'nombre': 'Montar Bici',
            'conocimiento': 'Intermedio'
        }
    ]
}

persona['edad'] = 35
persona['nacionalidad'] = 'peruano'

print(persona['edad'])
print(persona['nombre'])
#print(persona.nombre) #solo se puede asi en JS
print(persona)

#imprimir el primer hobby de la persona
# Volar drones
print(persona['hobbies'][0]['nombre'])

 # DICTIONARY keys: devuelve un arreglo
 # Extraer las llaves
print(persona.keys())
# Extraer los valores
print(persona.values())
# Limpia todo
persona.clear()
print(persona)


