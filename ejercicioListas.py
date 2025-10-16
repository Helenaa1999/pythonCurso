import copy

empleados= [
    ["Pedro", ["Python", "SQL"]],
    ["Manolo", ["Java", "C++", "JavaScript"]],
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
]
print(empleados)
copia_superficial = empleados.copy()

copia_profunda = copy.deepcopy(empleados)

copia_superficial[0][1].insert(2, "JavaScript")
copia_profunda[0][1].insert(2, "JavaScript")
print(copia_superficial)
print(empleados)
print(copia_profunda)

copia_profunda[-1][-1].insert(3, "Java")

empleado_nuevo = ["Juan", ["Node.js", "redis"]]
copia_profunda.append(empleado_nuevo)

print(copia_profunda)
