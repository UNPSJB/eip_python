from urllib import request
from collections import namedtuple
from pprint import pprint
import bz2
import io

Registro = namedtuple('Registro', 'nombre cantidad anio')

URL_DATOS = 'http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/9e1eca6c-4c58-4f22-8bd4-701fa16c9db0/download/nombres-2015.csv'

# obtener los datos de internet con urllib
def datos_web():
    datos_raw = []
    response = request.urlopen(URL_DATOS)
    for linea in response:
        linea = linea.decode('utf-8').strip()
        slinea = tuple(linea.split(','))
        if len(slinea) != 3:
            continue
        datos_raw.append(slinea)
    return datos_raw

# obtener datos de un archivo comprimido con bz2
def datos_bz2():
    datos_raw = []
    with bz2.BZ2File("./nombres_corto.csv.bz2", 'rb') as input:
        with io.TextIOWrapper(input, encoding='utf-8') as dec:        
            for linea in dec.readlines():
                slinea = tuple(linea.strip().split(','))
                if len(slinea) != 3:
                    continue
                datos_raw.append(slinea)
    return datos_raw

# datos crudos
def datos_in():
    datos_raw = [
        ('nombre', 'cantidad', 'anio'),
        ('Valentino', '2340', '2015'),
        ('Santino', '1893', '2015'),
        ('Guadalupe', '1392', '2015'),
        ('Thiago ', '1116', '2015'),
        ('Salvador', '904', '2015'),
        ('Milo', '786', '2015'),
        ('Maria Emilia', '690', '2015'),
        ('Amparo', '580', '2015'),
        ('María Victoria', '517', '2015')
    ]
    return datos_raw

datos_raw = datos_bz2()

# están en crudo
print("-" * 10, end=" "); print("Datos Crudos", end=" "); print("-" * 10)
print("Cantidad de tuplas", len(datos_raw))
pprint(datos_raw[:15])

# generamos nuestra propia lista de registros
datos = []

def convertir_dato_en_registro(tupla):
    nombre, cantidad, anio = tupla
    nombre = nombre.strip()
    cantidad = int(cantidad)
    anio = int(anio)
    return Registro(nombre, cantidad, anio)

for lst in datos_raw[1:]:
    datos.append(convertir_dato_en_registro(lst))
    
# liberamos memoria!
del(datos_raw)

print("-" * 10, end=" "); print("Registros", end=" "); print("-" * 10)
pprint(datos[:15])

print("-" * 10, end=" "); print("Datos de los registros", end=" "); print("-" * 10)
print("Nombre", datos[10].nombre)
print("Cantidad", datos[10].cantidad)
print("Anio", datos[10].anio)

print("-" * 10, end=" "); print("Consulta existencial", end=" "); print("-" * 10)
for d in datos:
    if d.nombre == 'Milo' and d.anio > 1990 :
        print(d)

print("-" * 10, end=" "); print("Consulta cantidad", end=" "); print("-" * 10)
r = []
for d in datos:
    if d.nombre =='Thiago' and d.anio > 1960 :
        r.append(d)
print ('{} registros'.format(len(r)))

# Contar Cantidad de personas con un nombre dado y compararlo con otro
def cantidad_de(nombre):
    r = []
    for d in datos:
        if d.nombre == nombre:
            r.append(d.cantidad)
    return sum(r)

def hay_mas_que(nombre1, nombre2):
    return cantidad_de(nombre1) > cantidad_de(nombre2)

def decir_que_hay_mas(nombre1, nombre2):
    if hay_mas_que(nombre1, nombre2):
        print('Hay mas ', nombre1)
    elif hay_mas_que(nombre2, nombre1):
        print('Hay mas ', nombre2)

decir_que_hay_mas('Miguel', 'Estela')

# Ordenamos por cantidad
print("-" * 10, end=" "); print("Ordenados por cantidad decreciente", end=" "); print("-" * 10)
ordenados = sorted(datos, key=lambda r: r.cantidad, reverse=True)
pprint(ordenados[:15])
