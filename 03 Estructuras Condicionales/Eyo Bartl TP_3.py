# 1 Edad del usuario
edad = int(input("Ingrese su edad: "))

# Verifica si es mayor de edad
if edad > 18:
    print("Es mayor de edad")

print("______________________________________________________________________")

# 2 nota del usuario
nota = float(input("Ingrese su nota: "))

# Verifica si la nota es mayor o igual a 6
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("______________________________________________________________________")

# 3 número par 
numero = int(input("Ingrese un número: "))

# Verifica si es par usando el operador módulo
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print("______________________________________________________________________")

# 4 edad del usuario
edad = int(input("Ingrese su edad: "))

# categoría a la que pertenece
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
    
print("______________________________________________________________________")

# 5 ingrese una contraseña
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

# verifica la longitud con len()
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

    
print("______________________________________________________________________")

# 6 EStadística

import random
from statistics import mode, median, mean

# Crear una lista con 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular los parámetros estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Imprimir los valores calculados
print("Lista de números:", numeros_aleatorios)
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Comparar para determinar el tipo de sesgo
if media > mediana > moda:
    print("Distribución con sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Distribución con sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Distribución sin sesgo")
else:
    print("No se puede determinar un sesgo claro")

print("______________________________________________________________________")

# 7 caracter 
texto = input("Ingrese una palabra o frase: ")

# Verificamos si el último carácter es una vocal (mayúscula o minúscula)
if texto[-1].lower() in "aeiou":
    texto += "!"  # Añadimos el signo de exclamación al final

# Mostramos el resultado
print(texto)


print("______________________________________________________________________")

# 8 ingresa el nombre al usuario
nombre = input("Ingrese su nombre: ")

# opciones
print("¿Cómo desea que se muestre su nombre?")
print("1. En mayúsculas")
print("2. En minúsculas")
print("3. Con la primera letra en mayúscula")

# Solicita opción
opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

# transformación según la opción seleccionada
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida. Por favor elija 1, 2 o 3.")


print("______________________________________________________________________")

# 9 Ingreso magnitud del terremoto

magnitud = float(input("Ingrese la magnitud del terremoto según la escala de Richter: "))

# Clasificamos 
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:  # magnitud >= 7
    print("Extremo (puede causar graves daños a gran escala).")
    
    
print("______________________________________________________________________")

# 10 solicitamos los datos al usuario

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))

# Convertimos el mes y día a una "fecha simplificada" a tupla para comparar más fácilmente
fecha = (mes, dia)

# Determinamos la estación según el hemisferio

if hemisferio == "N":
    if (fecha >= (12, 21) or fecha <= (3, 20)):
        estacion = "Invierno"
    elif (fecha >= (3, 21) and fecha <= (6, 20)):
        estacion = "Primavera"
    elif (fecha >= (6, 21) and fecha <= (9, 20)):
        estacion = "Verano"
    elif (fecha >= (9, 21) and fecha <= (12, 20)):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if (fecha >= (12, 21) or fecha <= (3, 20)):
        estacion = "Verano"
    elif (fecha >= (3, 21) and fecha <= (6, 20)):
        estacion = "Otoño"
    elif (fecha >= (6, 21) and fecha <= (9, 20)):
        estacion = "Invierno"
    elif (fecha >= (9, 21) and fecha <= (12, 20)):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio no válido"

# Mostramos el resultado
print(f"En esa fecha, en el hemisferio {hemisferio.upper()}, es {estacion}.")
