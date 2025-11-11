from animales import Animal

class AnimalesGranja(Animal):
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)

class Vaca(AnimalesGranja):
    def __init__(self, nombre, caracteristica="dar leche", ubicacion="granja"):
        super().__init__(nombre, "Muu")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Cerdo(AnimalesGranja):
    def __init__(self, nombre, caracteristica="revolcarse en el lodo", ubicacion="granja"):
        super().__init__(nombre, "Oink")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Oveja(AnimalesGranja):
    def __init__(self, nombre, caracteristica="se esquila", ubicacion="granja"):
        super().__init__(nombre, "Bee")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Gallo(AnimalesGranja):
    def __init__(self, nombre, caracteristica="cantar al amanecer", ubicacion="granja"):
        super().__init__(nombre, "kikiriki")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Cabra(AnimalesGranja):
    def __init__(self, nombre, caracteristica="trepar", ubicacion="granja"):
        super().__init__(nombre, "Baaaaaaa")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion