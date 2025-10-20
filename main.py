from pydantic import BaseModel
datos = {"nombre": "pepe", "edad": 45}

if not isinstance(datos["edad"], int):
    