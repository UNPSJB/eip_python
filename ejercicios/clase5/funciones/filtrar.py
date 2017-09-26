import unicodedata
from functools import reduce

from Levenshtein import ratio

def to_canonico(string):
    return ''.join((c for c in unicodedata.normalize('NFD', string.lower()) if unicodedata.category(c) != 'Mn'))

def inicio_func(anio):
    def _inicio(reg):
        return reg.anio >= anio
    return _inicio

def fin_func(anio):
    def _fin(reg):
        return reg.anio <= anio
    return _fin

def anio_func(anio):
    def _anio(reg):
        return reg.anio == anio
    return _anio

def levenshtein_func(nombre):
    def _levenshtein(reg):
        return ratio(to_canonico(reg.nombre), to_canonico(nombre)) > 0.9
    return _levenshtein

def canonico_func(nombre):
    def _canonico(reg):
        return reg.canonico == to_canonico(nombre)
    return _canonico

def nombre_func(nombre):
    def _nombre(reg):
        return reg.nombre == nombre
    return _nombre

def true_func(reg):
    return True

def and_func(f1, f2):
    def _and(reg):
        return f1(reg) and f2(reg)
    return _and

def or_func(f1, f2):
    def _or(reg):
        return f1(reg) and f2(reg)
    return _or

FILTROS = {
    "inicio": inicio_func,
    "fin": fin_func,
    "anio": anio_func,
    "levenshtein": levenshtein_func,
    "canonico": canonico_func,
    "nombre": nombre_func
    # Se pueden continuar creando y agregando funciones y todo funciona :)
    # ej regex, startswith, endswith
}

def aplicar_filtros(datos, filtros):
    filtro = reduce(lambda a, f: and_func(a, f), filtros, true_func)
    return [ r for r in datos if filtro(r) ]

def obtener_uno(datos, filtros):
    datos = aplicar_filtros(datos, filtros)
    if datos:
        return datos.pop(0)