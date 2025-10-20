from pydantic import BaseModel, constr, conint, EmailStr, field_validator

class Persona(BaseModel):
    nombre: constr(min_length=3, max_length=20) 
    
    edad: conint(ge=0, le=120) 
    email: EmailStr

p= Persona(nombre="Pepe", edad="cincuenta")

print(p.model_dum())
print(p.edad)

@field_validator("nombre")
#cls: clase v:valor
def nombre_mayusculas(cls, v):
    return v.title()

p = Persona(nombre="Juan Carlos" edad =30)
p.nombre #Juan Carlos

