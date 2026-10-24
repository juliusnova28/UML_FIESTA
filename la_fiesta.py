
class Invitacion:
    def __init__(self):
        self.codigo = ""

class Invitado:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.curso = ""
        self.invitacion = None  

class Presopuesto:
    def __init__(self):
        self.costo_del_alimento = 0
        self.costo_de_la_bebida = 0
        self.costo_total = 0


class Producto:
    def __init__(self):
        self.nombre = ""
        self.precio = 0
        self.cantidad = 0


class Consumo:
    def __init__(self):
        self.cantidad = 0
        self.invitado = None 
        self.producto = None 