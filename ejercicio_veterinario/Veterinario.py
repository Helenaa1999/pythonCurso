from abc import ABC

class Veterinario (ABC):
    def __init__ (self, nombre, id_veterinario):
        self._nombre = nombre
        self._id_veterinario = id_veterinario

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre.setter = nombre

    @property
    def id_veterinario(self):
        return self.id_veterinario
    
    @id_veterinario.setter
    def id_veterinario(self, id_veterinario):
        self.id_veterinario.setter = id_veterinario


    