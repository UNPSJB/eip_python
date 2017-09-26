from collections import namedtuple
import unicodedata
from funciones import metaphone

RegistroTupla = namedtuple('Registro', 'nombre cantidad anio genero')

Phonetic = metaphone.PhoneticAlgorithmsES()

class Registro(RegistroTupla):
    def __new__(cls, *args, **kwargs):
        if len(args) == 3:
            args = args + ("", )
        return RegistroTupla.__new__(cls, *args, **kwargs)
    
    def _nombre(self, n):
        try:
            return self.nombre.split()[n]
        except:
            return ""

    @property
    def metaphone(self):
        return Phonetic.metaphone(self.primero)

    @property
    def canonico(self):
        return ''.join((c for c in unicodedata.normalize('NFD', self.primero.lower()) if unicodedata.category(c) != 'Mn'))

    @property
    def primero(self):
        return self._nombre(0)

    @property
    def segundo(self):
        return self._nombre(1)

    @property
    def tercero(self):
        return self._nombre(2)
    
    @property
    def cuarto(self):
        return self._nombre(3)

    @property
    def quinto(self):
        return self._nombre(4)

    @staticmethod
    def factory(tupla):
        nombre, cantidad, anio = tupla
        nombre = nombre.strip()
        cantidad = int(cantidad)
        anio = int(anio)
        return Registro(nombre, cantidad, anio)