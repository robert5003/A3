
print("--- Ejercicio 1 ---")

class Perro:
    def __init__(self, nombre, raza, edad, peso, color, dueño, telefono_dueño):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.dueño = dueño
        self.telefono_dueño = telefono_dueño
        self.estado = "NO ATENDIDO"
        self.tamaño = self.definir_tamaño()

    def definir_tamaño(self):
        if self.peso < 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"

    def registrar_atencion(self):
        self.estado = "ATENDIDO"

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Dueño: {self.dueño}")
        print(f"Teléfono del Dueño: {self.telefono_dueño}")
        print(f"Estado: {self.estado}")
        print(f"Tamaño: {self.tamaño}")

# Ejemplo de uso
nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
edad = int(input("Ingrese la edad del perro: "))
peso = float(input("Ingrese el peso del perro (en kg): "))
color = input("Ingrese el color del perro: ")
dueño = input("Ingrese el nombre del dueño: ")
telefono_dueño = input("Ingrese el teléfono del dueño: ")

perro = Perro(nombre, raza, edad, peso, color, dueño, telefono_dueño)
perro.registrar_atencion()
perro.mostrar_informacion()

print("*****************************************************************************")

print("--- Ejercicio 2 ---")

class Articulo:
    def __init__(self, precio_compra):
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.30

    def mostrar_informacion(self):
        pass  # Este método será sobrescrito en las subclases


class Cuaderno(Articulo):
    def __init__(self, precio_compra, hojas):
        super().__init__(precio_compra)
        self.hojas = hojas
        self.marca = "HOJITAS"

    def mostrar_informacion(self):
        print(f"Artículo: Cuaderno")
        print(f"Marca: {self.marca}")
        print(f"Hojas: {self.hojas}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")


class Lapiz(Articulo):
    def __init__(self, precio_compra, tipo):
        super().__init__(precio_compra)
        self.tipo = tipo
        self.marca = "RAYAS"

    def mostrar_informacion(self):
        print(f"Artículo: Lápiz")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")


# Ejemplo de uso
cuaderno1 = Cuaderno(precio_compra=1.50, hojas=50)
cuaderno2 = Cuaderno(precio_compra=2.80, hojas=100)

lapiz1 = Lapiz(precio_compra=0.30, tipo="Grafito")
lapiz2 = Lapiz(precio_compra=0.50, tipo="Colores")

# Mostrar información de los artículos
cuaderno1.mostrar_informacion()
print()
cuaderno2.mostrar_informacion()
print()
lapiz1.mostrar_informacion()
print()
lapiz2.mostrar_informacion()

print("*****************************************************************************")

print("--- Ejercicio 3 ---")

class Auto:
    def __init__(self, marca, modelo, año, color, tipo, motor, combustible, traccion, precio_compra, origen):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo = tipo  # Por ejemplo, SUV, Sedán, Hatchback
        self.motor = motor  # Ejemplo: 2.0L
        self.combustible = combustible  # Ejemplo: Gasolina, Diesel
        self.traccion = traccion  # Ejemplo: 4x4, Tracción delantera
        self.precio_compra = precio_compra
        self.origen = origen  # Nacional o Importado
        self.ruedas = 4
        self.capacidad_pasajeros = 5
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.4

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Motor: {self.motor}")
        print(f"Combustible: {self.combustible}")
        print(f"Tracción: {self.traccion}")
        print(f"Origen: {self.origen}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")


# Ejemplo de uso
auto1 = Auto(
    marca="Toyota",
    modelo="Corolla",
    año=2023,
    color="Blanco",
    tipo="Sedán",
    motor="1.8L",
    combustible="Gasolina",
    traccion="Tracción delantera",
    precio_compra=20000,
    origen="Nacional"
)

auto2 = Auto(
    marca="BMW",
    modelo="X5",
    año=2024,
    color="Negro",
    tipo="SUV",
    motor="3.0L",
    combustible="Diesel",
    traccion="4x4",
    precio_compra=50000,
    origen="Importado"
)

# Mostrar información de los autos
auto1.mostrar_informacion()
print()
auto2.mostrar_informacion()

print("*****************************************************************************")

print("--- Ejercicio 4 ---")

class DispositivoElectronico:
    def __init__(self, tipo, modelo, almacenamiento, ram, procesador, pantalla, precio_compra):
        self.marca = "PHR"  # Todos los dispositivos son de la marca PHR
        self.tipo = tipo  # Puede ser Celular, Tablet, o Portátil
        self.modelo = modelo
        self.almacenamiento = almacenamiento  # Ejemplo: 128GB, 256GB
        self.ram = ram  # Ejemplo: 4GB, 8GB
        self.procesador = procesador  # Ejemplo: Snapdragon 888, Intel i5
        self.pantalla = pantalla  # Tamaño de la pantalla en pulgadas
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
        self.origen = "Importado"  # Todos los productos son importados

    def calcular_precio_venta(self):
        return self.precio_compra * 1.7

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"RAM: {self.ram}")
        print(f"Procesador: {self.procesador}")
        print(f"Pantalla: {self.pantalla} pulgadas")
        print(f"Origen: {self.origen}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")


# Ejemplo de uso
dispositivo1 = DispositivoElectronico(
    tipo="Celular",
    modelo="PHR Galaxy",
    almacenamiento="128GB",
    ram="8GB",
    procesador="Snapdragon 888",
    pantalla=6.5,
    precio_compra=300
)

dispositivo2 = DispositivoElectronico(
    tipo="Portátil",
    modelo="PHR Ultrabook",
    almacenamiento="512GB",
    ram="16GB",
    procesador="Intel i7",
    pantalla=15.6,
    precio_compra=800
)

# Mostrar información de los dispositivos
dispositivo1.mostrar_informacion()
print()
dispositivo2.mostrar_informacion()
