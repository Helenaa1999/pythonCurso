"""Objetivo del Ejercicio: Dividir un texto de 1000 líneas en bloques de 25 líneas cada uno, identificar cada vez que se hayan 
acumulado 25 líneas y sea necesario almacenar el bloque actual antes de iniciar un nuevo bloque.
Descripción del Problema: Se requiere dividir un texto grande en varios segmentos donde cada segmento contenga 
exactamente 25 líneas. Este método implica el cálculo de índices y el uso de operaciones matemáticas para manejar 
adecuadamente la división en bloques.
Instrucciones:
Asumir que tienes un texto representado como una lista de strings, donde cada string es una línea del texto. Puedes generar 
este texto así (no preocupes ahora por la sintaxis, la veremos más adelante): 
# Simular un texto de 1000 líneas
texto_largo = ["Línea " + str(i + 1) for i in range(1000)]
1.Utilizar un bucle para iterar a través de todas las líneas del texto.
2.Determinar cada vez que se completen 25 líneas.
3.Almacenar cada conjunto de 25 líneas en una nueva lista, creando un bloque.
4.Guardar todos los bloques en una lista de listas"""


texto_largo = ["Línea " + str(i+1) for i in range(1000)]

bloques = []
bloque_actual = []

for index, linea in enumerate(texto_largo, start=1):
    bloque_actual.append(linea)

    if index % 25 == 0: 
        bloques.append(bloque_actual)
        bloque_actual = []

if bloque_actual:
    bloques.append(bloque_actual)

print(f"Total de bloques creados: {len(bloques)}")

for idx, bloque in enumerate(bloques[:2], start=1):
    print(f"\n === BLOQUE {idx} ===")
    for linea in bloque:
        print(f"{linea}")
