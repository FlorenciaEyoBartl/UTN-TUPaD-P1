from math import pi


print("_________________________________________________")
#Ejercicio_1

print("hola mundo!")

print("_________________________________________________")
#Ejercicio_2

nombre = input ("Por favor ingrese su nombre: ")
saludo = print ("Hola", (nombre))

print("_________________________________________________")
#Ejercicio_3

print("Indique los siguientes datos personales: ")
print ()
nombre= input("Nombre: ")
print()
apellido= input("Apellido: ")
print()
edad = int(input("Edad: "))
print()
recidencia= input("Lugar de recidencia: ")

print(f"Su nombre completo es: {nombre} {apellido}, usted tiene {edad} años y recide en {recidencia}")

print("_________________________________________________")
#Ejercicio_4

from math import pi

radio=float(input("Ingrese el valor del rádio de la circunferencia: "))

perimetro =round( 2*radio * pi, 2) 
area =round (pi * (radio**2), 2)

print(f"El perimetro de la circunferencia es: {perimetro}")

print(f"El area de la circunferencia es: {area}")

print("_________________________________________________")
#Ejercicio_5

segundos =int(input("Ingrese la cantidad de segundos: "))

# 3600 = la cantidad de segundos que contiene 1 hora (60*60)
#convierte segundos a horas
horas = segundos / 3600

print(f"La cantidad de segundos {segundos} equivalen a {round(horas,2)} horas")


print("_________________________________________________")
#Ejercicio_6

numero = int( input("Ingrese un número: "))
print()
print(f"La tabla de multiplicación del 1 al 10 del {numero} es: ")
print("_________________________________________________")

# bucle for recorre los valores que va tomando la variable i 
# para multiplicarlos por la variable numero
# el rango establece la cantidad de veces que se ejecuta el bucle 
# del 1 al 10 inclusive 


for i in range(1,11):
    print(f" {numero} * {i} = {numero * i}")
    

print("_________________________________________________")
#Ejercicio_7


while True:
    
    num_1 = int(input("Ingrese un número distinto de 0: "))
    num_2 = int(input("Ingrese un número distinto de 0: "))

    if num_1 != 0 and num_2 != 0:
        break # si alguno de los dos o los dos valen 0 , se sale del bucle
    else:
     print("Debes digitar en ambos casos un número distinto de 0, vuelve a intentarlo")
     

# operaciones: si son distintos de 0 

suma = num_1 + num_2

resta =  num_1 - num_2

multiplicacion =  num_1 * num_2

division =  num_1 / num_2

# muestra resultado operaciones:

print(f"{num_1} + {num_2} = {suma}")

print(f"{num_1} - {num_2} = {resta}")

print(f"{num_1} * {num_2} = {multiplicacion}")

print(f"{num_1} / {num_2} = {round(division,2)}")

print("_________________________________________________")
#Ejercicio_8


altura = float(input("Ingrese su altura: "))

peso = float(input("Ingrese su peso: "))

imc = peso / (altura ** 2) 

print(f"Su Indice de masa corporal (IMC) es: {imc}")


print("_________________________________________________")
#Ejercicio_9

from fractions import Fraction

grados_c = float(input("Ingrese la temperatura en grados Celsius: "))

f = Fraction(9,5)

grados_F = ( (f * grados_c) + 32 )

print (f" ({f} * {grados_c}) + 32 = {round(grados_F,2)}") 

print(f"La misma temperatura en grados Fahrenheit es de: {round (grados_F,2)}")


print("_________________________________________________")
#Ejercicio_10

#programa que pida al usuario 3 números e imprima por pantalla el promedio de

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))
numero_3 = int(input("Ingrese el tercer numero: "))

promedio = (numero_1 + numero_2 + numero_3) / 3

print (f"El promerdio entre los números ingresados es de: {promedio}")