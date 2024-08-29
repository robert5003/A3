#Haz un ejercicio donde Una veterinaria atiende solamente perros y los registra en una base de datos. Se requiere un programa que lea la información básica del perro (no más de 8 características) y se muestre en pantalla. En esta veterinaria todos los animales que llegan, entran con el estado inicial de NO ATEN- DIDO y cuando se registran se cambia automáticamente a ATENDIDO. Por ahora como la veterinaria solo atiende perros, basado en el peso (menos de 10kg o más de 10kg) los registra como “Perro Grande” o “Pe- rro Pequeño”.

print("--- Ejercicio 1 ---")
#Paso 1: Crear una clase llamada Perro con las siguientes características: nombre, raza, edad, sexo, peso, color, estatus y tipo de perro (pequeño o grande).

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
        self.estatus = "ATENDIDO"
    
    def desatender(self):
        self.estatus = "NO ATENDIDO"
    
    def es_pequeño(self):
        return self.peso < 10
    
    def es_grande(self):
        return self.peso >= 10
    
    def cambiar_datos(self, nombre, raza, edad, sexo, peso, color, tipo):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.color = color
        self.tipo = tipo
        
    def cambiar_estatus(self, estatus):
        self.estatus = estatus
    
    def cambiar_tipo(self, tipo):
        self.tipo = tipo
        
    def es_adulto(self):
        return self.edad >= 1
    
    def es_joven(self):
        return self.edad < 1
    
    def calcular_edad_en_meses(self):
        return self.edad * 12
    
    def calcular_edad_en_dias(self):
        return self.edad * 365
    
    
#Paso 2: Crear una lista llamada base_datos y agregar varios perros a esta lista.

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

#Paso 3: Crear un bucle para mostrar los datos de cada perro en la lista en pantalla.

for perro in base_datos:
    perro.mostrar_datos()

#Paso 4: Crear un bucle para permitir al usuario seleccionar un perro y cambiar su estatus a ATENDIDO.

seleccionar_perro = int(input("Ingrese el número del perro que quiere seleccionar (1-5): "))

if seleccionar_perro >= 1 and seleccionar_perro <= 5:
    perro_seleccionado = base_datos[seleccionar_perro - 1]
    perro_seleccionado.atender()
    perro_seleccionado.mostrar_datos()
    print("El perro ha sido atendido correctamente.")

#Paso 5: Crear un bucle para permitir al usuario seleccionar un perro y cambiar sus datos.

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

#Paso 6: Crear un bucle para permitir al usuario seleccionar un perro y cambiar su estatus a NO ATENDIDO.

seleccionar_perro_desatender = int(input("Ingrese el número del perro que quiere seleccionar (1-5): "))

if seleccionar_perro_desatender >= 1 and seleccionar_perro_desatender <= 5:
    perro_seleccionado_desatender = base_datos[seleccionar_perro_desatender - 1]
    perro_seleccionado_desatender.desatender()
    perro_seleccionado_desatender.mostrar_datos()
    print("El perro ha sido desatendido correctamente.")

#Paso 7: Crear un bucle para mostrar los datos de cada perro en la lista en pantalla después de modificar o desatender algunos.

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


#Haz otro ejercicio donde Una papelería vende cuadernos y lápices. Los cuadernos pueden ser de 50 hojas o de 100 hojas. Los lápices pueden ser de grafito o de colores. El precio de venta es igual al precio de compra multiplicado por 1.30 que corresponde al margen de ganancia. La papelería requiere construir un programa que le permita registrar y visualizar por lo menos dos artículos de ítem. Todos los cuadernos son marca HOJITAS y los lápices son marca RAYAS ya que la papelería es un distribuidor exclusivo.

print("--- Ejercicio 2 ---")
#Paso 1: Definir la clase Cuaderno.

