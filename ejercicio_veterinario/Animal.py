from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, id_animal, nombre_duenio):
        self._especie = especie
        self._id_animal = id_animal
        self._nombre_duenio = nombre_duenio

    @property
    def especie(self):
        return self.especie
    
    @especie.setter
    def especie(self, especie):
        self.especie.setter= especie

    @property
    def nombre_duenio(self):
        return self.nombre_duenio

    @nombre_duenio.setter
    def nombre(self, nombre_duenio):
        self.nombre_duenio.setter= nombre_duenio

    @property
    def id_animal(self):
        return self.id_animal
    
    @id_animal.setter
    def id_animal(self, id_animal):
        self.id_animal.setter = id_animal
    

@abstractmethod
def decir_caracteristica(self):
    print(f"Soy un {self.especie} y me caracterizo por: ")