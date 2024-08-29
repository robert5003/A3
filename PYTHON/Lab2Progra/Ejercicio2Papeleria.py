print("--- Ejercicio 2 ---")
# Paso 1: Definir la clase Cuaderno.

class Cuaderno:
    def __init__(self, numero_hojas, precio_compra, marca):
        # Constructor que inicializa las características del cuaderno.
        self.numero_hojas = numero_hojas
        self.precio_compra = precio_compra
        self.marca = marca
        self.precio_venta = self.precio_compra * 1.30
    
    def mostrar_datos(self):
        # Método para mostrar la información del cuaderno.
        print(f"Cuaderno: {self.marca}")
        print(f"Número de hojas: {self.numero_hojas}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print("---------------------------------------------")
        print()
    
    def cambiar_marca(self, nueva_marca):
        # Método para cambiar la marca del cuaderno.
        self.marca = nueva_marca
        self.precio_venta = self.precio_compra * 1.30
        self.mostrar_datos()
    
    def cambiar_precio_compra(self, nuevo_precio_compra):
        # Método para cambiar el precio de compra del cuaderno.
        self.precio_compra = nuevo_precio_compra
        self.precio_venta = self.precio_compra * 1.30
        self.mostrar_datos()
    
    def cambiar_numero_hojas(self, nuevo_numero_hojas):
        # Método para cambiar el número de hojas del cuaderno.
        self.numero_hojas = nuevo_numero_hojas
        self.mostrar_datos()
    
    def es_marca_hojitas(self):
        # Método que verifica si el cuaderno es de la marca HOJITAS.
        return self.marca == "HOJITAS"
    
    def es_marca_rayas(self):
        # Método que verifica si el cuaderno es de la marca RAYAS.
        return self.marca == "RAYAS"

# Paso 2: Definir la clase Lápiz.

class Lapiz:  # nombre de la clase
    def __init__(self, color, precio_compra, marca):
        # Constructor que inicializa las características del lápiz.
        self.color = color
        self.precio_compra = precio_compra
        self.marca = marca
        self.precio_venta = self.precio_compra * 1.30
    
    def mostrar_datos(self):
        # Método para mostrar la información del lápiz.
        print(f"Lápiz: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Precio de compra: ${self.precio_compra}")
        print(f"Precio de venta: ${self.precio_venta}")
        print("---------------------------------------------")
        print()
    
    def cambiar_marca(self, nueva_marca):
        # Método para cambiar la marca del lápiz.
        self.marca = nueva_marca
        self.precio_venta = self.precio_compra * 1.30
        self.mostrar_datos()
    
    def cambiar_precio_compra(self, nuevo_precio_compra):
        # Método para cambiar el precio de compra del lápiz.
        self.precio_compra = nuevo_precio_compra
        self.precio_venta = self.precio_compra * 1.30
        self.mostrar_datos()
    
    def cambiar_color(self, nuevo_color):
        # Método para cambiar el color del lápiz.
        self.color = nuevo_color
        self.mostrar_datos()
    
    def es_marca_hojitas(self):
        # Método que verifica si el lápiz es de la marca HOJITAS (siempre devuelve False).
        return False
    
    def es_marca_rayas(self):
        # Método que verifica si el lápiz es de la marca RAYAS.
        return self.marca == "RAYAS"

# Paso 3: Crear objetos de las clases Cuaderno y Lápiz.

cuaderno_hojitas_1 = Cuaderno(50, 10.50, "HOJITAS")
cuaderno_hojitas_1.mostrar_datos()

lapiz_rayas_1 = Lapiz("Azul", 2.50, "RAYAS")  # Corregido el nombre de la clase
lapiz_rayas_1.mostrar_datos()

# Paso 4: Modificar los datos de los objetos.

cuaderno_hojitas_1.cambiar_marca("NUEVA MARCA")
cuaderno_hojitas_1.cambiar_precio_compra(12.00)
cuaderno_hojitas_1.cambiar_numero_hojas(75)

lapiz_rayas_1.cambiar_marca("NUEVA MARCA")

# Paso 5: Mostrar los datos de los objetos modificados.

cuaderno_hojitas_1.mostrar_datos()
lapiz_rayas_1.mostrar_datos()

print("--- Fin del Ejercicio ---")
