#1)***********************************************************
def recur_factorial(n):
    if n == 0:     # caso base
        return 1
    else:
        return n * recur_factorial(n - 1)  # caso recursivo

# pedimos al usuario un numero
num = int(input("Introduce un número entero positivo: "))

# con un buble for recorremos del 1 hasta num (inclusive) y mostramos el factorial de cada uno
for i in range(1, num + 1):
    print(f"{i}! = {recur_factorial(i)}")


#2)***********************************************************
# funcion recursiva que calcula el numero de fibonacci que le corresponde a cada posicion 
def fibonacci_recursivo(n):
    if n == 0:    #caso base
        return 0
    elif n == 1:  #caso base
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2) # caso recursivo

# funcion que muestra, a traves de un bucle for, la posicion de la serie y su numero de fibonacci correspondiente
def mostrar_serie_fibonacci(n):
    for i in range(n + 1):
        print(f"Posición {i}: {fibonacci_recursivo(i)}")

# Se le pide a al usuario un numero para calcular su posicion y serie de fibonacci 
n = int(input("Ingrese la posición hasta la que desea generar la serie de fibonacci: "))
mostrar_serie_fibonacci(n)


#3)***********************************************************
def potencia_recursiva(n, m):
    if m == 0: # caso base (exponente 0)
        return 1
    else:
        return n * potencia_recursiva(n, m - 1) # caso recursivo ( n^m = n * n^(m-1) )

# Entrada de usuario
base = int(input("Ingrese la base (n): "))
exponente = int(input("Ingrese el exponente (m): "))

# Cálculo y resultado
resultado = potencia_recursiva(base, exponente)
print(f"{base} elevado a {exponente} es: {resultado}")


#4)***********************************************************
def decimal_a_binario(n):
    if n == 0:       # Caso base si el numero es 0 o 1, devolvemos directamente su valor como string
        return "0"
    elif n == 1:
        return "1"
    else:
        # Caso recursivo convertimos el cociente y agregamos el resto al final
        return decimal_a_binario(n // 2) + str(n % 2)

# se le pide al usuario ingrese un numero 
numero = int(input("Ingrese un número entero positivo: "))

if numero >= 0:  # aseguramos que el numero ingresado por el usuario sea igual o mayor a 0
    binario = decimal_a_binario(numero) # binario es la variable que va a almacenar el resultado de la funcion recursiva
    print(f"El número {numero} en binario es: {binario}") # se muestra el resultado por consola
else:
    print("Por favor, ingrese un número entero positivo.") # en caso de que el usuario no ingrese el dato solicitado se muestra el mensaje de error


#5)***********************************************************
def es_palindromo(palabra):
    # caso base la palabra tiene 0 o 1 letra, es palindromo
    if len(palabra) <= 1:
        return True
    # si la primera y la ultima letra no coinciden, no es palindromo
    elif palabra[0] != palabra[-1]:
        return False
    else:
        # caso recursivo verificamos la palabra por los extremos (que en cada verificacion se iran acortando en 1 caracter por ambos lados)
        return es_palindromo(palabra[1:-1])

# programa principal

texto = input("Ingrese una palabra sin espacios ni tildes: ").lower() # .lower() convierte todo a minusculas

if texto.isalpha():  # .isalpha() verifica que el texto este compuesto solo por letras 
    if es_palindromo(texto):
        print(f"{texto} es un palíndromo ")
    else:
        print(f"{texto} no es un palíndromo")
else:
    print("Por favor, ingrese solo letras, sin espacios ni símbolos.")


#6)***********************************************************
def suma_digitos(num):
    # Caso base: si el número es de un solo dígito, lo devolvemos tal cual
    if num < 10:
        return num
    else:
        # Obtenemos el último dígito (n % 10) y sumamos el resto de los dígitos (n // 10)
        return (num % 10) + suma_digitos(num // 10)

# Solicitar el número al usuario
num = int(input("Ingrese un valor para sumar sus dígitos: "))

# Calcular la suma de los dígitos
resultado = suma_digitos(num)

# Mostrar el resultado
print(f"La suma de los dígitos de {num} es: {resultado}")


#7)***********************************************************
def contar_bloques(n):
    if n == 1:  # caso base 
        return 1 
    else:
        return n + contar_bloques(n - 1) # # va calculando por cada nivel de la piramide un bloque menos que en la base.

nivel_base = int(input("Ingrese el número de bloques en la base: "))
total = contar_bloques(nivel_base)
print(f"El total de bloques necesarios para la pirámide es: {total}")


#8)***********************************************************
def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        return (1 if ultimo_digito == digito else 0) + contar_digito(resto_numero, digito)

# Solicitar datos al usuario con validación
while True:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        digito = int(input("Ingrese un dígito a buscar (0-9): "))
        if numero >= 0 and 0 <= digito <= 9:
            break
        print("¡Número debe ser positivo y dígito entre 0-9!")
    except ValueError:
        print("¡Ingrese valores numéricos válidos!")

# Calcular y mostrar resultado
cantidad = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}")

