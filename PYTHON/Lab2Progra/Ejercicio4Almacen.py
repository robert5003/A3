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