
from .contar import contar_por_nombre 

def hay_mas_que(datos, nombre1, nombre2):
    return contar_por_nombre(datos, nombre1) >= contar_por_nombre(datos, nombre2)

def decir_que_hay_mas(datos, nombre1, nombre2):
    if hay_mas_que(datos, nombre1, nombre2):
        return nombre1
    elif hay_mas_que(datos, nombre2, nombre1):
        return nombre2