
# Contar Cantidad de personas con un nombre dado y compararlo con otro
def contar_por_nombre(datos, nombre):
    r = []
    for d in datos:
        if d.nombre == nombre:
            r.append(d.cantidad)
    return sum(r)