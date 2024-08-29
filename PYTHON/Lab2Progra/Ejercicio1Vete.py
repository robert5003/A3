print("--- Ejercicio 1 ---")

# Paso 1: Crear una clase llamada Perro con las siguientes características: 
# nombre, raza, edad, sexo, peso, color, estatus y tipo de perro (pequeño o grande).

class Perro:
    def __init__(self, nombre, raza, edad, sexo, peso, color, estatus, tipo):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.color = color
        self.estatus = "NO ATENDIDO"
        self.tipo = tipo
    
    def mostrar_datos(self):
        # Muestra la información del perro en pantalla.
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Sexo: {self.sexo}")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Estatus: {self.estatus}")
        print(f"Tipo: {self.tipo}")
        print("---------------------------------------------")
    
    def atender(self):
        # Cambia el estatus del perro a 'ATENDIDO'.
        self.estatus = "ATENDIDO"
    
    def desatender(self):
        # Cambia el estatus del perro a 'NO ATENDIDO'.
        self.estatus = "NO ATENDIDO"
    
    def es_pequeño(self):
        # Verifica si el perro es pequeño (peso menor a 10 kg).
        return self.peso < 10
    
    def es_grande(self):
        # Verifica si el perro es grande (peso mayor o igual a 10 kg).
        return self.peso >= 10
    
    def cambiar_datos(self, nombre, raza, edad, sexo, peso, color, tipo):
        # Permite cambiar los datos del perro.
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.color = color
        self.tipo = tipo
        
    def cambiar_estatus(self, estatus):
        # Permite cambiar el estatus del perro.
        self.estatus = estatus
    
    def cambiar_tipo(self, tipo):
        # Permite cambiar el tipo del perro (pequeño o grande).
        self.tipo = tipo
        
    def es_adulto(self):
        # Verifica si el perro es adulto (edad mayor o igual a 1 año).
        return self.edad >= 1
    
    def es_joven(self):
        # Verifica si el perro es joven (edad menor a 1 año).
        return self.edad < 1
    
    def calcular_edad_en_meses(self):
        # Calcula la edad del perro en meses.
        return self.edad * 12
    
    def calcular_edad_en_dias(self):
        # Calcula la edad del perro en días.
        return self.edad * 365
    
    
# Paso 2: Crear una lista llamada base_datos y agregar varios perros a esta lista.
base_datos = []

perro1 = Perro("Buddy", "Golden Retriever", 4, "Macho", 10.5, "Blanco y Gris", "ATENDIDO", "Pequeño")
base_datos.append(perro1)

perro2 = Perro("Max", "Golden Retriever", 3, "Macho", 12.5, "Negro y Gris", "ATENDIDO", "Pequeño")
base_datos.append(perro2)

perro3 = Perro("Luna", "Labrador", 2, "Hembra", 11.2, "Blanco y Gris", "ATENDIDO", "Pequeño")
base_datos.append(perro3)

perro4 = Perro("Rex", "Golden Retriever", 5, "Macho", 10.8, "Blanco y Gris", "ATENDIDO", "Pequeño")
base_datos.append(perro4)

perro5 = Perro("Luna", "Golden Retriever", 3, "Hembra", 12.5, "Negro y Gris", "ATENDIDO", "Pequeño")
base_datos.append(perro5)

# Paso 3: Crear un bucle para mostrar los datos de cada perro en la lista en pantalla.
for perro in base_datos:
    perro.mostrar_datos()

# Paso 4: Crear un bucle para permitir al usuario seleccionar un perro y cambiar su estatus a ATENDIDO.
seleccionar_perro = int(input("Ingrese el número del perro que quiere seleccionar (1-5): "))

if seleccionar_perro >= 1 and seleccionar_perro <= 5:
    perro_seleccionado = base_datos[seleccionar_perro - 1]
    perro_seleccionado.atender()
    perro_seleccionado.mostrar_datos()
    print("El perro ha sido atendido correctamente.")

# Paso 5: Crear un bucle para permitir al usuario seleccionar un perro y cambiar sus datos.
seleccionar_perro_modificar = int(input("Ingrese el número del perro que quiere seleccionar (1-5): "))

if seleccionar_perro_modificar >= 1 and seleccionar_perro_modificar <= 5:
    perro_seleccionado_modificar = base_datos[seleccionar_perro_modificar - 1]
    nombre_modificar = input("Ingrese el nuevo nombre del perro: ")
    raza_modificar = input("Ingrese la nueva raza del perro: ")
    edad_modificar = int(input("Ingrese la nueva edad del perro (en años): "))
    sexo_modificar = input("Ingrese el nuevo sexo del perro (Macho/Hembra): ")
    peso_modificar = float(input("Ingrese el nuevo peso del perro (en kg): "))
    color_modificar = input("Ingrese el nuevo color del perro: ")
    tipo_modificar = input("Ingrese el nuevo tipo del perro (Pequeño/Grande): ")
    perro_seleccionado_modificar.cambiar_datos(nombre_modificar, raza_modificar, edad_modificar, sexo_modificar, peso_modificar, color_modificar, tipo_modificar)
    perro_seleccionado_modificar.mostrar_datos()
    print("Los datos del perro han sido modificados correctamente.")

# Paso 6: Crear un bucle para permitir al usuario seleccionar un perro y cambiar su estatus a NO ATENDIDO.
seleccionar_perro_desatender = int(input("Ingrese el número del perro que quiere seleccionar (1-5): "))

if seleccionar_perro_desatender >= 1 and seleccionar_perro_desatender <= 5:
    perro_seleccionado_desatender = base_datos[seleccionar_perro_desatender - 1]
    perro_seleccionado_desatender.desatender()
    perro_seleccionado_desatender.mostrar_datos()
    print("El perro ha sido desatendido correctamente.")

# Paso 7: Crear un bucle para mostrar los datos de cada perro en la lista en pantalla después de modificar o desatender algunos.
print("---------------------------------------------")

for perro in base_datos:
    perro.mostrar_datos()
    print("---------------------------------------------")
    print()
    print("--- Estadísticas ---")
    print(f"Total de perros: {len(base_datos)}")
    print(f"Perros atendidos: {sum(perro.estatus == 'ATENDIDO' for perro in base_datos)}")
    print(f"Perros no atendidos: {sum(perro.estatus == 'NO ATENDIDO' for perro in base_datos)}")
    print(f"Perros pequeños: {sum(perro.es_pequeño() for perro in base_datos)}")
    print(f"Perros grandes: {sum(perro.es_grande() for perro in base_datos)}")
    print(f"Perros adultos: {sum(perro.es_adulto() for perro in base_datos)}")
    print(f"Perros jóvenes: {sum(perro.es_joven() for perro in base_datos)}")
    print(f"Promedio de edad en años: {sum(perro.edad for perro in base_datos) / len(base_datos) if len(base_datos) > 0 else 0}")
    print(f"Promedio de edad en meses: {sum(perro.calcular_edad_en_meses() for perro in base_datos) / len(base_datos) if len(base_datos) > 0 else 0}")
    print(f"Promedio de edad en días: {sum(perro.calcular_edad_en_dias() for perro in base_datos) / len(base_datos) if len(base_datos) > 0 else 0}")
    print("---------------------------------------------")
    print()
    input("Presione enter para continuar...")
    print("---------------------------------------------")
    print()

print("--- Fin del Ejercicio ---")
