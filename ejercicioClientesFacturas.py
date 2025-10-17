from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellidos, id_fiscal):
        self._id_fiscal = id_fiscal
        self._nombre = nombre
        self._apellidos = apellidos

    @property 
    def id_fiscal(self):
        return self.id_fiscal

    @id_fiscal.setter
    def id_fiscal(self, value):
        self._id_fiscal.setter = value

    @property 
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self.nombre.setter = value

    @property
    def apellidos(self):
        return self._apellidos
    
    @apellidos.setter
    def apellidos(self, value):
        self.nombre.setter = value

    @staticmethod
    def metodo_estatico():
        return "este es un método estático"

    @abstractmethod
    def saludo(self):
        return f"Hola, mi nombre es {self.nombre} {self.apellidos}."
    

class Cliente(Persona):
    def __int__(self, nombre, apellidos, id_fiscal, id_cliente, email = None):
        super().__init__(nombre, apellidos, id_fiscal)
        self._id_cliente = id_cliente
        self._email = email
    
    @property
    def id_cliente(self):
        return self._id_fiscal
    
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        if id_cliente < 0:
            raise ValueError("El ID no puede ser negativo.")
        self.id_fiscal.setter = id_cliente
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self.email.setter = email


    def __del__(self):
        print(f"Ciente id: {self.id_cliente} eliminado.")

    def __str__(self):
        return f"{self.nombre} {self.apellidos}, ID: {self.id_cliente}"
    
    def saludo(self):
        return super().saludo() + f"Mi ID de cliente es {self.id_cliente}."

class Factura():
    def __init__ (self, id_factura, cliente: Cliente):
        self.id_factura = id_factura
        self.cliente = cliente
    
    def mostrar_detalle(self):
        print(f"Factura ID: {self.id_factura}, Cliente: {self.cliente}")

    def __eq__(self, other):
        if isinstance(other, Factura):
            return self
    