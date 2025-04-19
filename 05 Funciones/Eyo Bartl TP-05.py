# 1 _____________________________________________________________________


def saludo ():
    print("Hola Mundo!!")
def main ():
    saludo()
main()

#2_____________________________________________________________________


def saludar_usuario(nombre):
    return f"Hola {nombre}!"

def main ():
    nombre_ingresado = input("Ingrese su nombre: ")
    saludo = saludar_usuario(nombre_ingresado)
    print(saludo)

main()

#3_____________________________________________________________________


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def main():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")

    informacion_personal(nombre, apellido, edad, residencia)

main()

#4_____________________________________________________________________


from math import pi  # importo la funcion pi de la biblioteca math

def calcular_area_circulo(radio):
    return pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

def main():
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
    
main()

#5_____________________________________________________________________


def segundos_a_horas(segundos):
    return segundos / 3600  # 1 hora = 3600 segundos

def main():
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

main()

#6_____________________________________________________________________


def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
    tabla_multiplicar(numero)

main()

#7_____________________________________________________________________

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida"
    return (suma, resta, multiplicacion, division)

def main():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
    
main()


#8_____________________________________________________________________

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main ():
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)

    print(f"Su IMC es: {imc:.2f}")
    
main()


#9_____________________________________________________________________

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)

    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
    
main()


#10_____________________________________________________________________

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def main():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(a, b, c)

    print(f"El promedio es: {promedio:.2f}")

main()