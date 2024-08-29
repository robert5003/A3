class Evento:
    def __init__(self, fecha, lugar, num_asistentes, servicios):
        # Inicializa los atributos del evento.
        self.fecha = fecha
        self.lugar = lugar
        self.num_asistentes = num_asistentes
        self.servicios = servicios

    def mostrar_informacion(self):
        # Muestra la información básica del evento.
        print(f"Fecha: {self.fecha}")
        print(f"Lugar: {self.lugar}")
        print(f"Número de asistentes: {self.num_asistentes}")
        print(f"Servicios: {', '.join(self.servicios)}")

class Boda(Evento):
    def __init__(self, fecha, lugar, num_asistentes, servicios, nombre_novios):
        # Inicializa los atributos de una boda, incluyendo los novios.
        super().__init__(fecha, lugar, num_asistentes, servicios)
        self.nombre_novios = nombre_novios

    def mostrar_informacion(self):
        # Muestra la información específica de una boda.
        print(f"Evento: Boda")
        print(f"Nombres de los novios: {self.nombre_novios}")
        super().mostrar_informacion()

class Cumpleaños(Evento):
    def __init__(self, fecha, lugar, num_asistentes, servicios, nombre_cumpleanero, edad):
        # Inicializa los atributos de un cumpleaños, incluyendo el cumpleañero.
        super().__init__(fecha, lugar, num_asistentes, servicios)
        self.nombre_cumpleanero = nombre_cumpleanero
        self.edad = edad

    def mostrar_informacion(self):
        # Muestra la información específica de un cumpleaños.
        print(f"Evento: Cumpleaños")
        print(f"Nombre del cumpleañero: {self.nombre_cumpleanero}")
        print(f"Edad: {self.edad}")
        super().mostrar_informacion()

class Conferencia(Evento):
    def __init__(self, fecha, lugar, num_asistentes, servicios, tema, nombre_ponente):
        # Inicializa los atributos de una conferencia, incluyendo el tema y el ponente.
        super().__init__(fecha, lugar, num_asistentes, servicios)
        self.tema = tema
        self.nombre_ponente = nombre_ponente

    def mostrar_informacion(self):
        # Muestra la información específica de una conferencia.
        print(f"Evento: Conferencia")
        print(f"Tema: {self.tema}")
        print(f"Ponente: {self.nombre_ponente}")
        super().mostrar_informacion()

# Ejemplo de uso
print("Registro de eventos:")
tipo_evento = input("Ingrese el tipo de evento (Boda, Cumpleaños, Conferencia): ")

fecha = input("Ingrese la fecha del evento (DD/MM/AAAA): ")
lugar = input("Ingrese el lugar del evento: ")
num_asistentes = int(input("Ingrese el número de asistentes: "))
servicios = input("Ingrese los servicios requeridos (separados por comas): ").split(",")

if tipo_evento.lower() == "boda":
    nombre_novios = input("Ingrese los nombres de los novios: ")
    evento = Boda(fecha, lugar, num_asistentes, servicios, nombre_novios)
elif tipo_evento.lower() == "cumpleaños":
    nombre_cumpleanero = input("Ingrese el nombre del cumpleañero: ")
    edad = int(input("Ingrese la edad del cumpleañero: "))
    evento = Cumpleaños(fecha, lugar, num_asistentes, servicios, nombre_cumpleanero, edad)
elif tipo_evento.lower() == "conferencia":
    tema = input("Ingrese el tema de la conferencia: ")
    nombre_ponente = input("Ingrese el nombre del ponente: ")
    evento = Conferencia(fecha, lugar, num_asistentes, servicios, tema, nombre_ponente)
else:
    print("Tipo de evento no válido")
    exit()

print("\nInformación del evento registrado:")
evento.mostrar_informacion()
