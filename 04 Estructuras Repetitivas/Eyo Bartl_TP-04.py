# 1) Imprime los números del 1 al 100 desde un bucle for porque se sabe cuantas veces se quiere iterar 
for i in range (1,101):
    print(i)
    
print("_"*20)

# 2) Pide al usuario ingrese un numero y determine la cantidad de digitos que contiene el numero
num = int(input("Ingrese un numero: "))
print(f"La cantidad de digitos que contiene el numero {num} es: ", len(str(num))) 

print("_"*20)

# 3) Programa que sume todos los numeros comprendidos entre dos valores ingresados por el usuario pero que excluya esos dos valores
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = 0    
for i in range(num1+1, num2):
   suma += i
print(f"La suma de los numeros comprendidos entre {num1} y {num2} es: ", suma)

print("_"*20)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
# El programa debe mostrar el total acumulado al finalizar la suma.
suma = 0
while True:
    num = int(input("Ingrese un numero (0 para salir y ver el resultado de la suma de los números ingresados): "))
    if num == 0:
        break
    suma += num
print(f"La suma total acumulada es: {suma}")

print("_"*20)

# 5) El usuario deba adivinar un número aleatorio entre 0 y 9. El programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
num_aleatorio = random.randint(0, 9)   
intentos = 0
while True:
    num_usuario = int(input("Adivina el numero aleatorio entre 0 y 9: "))
    intentos += 1
    if num_usuario == num_aleatorio:
        print(f"Felicitaciones, adivinaste el numero {num_aleatorio} en {intentos} intentos.")
        break
    elif num_usuario < num_aleatorio:
        print("El numero es mayor.")
    else:
        print("El numero es menor.")
        
print("_"*20)

# 6) Programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100, -1, -2):
    print(i)    

# 7) Programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario y mostre el resultado de la suma.
num = int(input("Ingrese un numero entero positivo: "))
suma = 0
for i in range(num + 1):
    suma += i
print(f"La suma de los numeros comprendidos entre 0 y {num} es: ", suma)

#  8)   programa que permita al usuario ingresar 100 números enteros. 
# el Programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio)

num_pares = 0
num_impares = 0
num_positivos = 0
num_negativos = 0

for i in range(100):
    num = int(input("Ingrese un numero entero: "))
    if num % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
    if num > 0:
        num_positivos += 1
    elif num < 0:
        num_negativos += 1
        
print(f"Cantidad de numeros negativos: {num_negativos}")
print(f"Cantidad de numeros pares: {num_pares}")
print(f"Cantidad de numeros impares: {num_impares}")
print(f"Cantidad de numeros positivos: {num_positivos}")

print("_"*20) 

# 9) Programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
num = 0
suma = 0
for i in range(100):
    num = int(input("Ingrese un numero entero: "))
    suma += num 
media = suma / 100 
 
print(f"La media de los numeros es: {media}")

print("_"*20)

# 10) programa que invierta el orden de los dígitos de un número ingresado por elnusuario.
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

num = int(input("Ingrese un numero: "))
num_invertido = str(num)[::-1]  

print(f"El numero invertido es: {num_invertido}")


print("_"*20)



    


        
        