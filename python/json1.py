#import json , no sería necesario, Python3 ya tiene por defecto esta librería.


#Lista con varios diccionarios como elementos de la lista
pedidos = [
    {"numero": 1, "cliente": "Juan Pérez", "productos": [{"nombre": "Café", "precio": 250, "cantidad": 2}], "estado": "pendiente"},
    {"numero": 2, "cliente": "María López", "productos": [{"nombre": "Té", "precio": 200, "cantidad": 1}], "estado": "en preparación"}
]

# Guardar en un archivo JSON
with open("pedidos.json", "w") as archivo:
    json.dump(pedidos, archivo, indent=4)  # indent=4 para mejor legibilidad
