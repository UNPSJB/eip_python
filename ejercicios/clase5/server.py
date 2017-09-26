from datetime import datetime
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_restful_swagger import swagger

from funciones import filtrar
from modelo import Registro
import storage
import data_load

#REGISTROS = storage.recuperar_datos()
REGISTROS = [Registro.factory(tupla) for tupla in data_load.datos_web_actual()]

parser = reqparse.RequestParser()
parser.add_argument('nombre', required=True)
parser.add_argument('inicio', type=int)
parser.add_argument('fin', type=int)
parser.add_argument('anio', type=int)
parser.add_argument('search')

def to_dict(regs):
    return [r._asdict() for r in regs]

class Nombres(Resource):
    @swagger.operation()
    def get(self):
        filtros = []
        args = parser.parse_args()
        search = args["search"] or "canonico"
        nombre = args["nombre"]
        # Preparo filtros para pasar al filtrador
        if args["inicio"]:
            filtros.append(filtrar.FILTROS["inicio"](args["inicio"]))
        if args["fin"]:
            filtros.append(filtrar.FILTROS["fin"](args["fin"]))
        if args["anio"]:
            filtros.append(filtrar.FILTROS["anio"](args["anio"]))
        filtros.append(filtrar.FILTROS[search](nombre))
        nombres = filtrar.aplicar_filtros(REGISTROS, filtros)
        return to_dict(nombres)

    @swagger.operation(
        parameters=[
            {
              "name": "body",
              "required": True,
              "allowMultiple": False,
              "dataType": Registro.__name__,
              "paramType": "body"
            }
          ]
    )
    def post(self):
        args = parser.parse_args()
        nombre = args["nombre"]
        anio = args["anio"] or datetime.now().year
        filtros = [
            filtrar.FILTROS["nombre"](nombre),
            filtrar.FILTROS["anio"](anio)
        ]
        viejo = filtrar.obtener_uno(REGISTROS, filtros)
        if viejo is None:
            viejo = Registro.factory((nombre, 0, anio))
        else:
            REGISTROS.remove(viejo)
        nuevo = viejo._replace(cantidad=viejo.cantidad + 1)
        REGISTROS.append(nuevo)
        return nuevo._asdict(), 201

    @swagger.operation()
    def delete(self):
        args = parser.parse_args()
        nombre = args["nombre"]
        anio = args["anio"] or datetime.now().year
        filtros = [
            filtrar.FILTROS["nombre"](nombre),
            filtrar.FILTROS["anio"](anio)
        ]
        viejo = filtrar.obtener_uno(REGISTROS, filtros)
        if viejo is None:
            viejo = Registro.factory((nombre, 0, anio))
        else:
            REGISTROS.remove(viejo)
        nuevo = viejo._replace(cantidad=viejo.cantidad - 1)
        if nuevo.cantidad:
            REGISTROS.append(nuevo)
        return nuevo._asdict(), 201

def main():
    app = Flask(__name__)
    #api = Api(app)
    api = swagger.docs(Api(app), apiVersion='1')
    api.add_resource(Nombres, '/nombres/')
    app.run(debug=True)
    
if __name__ == '__main__':
    main()