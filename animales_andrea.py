class Animal:
    """Clase base que almacena el nombre y el sonido."""
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido


class Animales_Marinos(Animal): 
    """
    Clase intermedia. DEBE aceptar los argumentos de sus hijos
    y pasarlos a su padre (Animal).
    """
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)


class Delfin(Animales_Marinos):
    def __init__(self):
        super().__init__(
            "Soy un delfín influencer",
            "Perdón, quise decir: iiiiiii (sígueme en Insta)"
        )


class Tiburon(Animales_Marinos):
    def __init__(self):
        super().__init__(
            "Soy un tiburón mal entendido",
            "Quería decir: ñam ñam... digo, 'solo soy incomprendido'"
        )


class Pulpo(Animales_Marinos):
    def __init__(self):
        super().__init__(
            "Soy un pulpo multitarea",
            "Perdón, estoy respondiendo 8 whatsapps a la vez"
        )


class Medusa(Animales_Marinos):
    def __init__(self):
        super().__init__(
            "Soy una medusa brillante",
            "Ups, no hablo, solo doy toques eléctricos"
        )


class PezPayaso(Animales_Marinos):
    def __init__(self):
        super().__init__(
            "Soy un pez payaso",
            "Quería decir: 'ríete por compromiso, por favor'"
        )
