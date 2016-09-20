from datetime import datetime

def edad_en_dias(fecha_de_nacimiento):
    ahora = datetime.now()
    edad = ahora - fecha_de_nacimiento
    return edad.days

def f():
    pass
