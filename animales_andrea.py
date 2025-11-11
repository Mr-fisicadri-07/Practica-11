from animales import Animal

class AnimalesMarinos(Animal): 
    """
    Clase intermedia. DEBE aceptar los argumentos de sus hijos
    y pasarlos a su padre (Animal).
    """
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)


class Delfin(AnimalesMarinos):
    
    def __init__(self, nombre, caracteristica="hacer acrobacias", ubicacion="océano abierto"):
        super().__init__(nombre, "Quería decir, iiiiiii")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion


class Tiburon(AnimalesMarinos):
    
    def __init__(self, nombre, caracteristica="asustar bañistas sin querer", ubicacion="aguas profundas"):
        super().__init__(nombre, "Quería decir, ñam ñam... es broma, casi siempre")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion


class Pulpo(AnimalesMarinos):
    
    def __init__(self, nombre, caracteristica="hacer multitarea con 8 brazos", ubicacion="roca del fondo marino"):
        super().__init__(nombre, "Quería decir, glub glub mientras lo agarro todo")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion


class Medusa(AnimalesMarinos):
    
    def __init__(self, nombre, caracteristica="picar por accidente", ubicacion="superficie del mar"):
        super().__init__(nombre, "Quería decir, brillo y doy toques eléctricos")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion


class PezGlobo(AnimalesMarinos):
    
    def __init__(self, nombre, caracteristica="ser un globito :)", ubicacion="arrecife de coral"):
        super().__init__(nombre, "Me inflo, me desinflo")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion


class CaballitoDeMar(AnimalesMarinos):
    
    def __init__(self, nombre, caracteristica="flotar con estilo", ubicacion="praderas de algas"):
        super().__init__(nombre, "Quería decir, trot trot pero debajo del agua")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion


class EstrellaDeMar(AnimalesMarinos):
    
    def __init__(self, nombre, caracteristica="no hacer nada pero posar bien", ubicacion="arena del fondo"):
        super().__init__(nombre, "Quería decir, soy silenciosa pero importante en las fotos")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion