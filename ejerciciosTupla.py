try:
    with 1,2,3 as mi_tupla:
        mi_tupla[1] = 0
except:
    TypeError
else:
    print("Tupla modificada")


tupla_mixta = (1, "dos", [3,4], {5: "cinco"}, (6,7), 8.0, True, None, {9})

tupla_mixta[2][0] = 6
print(tupla_mixta)

for elemento in tupla_mixta:
    print(f"{elemento} => {type(elemento)}")

tupla_mixta = (1, ["Hola", "Adiós"], True)

print(sorted(tupla_mixta))

