from collections import namedtuple

RegistroTupla = namedtuple('Registro', 'nombre cantidad anio genero')

class Registro(RegistroTupla):
    def __new__(cls, *args, **kwargs):
        if len(args) == 3:
            args = args + ("",)
        return RegistroTupla.__new__(cls, *args, **kwargs)
    
    def _nombre(self, n):
        try:
            return self.nombre.split()[n]
        except:
            return ""

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