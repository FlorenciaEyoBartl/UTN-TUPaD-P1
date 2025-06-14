# 1 **************************************************************************
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
# Añadimos nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# 2 **************************************************************************
# Continuación del ejercicio anterior, modificamos los precios(valores) de las frutas(keys)
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# 3 **************************************************************************
# Continuación del ejercicio anterior, imprimimos solo las keys del diccionario "precio_fruta"
lista_frutas = list(precios_frutas.keys()) # guardamos el nombre de las keys en una nueva lista "lista_frutas"
print(lista_frutas)

# 4 **************************************************************************
contactos = {} # diccionario para almacenar 5 contactos.

for i in range(5): # Cargar 5 contactos
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ") # pide el nombre a modo de key y aumenta el contador i e 1 cada vez.
    telefono = input(f"Ingrese el teléfono de {nombre}: ") # pide el telefono a modo de valor
    contactos[nombre] = telefono # contacto = diccionario, nombre = key, telefono es el valor guardado en cada key. 

# Consulta un contacto
nombre_consulta = input("Ingrese el nombre a consultar: ")
if nombre_consulta in contactos: # busca la keyen el diccionario
    print(f"El teléfono de {nombre_consulta} es: {contactos[nombre_consulta]}") 
    # si encuentra la key la imprime "{nombre_consulta}" luego imprime el valor de esa key "{contactos[nombre_consulta]}"
    
# si no encuentra la key solicitada imprime "El contacto no existe"
else:
    print("El contacto no existe")

# 5 **************************************************************************
frase = input("Ingrese una frase: ")
palabras = frase.split() 
# split() divide el string en palabras usando los espacios como separadores. crea una lista con esas palabras

# Palabras únicas
palabras_unicas = set(palabras) # Convertimos la lista a un set, que automáticamente elimina duplicados.
print("Palabras únicas:", palabras_unicas)

# Recuento de palabras
recuento = {} # diccionario vacío "recuento" para guardar los conteos.
for palabra in palabras: # recorremos cada palabra en la lista palabras.
    recuento[palabra] = recuento.get(palabra, 0) + 1 # recuento.get(palabra, 0) busca la palabra en el diccionario.
    # si existe, devuelve su valor actual.Le sumamos 1 y lo guardamos en el diccionario
    # sino existe devuelve , valor por defecto. 
print("Recuento:", recuento) # Mostramos el diccionario con los conteos
print("Palabras únicas:", palabras_unicas)# Mostramos las palabras unicas 

# 6 **************************************************************************
alumnos = {}

# Ingresar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = [] # Crea lista vacía para las notas del alumno actual
    for j in range(3): #  Para cada alumno, pide 3 notas
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota) #  Agrega la nota a la lista
    alumnos[nombre] = tuple(notas) # guarda las notas en formato tupla como valores en el diccionario "alumnos".

# Calcular y mostrar promedios
for nombre, notas in alumnos.items(): # alumnos.items() devuelve pares (nombre, notas) del diccionario
    promedio = sum(notas) / len(notas) # Suma todas las notas de un alumno y las divide por la cantidad de notas. 
    print(f"{nombre}: Promedio = {promedio:.2f}")# :.2 Formatea el promedio a 2 decimales
    
    
# 7 **************************************************************************
parcial1 = {1, 3, 5, 7, 9}
parcial2 = {2, 3, 5, 8, 9}

# Aprobaron ambos parciales con operador and
ambos = parcial1 & parcial2 #  # Equivalente a parcial1.intersection(parcial2)
print("Aprobaron ambos parciales:", ambos)

# Aprobaron el primer parcial
# .symmetric_difference() es un método de los conjuntos (set) en Python. 
# Se utiliza para obtener los elementos que están en uno y solo uno de los conjuntos (la diferencia simétrica).
solo_uno = parcial1.symmetric_difference(parcial2)
print("Aprobaron solo uno:", solo_uno) # imprimimos la variable que usamos para guardar el resultado de ".symmetric_difference()"

# Aprobaron al menos uno. Equivalente a parcial1 | parcial2.
al_menos_uno = parcial1.union(parcial2) # .union() todos los elementos sin repetición.
print("Aprobaron al menos uno:", al_menos_uno)


# 8 **************************************************************************
stock = {}

while True:
    print("\n1. Consultar stock")
    print("2. Agregar unidades")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        producto = input("Producto a consultar: ")
        print(f"Stock de {producto}: {stock.get(producto, 0)}")
    elif opcion == "2":
        producto = input("Producto: ")
        if producto in stock:
            unidades = int(input("Unidades a agregar: "))
            stock[producto] += unidades
        else:
            print("El producto no existe")
    elif opcion == "3":
        producto = input("Nuevo producto: ")
        unidades = int(input("Stock inicial: "))
        stock[producto] = unidades
    elif opcion == "4":
        break
    else:
        print("Opción inválida")
# 9 **************************************************************************
agenda = {}

while True:
    print("\n1. Agregar evento")
    print("2. Consultar evento")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        dia = input("Día (ej. lunes): ")
        hora = input("Hora (ej. 10:00): ")
        evento = input("Evento: ")
        agenda[(dia, hora)] = evento
    elif opcion == "2":
        dia = input("Día a consultar: ")
        hora = input("Hora a consultar: ")
        evento = agenda.get((dia, hora), "No hay eventos programados")
        print(f"Evento: {evento}")
    elif opcion == "3":
        break
    else:
        print("Opción inválida")
# 10 *************************************************************************
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}

invertido = {capital: pais for pais, capital in original.items()}
print("Diccionario invertido:", invertido)