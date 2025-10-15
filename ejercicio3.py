"""normalizamos un nombre propio y extraemos iniciales."""

nombre_completo = " Ana MARÍA López "
partes_normalizadas =  []

#Elimina los huecos de delante y detrás
nombre_sin_espacios = nombre_completo.strip()

#Divide en partes
partes = nombre_sin_espacios.split()

for palabra in partes: 
    #Primero se pone todas las palabras en minúsculas y después solo la primera letra de cada palabra
    palabra_normalizada = palabra.lower().capitalize()
    partes_normalizadas.append(palabra_normalizada)

normalizado = " ".join(partes_normalizadas)

iniciales_lista = []
for palabra in partes_normalizadas:
    inicial = palabra[0]
    iniciales_lista.append(inicial)

iniciales = ".".join(iniciales_lista)

assert normalizado == "Ana María López"
assert iniciales == "A.M.L"

print("OK: ej2")