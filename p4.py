producto = {
    "nombre": "Fabuloso",
    "marca": "Maestro Limpio",
    "descripcion": "Limpiador de pisos",
    "costo": 15
}

producto["codigo_barras"] = "ABC123"

'''print(producto)'''
print('-------------------------------------------')
import random

puntos = []

for i in range(10):
    p = {
        "x": random.uniform(-10, 10),
        "y": random.uniform(-10, 10)
    }
    puntos.append(p)

'''print(puntos)'''
print('-------------------------------------------')
def T(p):
    d = ((p["x"] - 1) ** 2 + (p["y"] - 2) ** 2) ** 0.5
    nx = p["x"] < 0
    return {
        "x": p["x"],
        "y": p["y"],
        "d": d,
        "nx": nx
    }

puntos_ext = map(T, puntos)

'''print(list(puntos_ext))'''
print('-------------------------------------------0')
filtro1 = []
filtro2 = []

for p in puntos_ext:
    if p["d"] < 2:
        filtro1.append(p)
    if p["nx"]:
        filtro2.append(p)

print(filtro1)
print('-------------------------------------------1')
print(filtro2)
print('-------------------------------------------2')
## FORMA FÁCIL

filtro1 = []
filtro2 = []

for p in puntos:
    x = p["x"]
    y = p["y"]

    d = ((x - 1) ** 2 + (y - 2) ** 2) ** 0.5

    if d < 2:
        filtro1.append(p)

for p in puntos:
    x = p["x"]

    if x < 0:
        filtro2.append(p)