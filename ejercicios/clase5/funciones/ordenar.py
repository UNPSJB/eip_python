# Ordenamos por cantidad
def ordenar_por_cantidad(datos, asc=True):
    return sorted(datos, key=lambda r: r.cantidad, reverse=asc)