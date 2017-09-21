from pprint import pprint

from data_load import load_datos_raw
from modelo import convertir_dato_en_registro
from funciones import ordenar, compara
import storage

# generamos nuestra propia lista de registros

#for d in datos:
#    if d.nombre == 'Milo' and d.anio > 1990 :
#        pass

#r = []
#for d in datos:
#    if d.nombre =='Thiago' and d.anio > 1960 :
#        r.append(d)


def main():
    #datosbz = [convertir_dato_en_registro(tupla) for tupla in load_datos_raw()]
    #pprint(datos)
    #pprint([(r.primer_nombre, r.genero) for r in datos])
    #datos = storage.recuperar_datos()
    #print("listos los datos")
    #nombre = compara.decir_que_hay_mas(datos, "Juan Carlos", "Juan Pablo")
    #print(len(datos), nombre)
    #storage.guardar_datos(datos)
    #pprint([type(r) for r in datos])

if __name__ == '__main__':
    main()