class Cuaderno:
    def __init__(self, numero_hojas, precio_compra, marca):
        self.numero_hojas = numero_hojas
        self.precio_compra = precio_compra
        self.marca = marca
        self.precio_venta = self.precio_compra * 1.30
    
    def mostrar_datos(self):
        print(f"Cuaderno: {self.marca}")
        print(f"Número de hojas: {self.numero_hojas}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print("---------------------------------------------")
        print()
    
    def cambiar_marca(self, nueva_marca):
        self.marca = nueva_marca
        self.precio_venta = self.precio_compra * 1.30
        self.mostrar_datos()
    
    def cambiar_precio_compra(self, nuevo_precio_compra):
        self.precio_compra = nuevo_precio_compra
        self.precio_venta = self.precio_compra * 1.30
        self.mostrar_datos()
    
    def cambiar_numero_hojas(self, nuevo_numero_hojas):
        self.numero_hojas = nuevo_numero_hojas
        self.mostrar_datos()
    
    def es_marca_hojitas(self):
        return self.marca == "HOJITAS"
    
    def es_marca_rayas(self):
        return self.marca == "RAYAS"
    
#Paso 2: Definir la clase Lápiz.

class Lapis:
    def __init__(self, color, precio_compra, marca):
        self.color = color
        self.precio_compra = precio_compra
        self.marca = marca
        self.precio_venta = self.precio_compra * 1.30
    
    def mostrar_datos(self):
        print(f"Lápiz: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print("---------------------------------------------")
        print()
    
    def cambiar_marca(self, nueva_marca):
        self.marca = nueva_marca
        self.precio_venta = self.precio_compra * 1.30
        self.mostrar_datos()
    
    def cambiar_precio_compra(self, nuevo_precio_compra):
        self.precio_compra = nuevo_precio_compra
        self.precio_venta = self.precio_compra * 1.30
        self.mostrar_datos()
    
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        self.mostrar_datos()
    
    def es_marca_hojitas(self):
        return False
    
    def es_marca_rayas(self):
        return self.marca == "RAYAS"

#Paso 3: Crear objetos de las clases Cuaderno y Lápiz.

cuaderno_hojitas_1 = Cuaderno(50, 10.50, "HOJITAS")
cuaderno_hojitas_1.mostrar_datos()

lapiz_rayas_1 = Lapis("Azul", 2.50, "RAYAS")
lapiz_rayas_1.mostrar_datos()

#Paso 4: Modificar los datos de los objetos.

cuaderno_hojitas_1.cambiar_marca("NUEVA MARCA")
cuaderno_hojitas_1.cambiar_precio_compra(12.00)
cuaderno_hojitas_1.cambiar_numero_hojas(75)

lapiz_rayas_1.cambiar_marca("NUEVA MARCA")

#Paso 5: Mostrar los datos de los objetos modificados.

cuaderno_hojitas_1.mostrar_datos()
lapiz_rayas_1.mostrar_datos()

#Haz otro ejercicio donde un concesionario de autos vende vehículos nacionales e importados. Todos tienen 4 ruedas y capacidad para 5 pasajeros. Esta información debe registrarse siempre por razones de ley. Requiere un programa que le permita almacenar las 10 principales características de los autos. El precio de venta de cada auto es igual al precio de compra multiplicado por 1.4 que corresponde a su margen de ganancia.

print("--- Ejercicio 3 ---")

#Paso 1: Definir la clase Auto.

class Auto:
    def __init__(self, marca, modelo, año, color, precio_compra, tipo):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.precio_compra = precio_compra
    
    def mostrar_datos(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Precio de compra: ${self.precio_compra}")
        print("---------------------------------------------")
        print()
    
    def calcular_margen_ganancia(self):
        return self.precio_compra * 1.4
    
    def es_nacional(self):
        return self.marca == "Nacional"
    
    def es_importado(self):
        return self.marca == "Importado"
    
    def es_de_4_ruedas(self):
        return self.tipo == "4 ruedas"
    
    def es_capaz_de_5_pasajeros(self):
        return self.tipo == "Capaz de 5 pasajeros"
    
#Paso 2: Crear objetos de la clase Auto.

auto_nacional_1 = Auto("Nacional", "Toyota Camry", 2010, "Blanco", 20000.00, "4 ruedas")
auto_nacional_1.mostrar_datos()

auto_importado_1 = Auto("Importado", "Ford Fusion", 2015, "Negro", 30000.00, "4 ruedas")
auto_importado_1.mostrar_datos()

#Paso 3: Mostrar los datos de los objetos.

auto_nacional_1.mostrar_datos()
auto_importado_1.mostrar_datos()

print("--- Fin del Ejercicio ---")

#Haz un ejercicio donde un almacén vende dispositivos electrónicos (celulares, tablets y portá- tiles). Todos PHR que es una nueva marca que está entrando en el mer- cado. Se requiere almacenar sus 6 principales características. Todos son productos importados y su precio de venta es igual al precio de compra multiplicado por 1.7 que corresponde a su margen de ganancia.

print("--- Ejercicio 4 ---")

#Paso 1: Definir la clase DispositivoElectrónico.

class DispositivoElectronico:
    def __init__(self, marca, modelo, año, color, precio_compra, tipo):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.precio_compra = precio_compra
        self.tipo = tipo
    
    def mostrar_datos(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Tipo: {self.tipo}")
        print("---------------------------------------------")
        print()
    
    def calcular_margen_ganancia(self):
        return self.precio_compra * 1.7
    
    def es_nueva_marca(self):
        return self.marca == "Nueva Marca"
    
    def es_importado(self):
        return True
    
    def es_celular(self):
        return self.tipo == "Celular"
    
    def es_tablet(self):
        return self.tipo == "Tablet"
    
    def es_portatil(self):
        return self.tipo == "Portátil"
    
#Paso 2: Crear objetos de la clase DispositivoElectrónico.

dispositivo_electronico_celular_1 = DispositivoElectronico("Nueva Marca", "Samsung Galaxy S20", 2020, "Negro", 15000.00, "Celular")
dispositivo_electronico_celular_1.mostrar_datos()

dispositivo_electronico_tablet_1 = DispositivoElectronico("Nueva Marca", "Apple iPad Pro", 2021, "Gris", 25000.00, "Tablet")
dispositivo_electronico_tablet_1.mostrar_datos()

dispositivo_electronico_portatil_1 = DispositivoElectronico("Nueva Marca", "Acer Aspire 5", 2022, "Blanco", 10000.00, "Portátil")

#Paso 3: Mostrar los datos de los objetos.

dispositivo_electronico_celular_1.mostrar_datos()
dispositivo_electronico_tablet_1.mostrar_datos()
dispositivo_electronico_portatil_1.mostrar_datos()

print("--- Fin del Ejercicio ---")