#!/usr/bin/python
# "Matias Iglesias"
# "Copyright (C) 2015 Matias Iglesias"
# "Public Domain"
# "1.0"

import argparse
import urllib.request
from urllib.error import HTTPError, URLError
import re
#import sys

#print sys.argv

ARCHIVO_FUENTES = "fuentes.txt"

parser = argparse.ArgumentParser(description='Web Scrapper')
parser.add_argument('-d', '--depth', type=int, default=1, required=False,
                    help='Depth. Profundidad de la busqueda (default: 1)')
parser.add_argument('-s', '--search_for', type=str, required=True,
                    help='String a buscar')

args = parser.parse_args()
#print args.accumulate(args.integers)


def obtener_fuentes():
    f = open(ARCHIVO_FUENTES, "r")
    #fuentes = []
    fuentes = f.read().splitlines(False)
    f.close()
    return fuentes


def scrapp_source(source, search_for, depth=1):
    print("Abro URL: " + source + " Profundidad: " + str(depth))
    try:
        f = urllib.request.urlopen(source)
        #print f.read()
        urls = obtener_urls(f.read().decode("utf-8"))
        for url in urls:
            match = re.search(r'\/', url)
            if match and url != "/":
                #print url + " es un directorio"
                if depth > 1:
                    print("Busco recursivamente en " + source + " subidrectorio " + url)
                    scrapp_source(source + url, search_for, depth - 1)
            else:
                #print url + " es un archivo"
                match = re.search(search_for.lower(), url.lower())
                if match:
                    print("Bajo " + source + url)
                    file_tmp = urllib.request.urlopen(source + url)
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


fuentes = obtener_fuentes()
#print fuentes
for fuente in fuentes:
    # print("Scrappeo " + fuente)
    scrapp_source(fuente, args.search_for, args.depth)
