from datetime import datetime


def edad_en_dias(fecha_de_nacimiento):
    ahora = datetime.now()
    edad = ahora - fecha_de_nacimiento
    return edad.days

if __name__ == "__main__":
    import sys
    fecha = datetime(
        int(sys.argv[1]),
        int(sys.argv[2]),
        int(sys.argv[3])
    )
    print(edad_en_dias(fecha))
