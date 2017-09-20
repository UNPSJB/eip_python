from collections import namedtuple

#Registro = namedtuple('Registro', 'nombre cantidad anio')

def es_de_varon(nombre):
    return (nombre.endswith('o') or \
        nombre.endswith("el") or \
        nombre.endswith("or")) and \
        not nombre.endswith("aro")

class Registro():
    def __init__(self, nombre, cantidad, anio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.anio = anio

    def _nombre(self, n):
        try:
            return self.nombre.split()[n]
        except:
            return ""

    @property
    def genero(self):
        return es_de_varon(self.primer_nombre) and "M" or "F"

    @property
    def primer_nombre(self):
        return self._nombre(0)

    @property
    def segundo_nombre(self):
        return self._nombre(1)

def convertir_dato_en_registro(tupla):
    nombre, cantidad, anio = tupla
    nombre = nombre.strip()
    cantidad = int(cantidad)
    anio = int(anio)
    return Registro(nombre, cantidad, anio)