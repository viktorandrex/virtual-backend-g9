mes = "agosto"
print("el mes es:",mes)

dia = 16
print("el dia", dia, "del mes de", mes)
#internamente python convierte todo el conjunto de variables a string

alumnos = 23
grupo = 9
#grupo = 0,9 imprime (0, 9) se llama dupla no array
#si es numerica mayor a 0, no puede comenzar con 0

print("los alumnos son {} y son del grupo {} y todos estan atentos".format(alumnos, grupo))

#en este modo poniendo la posicion del elelemtno en el format porque alli es un array
print("los alumnos son {1} y son del grupo {0} y todos estan atentos".format(grupo, alumnos))

#lo que esta dentro de las llaves es codigo python
print(f"los alumnos son {1+1}")
print(f"los alumnos son {alumnos}")
print(f"los alumnos son {alumnos} y el grupo es {9}")