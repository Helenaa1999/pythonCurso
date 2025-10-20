from ejercicio_veterinario import Animal

class Gato(Animal):
    def __init__ (self, especie, id_animal, nombre_duenio, raza):
        super.__init__(especie, id_animal, id_animal, nombre_duenio)
        self._raza = raza

    @property
    def raza(self):
        return self.raza

    @raza.setter
    def raza(self, raza):
        self.raza.setter = raza


    def decir_caracteristica(self):
        print(f"{self.super} ser cariñoso con mis dueños")