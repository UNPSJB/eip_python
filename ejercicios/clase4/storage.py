import pickle

ARCHIVO = "datos.pkl"

def guardar_datos(datos):
    with open(ARCHIVO, "wb") as f:
        pickle.dump(datos, f)

def recuperar_datos():
    with open(ARCHIVO, "rb") as f:
        datos = pickle.load(f)
    return datos