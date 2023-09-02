#punto 1 Crear listado de materias
asignaturas = ['introduccion',
'lógica',
'metodologías',
'base de datos',
'móviles 1',
'web 1',
'nuevas tecnologías',
'web 2',
'móviles 2']
print(asignaturas)

#punto 2 rdenar la lista, se imprime de la Z a la A
asignaturas.reverse()
print(asignaturas)

#punto 3
#	Agregar “Diseño” , en la posición 4
asignaturas.insert(3,'Diseño')
print(asignaturas)

# Agregar “Teoría del color” al final
asignaturas.append('Toería del color')
print(asignaturas)

# punto 4
# Imprimir todo en mayúscula. Se realiza mapeo de lista a string, dado que una a una lista no se le puede aplicar el metodo upper. 
palabra_mayu = list(map(str.upper,asignaturas))
print(palabra_mayu)


