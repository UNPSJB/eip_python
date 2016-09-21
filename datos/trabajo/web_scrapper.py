#!/usr/bin/python
# "Matias Iglesias"
# "Copyright (C) 2015 Matias Iglesias"
# "Public Domain"
# "1.0"

# 1. Ejecutar el script
# 1. Leer e interpetar el codigo buscar en la ayuda respectiva
# 1. Este script funciona en python 2 pero no en python 3, descomentar
# todos los prints de debug y arreglar los que correspondan para que funcionen
# en python 3
# 1. Implementar los TODO y los FIXME
# 1. Mejorar el bloque try except de la funcion scrapp_source, identificar y
# trabajar solo sobre los posibles puntos de falla no sobre todo el bloque de 
# la funcion
# 1. La funcion scrapp_source, toma dos caminos alternos para cada url 
# dependiendo del tipo de url que es, identificar esos caminos e implementarlos
# como funcion
# 1. Modularizar el codigo creando los modulos y/o paquetes correspondientes para
# separar la logica de manejar archivos (leer y escribir) y la de obtener urls
# posteriormente crear main.py y trabajar con los modulos y/o paquetes obtenidos.

import re
import sys
import urllib.request
from urllib.error import HTTPError, URLError

ARCHIVO_FUENTES = "fuentes.txt"


def obtener_fuentes():
    # TODO: Manejar el archivo en un bloque with
    f = open(ARCHIVO_FUENTES, "r")
    # TODO: Usar readlines del objeto file
    fuentes = f.read().splitlines(False)
    f.close()
    return fuentes


def scrapp_source(source, search_for, depth=1):
    # print("Abro URL: " + source + " Profundidad: " + str(depth))
    try:
        # TODO: Manejar el request en un bloque with
        f = urllib.request.urlopen(source)
        #print f.read()
        urls = obtener_urls(f.read().decode("utf-8"))
        for url in urls:
            match = re.search(r'\/', url)
            if match and url != "/":
                #print url + " es un directorio"
                if depth > 1:
                    # print("Busco recursivamente en " + source + " subidrectorio " + url)
                    scrapp_source(source + url, search_for, depth - 1)
            else:
                #print url + " es un archivo"
                match = re.search(search_for.lower(), url.lower())
                if match:
                    # print("Bajo " + source + url)
                    # FIXME: file_tmp nunca es cerrado, manejar el request en un bloque with
                    file_tmp = urllib.request.urlopen(source + url)
                    # TODO: Manejar el request en un bloque with
                    local_file = open(url, "wb")
                    local_file.write(file_tmp.read())
                    local_file.close()
        f.close()
        #print urls
    except HTTPError as e:
        print("Ocurrio un error")
        print(e.code)
    except URLError as e:
        print("Ocurrio un error")
        print(e.reason)


def obtener_urls(http):
    # print("HTTP Crudo " + http)
    urls = re.findall(r'href=[\'"]?([^\'" >]+)', http)
    return urls

depth = 1
search_for = None

# TODO: Agregar el bloque if __name__ == '__main__': para trabajar con este 
# script de manera mas limpia ver http://www.artima.com/weblogs/viewpost.jsp?thread=4829

try:
    search_for = sys.argv[1]
    depth = int(sys.argv[2])
except IndexError as ex:
    if search_for is None:
        print("""\
Uso: python web_scrapper.py search [depth]""")
except ValueError as ex:
    print("""\
Uso: python web_scrapper.py search [depth]
depth debe ser un entero""")

if search_for is not None:
    fuentes = obtener_fuentes()
    # print fuentes
    for fuente in fuentes:
        # print("Scrappeo " + fuente)
        scrapp_source(fuente, search_for, depth)
