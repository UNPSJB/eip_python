from urllib import request
import bz2
import io

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
    return datos_raw[1:]

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

load_datos_raw = datos_bz2
