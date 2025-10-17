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
            return self.id_factura == other.id_factura and self.cliente == other.cliente
        return False
    
    @property
    def id_factura(self):
        return self.id_factura

    @id_factura.setter
    def id_factura(self, id_factura):
        self.id_factura = id_factura

    @property
    def cliente(self):
        return self.cliente
    
    

if __name__ == "__main__":
    mi_cliente = Cliente("4332542F", "Juan", "Pérez",
                         12342, "juan.perez@example.com")
    instancia1 = Cliente("4333242F", "Pedro", "Pérez",
                         12343, "jpedro@example.com")
    
    Cliente.mostrar_numero_de_instancias()
    instancia2 = Cliente("43397442F", "Pepe", "Pérez",
                         1249783, "jpepe@example.com")
    Cliente.mostrar_numero_de_instancias()
    instancia3 = Cliente("4343242F", "Carlos", "Pérez",
                         12453, "jcarlos@example.com")
    
    instancia3.id_cliente = 443
    Cliente.mostrar_numero_de_instancia()

    factura1 = Factura("FAC001", mi_cliente)
    factura2 = Factura("FAC001", mi_cliente)

    if(factura1 == factura2):
        print("Las facturas son las mismas.")
    else:
        print("Las facturas son distintas")

    factura1.mostrar_detalle()
    print(factura1)

    miset = {factura1, factura2}
    print(miset)

    