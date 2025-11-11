from animales import Animal

class Animales_Domesticos(Animal): 
    
    def __init__(self, nombre, sonido):
    
        super().__init__(nombre, sonido)
        

class Perro(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="hacer pis", ubicacion="casa"):
    
        super().__init__(nombre, "Quería decir, guau guau")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Gato(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="arañar", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "Perdón, miau miau")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion


class Hamster(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="roer", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "quería decir *roe algo*")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Periquito(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="dar picotazos", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "perdón, pío pío")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Nemo(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="ser un payaso", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "quería decir, glugluglu")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion