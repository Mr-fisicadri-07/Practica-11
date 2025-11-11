from animales import Animal

class AnimalesDomesticos(Animal): 
    
    def __init__(self, nombre, sonido):
    
        super().__init__(nombre, sonido)
        

class Perro(AnimalesDomesticos):
    
    def __init__(self, nombre, caracteristica="hacer pis", ubicacion="casa"):
    
        super().__init__(nombre, "Quería decir, guau guau")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Gato(AnimalesDomesticos):
    
    def __init__(self, nombre, caracteristica="arañar", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "Perdón, miau miau")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion


class Hamster(AnimalesDomesticos):
    
    def __init__(self, nombre, caracteristica="roer", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "quería decir *roe algo*")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Periquito(AnimalesDomesticos):
    
    def __init__(self, nombre, caracteristica="dar picotazos", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "perdón, pío pío")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Nemo(AnimalesDomesticos):
    
    def __init__(self, nombre, caracteristica="ser un payaso", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "quería decir, glugluglu")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion