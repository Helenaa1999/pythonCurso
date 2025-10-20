from pydantic import BaseModel, Field, Validator
from fastapi import FastAPIfrom schemas 
import GatoIn, PerroIn, VeterinarioInfrom domain 
import Gato, Veterinario

app = FastAPI(title="Veterinaria Simple API")
GATOS = []
PERROS = []
VETS = []

@app.post("/gatos")
def crear_gato(gato: GatoIn):
    nuevo = Gato(gato.id_, gato.nombre, gato.peso)
    GATOS.append(nuevo)
    return {"mensaje": f"Gato {nuevo.nombre} registrado", "total": len(GATOS)}


@app.post("/veterinarios")
def crear_veterinario(vet: VeterinarioIn):
    nuevo = Veterinario(vet.nombre)
    VETS.append(nuevo)
    return {"mensaje": f"Veterinario {nuevo.nombre} añadido", "total": len(VETS)}

@app.get("/animales/total")
def total_animales():
    from domain import AnimalDomestico
    return {"total_animales": AnimalDomestico.total_animales()}

@app.post("/atender")
def atender(vet: VeterinarioIn, gato: GatoIn | None = None, perro: PerroIn | None = None):
    veterinario = Veterinario(vet.nombre)
    if gato:
        animal = Gato(gato.id_, gato.nombre, gato.peso)
    elif perro:
        animal = Perro(perro.id_, perro.nombre, perro.peso)
    else:
        return {"error": "Debe enviar un gato o un perro"}

    resultado = veterinario.atender(animal)
    return {"resultado": resultado}