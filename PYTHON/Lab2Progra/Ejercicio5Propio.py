class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        # Muestra la información del plato, incluyendo su nombre y precio.
        print(f"Plato: {self.nombre}, Precio: ${self.precio:.2f}")


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.platos = []
        self.total = 0

    def agregar_plato(self, plato, cantidad):
        # Agrega un plato al pedido, junto con la cantidad deseada.
        # Calcula y actualiza el total del pedido.
        self.platos.append((plato, cantidad))
        self.total += plato.precio * cantidad

    def mostrar_informacion(self):
        # Muestra el resumen del pedido, incluyendo el cliente, 
        # los platos pedidos, la cantidad de cada plato y el total a pagar.
        print(f"Cliente: {self.cliente}")
        print("Platos pedidos:")
        for plato, cantidad in self.platos:
            print(f"- {plato.nombre} x{cantidad} -> ${plato.precio * cantidad:.2f}")
        print(f"Total a pagar: ${self.total:.2f}")


# Creación de algunos platos disponibles en el menú
menu = [
    Plato("Ensalada César", 8.50),
    Plato("Sopa de Tomate", 5.00),
    Plato("Pizza Margherita", 12.00),
    Plato("Lasagna", 15.00),
    Plato("Tarta de Queso", 6.50)
]

# Ejemplo de uso
print("Bienvenido al sistema de pedidos del restaurante.")
cliente = input("Ingrese el nombre del cliente: ")
pedido = Pedido(cliente)

# Mostrar menú y tomar pedido
print("\nMenú disponible:")
for i, plato in enumerate(menu, start=1):
    print(f"{i}. {plato.nombre} - ${plato.precio:.2f}")

while True:
    seleccion = int(input("\nSeleccione el número del plato (0 para terminar): "))
    if seleccion == 0:
        break
    elif 1 <= seleccion <= len(menu):
        cantidad = int(input(f"Ingrese la cantidad de {menu[seleccion - 1].nombre} deseada: "))
        pedido.agregar_plato(menu[seleccion - 1], cantidad)
    else:
        print("Selección inválida. Inténtelo nuevamente.")

# Mostrar resumen del pedido
print("\nResumen del pedido:")
pedido.mostrar_informacion()
