#haz una condicion de 3 numero

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))

if (numero1 > numero2 and numero1 > numero3):
    print(f"El numero mayor es:", numero1)

elif (numero2 > numero1 and numero2 > numero3):
    print(f"El numero mayor es:", numero2)
else: 
    print(f"El numero mayor es:", numero3)

#haz una condicion para saber cual es mayor, el menor y el de en medio

if (numero1 > numero2 and numero1 > numero3) and (numero1 < numero2 and numero1 < numero3):
    print(f"El numero menor es:", numero1)

elif (numero2 > numero1 and numero2 > numero3) and (numero2 < numero1 and numero2 < numero3):
    print(f"El numero menor es:", numero1)

elif (numero3 > numero1 and numero3 > numero2) and (numero3 < numero1 and numero3 < numero2):
    print(f"El numero menor es:", numero3)

elif (numero2 > numero1 and numero2 > numero3) and (numero2 < numero1 and numero2 < numero3):
    print(f"El numero menor es:", numero2)
else:
    print(f"El numero menor es:", numero3)

if (numero1 < numero2 and numero1 < numero3) and (numero1 > numero2 and numero1 > numero3):
    print(f"El numero en medio es:", numero1)

elif (numero1 < numero3 and numero1 < numero2) and (numero1 > numero3 and numero1 > numero2):
    print(f"El numero en medio es:", numero1)

elif (numero2 < numero1 and numero2 < numero3) and (numero2 > numero1 and numero2 > numero3):
    print(f"El numero en medio es:", numero2)

elif (numero3 < numero1 and numero3 < numero2) and (numero3 > numero1 and numero3 > numero2):
    print(f"El numero en medio es:", numero3)

elif (numero2 < numero3 and numero2 < numero1) and (numero2 > numero3 and numero2 > numero1):
    print(f"El numero en medio es:", numero2)


#haz una condicion del while donde pueda elegir que tabla de multiplicar y hacer si quiere volver la tabla

tabla = int(input("Ingrese la tabla de multiplicar que desea ver: "))
numero = int(input("Ingrese el numero hasta el que quiere multiplicar: "))

while numero > 0:
    print(f"{tabla} x {numero} = {tabla * numero}")
    numero -= 1

#Una funcion que reciba: palabras y que cuente cuantas veces se repite la "A"

def contar_a(palabras):
    contador = 0
    for palabra in palabras:
        contador += palabra.lower().count("a")
    return contador

palabras = ["Hola", "Mundo", "Esto", "Es", "Un", "Ejemplo"]

print(contar_a(palabras))

#haz un ejemplo de tupla, lista y conjunto

tupla = (1, 2, 3, 4, 5)
lista = [1, 2, 3, 4, 5]
conjunto = {1, 2, 3, 4, 5}

print(tupla[2])

#Haz Un diccionario que contenga una rutina

rutina = {
    "nombre": "Roberto Carlos Orellana",
    "descripcion": "Rutinal del dia de la manaña",
    "mañana": [
        {"clase": "bañarme", "descripcion": "Preparar la primera clase"},
        {"clase": "siguente clase", "descripcion": "Segunda clase "},
        {"clase": "tercera clase", "descripcion": "clase final para despues almorzar"}
    ]
}

print(rutina["mañana"][1]["descripcion"])





