from pprint import pprint

from data_load import load_datos_raw
from modelo import convertir_dato_en_registro
from funciones.ordenar import ordenar_por_cantidad
from funciones import compara

# generamos nuestra propia lista de registros

#for d in datos:
#    if d.nombre == 'Milo' and d.anio > 1990 :
#        pass

#r = []
#for d in datos:
#    if d.nombre =='Thiago' and d.anio > 1960 :
#        r.append(d)


def main():
    datos = [convertir_dato_en_registro(tupla) for tupla in load_datos_raw()]
    pprint([(r.primer_nombre, r.genero) for r in datos])

if __name__ == '__main__':
    main()