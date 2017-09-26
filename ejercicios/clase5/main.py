from pprint import pprint
import random

from data_load import load_datos_raw
from modelo import Registro
from funciones import ordenar, compara, gender
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
    #datosweb = [Registro.factory(tupla) for tupla in load_datos_raw()]
    #pprint(datos)
    #pprint([(r.primer_nombre, r.genero) for r in datos])
    datos = storage.recuperar_datos()
    r = random.choice(datos)
    g = gender.get_genders(r.primero)
    print(r, g)
    print(r._asdict())
    for r in datos:
        print(r.metaphone, g)
    #print("listos los datos")
    #nombre = compara.decir_que_hay_mas(datos, "Juan Carlos", "Juan Pablo")
    #print(len(datos), nombre)
    #datos = list(set(datosweb + datosrec))
    #storage.guardar_datos(datos)
    #pprint([type(r) for r in datos])

if __name__ == '__main__':
    main()