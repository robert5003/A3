print("--- Ejercicio 3 ---")

# Paso 1: Definir la clase Auto.

class Auto:
    def __init__(self, marca, modelo, año, color, precio_compra, tipo):
        # Constructor que inicializa las características del auto.
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.precio_compra = precio_compra
        self.tipo = tipo
    
    def mostrar_datos(self):
        # Método para mostrar la información del auto.
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Precio de compra: ${self.precio_compra}")
        print("---------------------------------------------")
        print()
    
    def calcular_margen_ganancia(self):
        # Método que calcula y retorna el precio de venta con el margen de ganancia del 40%.
        return self.precio_compra * 1.4
    
    def es_nacional(self):
        # Método que verifica si el auto es de marca Nacional.
        return self.marca == "Nacional"
    
    def es_importado(self):
        # Método que verifica si el auto es de marca Importado.
        return self.marca == "Importado"
    
    def es_de_4_ruedas(self):
        # Método que verifica si el auto es de 4 ruedas.
        return self.tipo == "4 ruedas"
    
    def es_capaz_de_5_pasajeros(self):
        # Método que verifica si el auto tiene capacidad para 5 pasajeros.
        return self.tipo == "Capaz de 5 pasajeros"
    
# Paso 2: Crear objetos de la clase Auto.

# Creación de un objeto de auto nacional.
auto_nacional_1 = Auto("Nacional", "Toyota Camry", 2010, "Blanco", 20000.00, "4 ruedas")
auto_nacional_1.mostrar_datos()

# Creación de un objeto de auto importado.
auto_importado_1 = Auto("Importado", "Ford Fusion", 2015, "Negro", 30000.00, "4 ruedas")
auto_importado_1.mostrar_datos()

# Paso 3: Mostrar los datos de los objetos.

# Mostrar los datos del auto nacional.
auto_nacional_1.mostrar_datos()

# Mostrar los datos del auto importado.
auto_importado_1.mostrar_datos()

print("--- Fin del Ejercicio ---")
