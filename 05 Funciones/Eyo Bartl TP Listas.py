#1***********************************************************

lista_M4 = list(range(0,101,4))
print(lista_M4)

#2***********************************************************

lista_elemetos= ["auto","moto","tren","bici","micro"]
print("el penultimo medio de trasporte es: ",lista_elemetos[-2])

#3***********************************************************

lista_vacia = []

lista_vacia.append(1)
lista_vacia.append(2)

print(lista_vacia)

#4***********************************************************

animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[-2]="loro"
animales[-1]="oso"
print(animales)

#5***********************************************************

numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
"""el este fragmento de codigo se removio el numero mas grande de la lista "numeros" """

#6***********************************************************

lista_10_30 = list(range(10,31,5))
print(lista_10_30[0])
print(lista_10_30[1])

#7***********************************************************

autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1]="fox"
autos[2]="vento"
print(autos)

#8***********************************************************

dobles= []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9***********************************************************

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

print(compras)

compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")

print(compras)

#10**********************************************************

lista_anidada=[15, True, [25.5, 57.9, 30.6], False ]
print(lista_anidada)


#************************************************************