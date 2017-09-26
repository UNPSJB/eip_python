from urllib import request
import bz2
import io

URLS_DATOS = [
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/811bf426-fc36-4f20-b2e1-59bdbb938153/download/nombres-1920-1924.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/6f108571-4bde-443c-8d5c-420437478267/download/nombres-1925-1929.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/0ef09d87-2b8c-4f54-8a2f-c088a988624d/download/nombres-1930-1934.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/87ee40f7-723e-4e08-bbd7-1777cedede69/download/nombres-1935-1939.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/da2b2195-e15c-4dc2-b35c-2465b8f14303/download/nombres-1940-1944.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/62a614da-5522-4b74-842e-9c73ac668f88/download/nombres-1945-1949.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/9f29cc91-4474-49ac-81a5-df999b1ee0fc/download/nombres-1950-1954.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/d95b5609-c55f-4772-bd9a-53dc88fc805a/download/nombres-1955-1959.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/38d176fe-6447-40e3-a2ce-ddd1a6fe8d62/download/nombres-1960-1964.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/54133680-1081-4db5-8e1d-a002c1fdb6f5/download/nombres-1965-1969.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/054a1f82-7304-4305-ba1c-2546befdd78e/download/nombres-1970-1974.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/41ef698a-b71c-4b25-b69f-ae12e30dc356/download/nombres-1975-1979.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/9fc0c3f6-061b-4e70-821c-1e860276b119/download/nombres-1980-1984.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/778842bb-4783-46fe-84ba-7dea0ea75736/download/nombres-1985-1989.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/fb029bfb-e587-47eb-bcf6-95ac0253f843/download/nombres-1990-1994.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/be63d92a-1c6f-4899-8883-994024877dc9/download/nombres-1995-1999.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/55eb9549-2be8-41ce-8c72-52ee789f6e01/download/nombres-2000-2004.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/2bc614ab-e044-4e49-94f6-b6e8cec02607/download/nombres-2005-2009.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/d7229d66-d2f1-4679-8fb5-568a5e8f6ab3/download/nombres-2010-2014.csv",
    "http://datos.gob.ar/dataset/b8418d41-8e0c-4e85-8aa8-80d51a840132/resource/9e1eca6c-4c58-4f22-8bd4-701fa16c9db0/download/nombres-2015.csv"
]


# obtener los datos de internet con urllib
def datos_web(url):
    datos_raw = []
    response = request.urlopen(url)
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

def datos_webs():
    datos = []
    for url in URLS_DATOS:
        datos.extend(datos_web(url))
    return datos

def datos_web_actual():
    return datos_web(URLS_DATOS[-1])

load_datos_raw = datos_in
