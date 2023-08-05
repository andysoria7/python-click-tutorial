import json
import os

# Funcion que permite leer un json.
def read_json():
    # Si no existe el archivo data.json, entonces lo crea.
    if not os.path.isfile('data.json'):
        with open('data.json', 'w') as f:
            json.dump([], f)
    # Caso contrario solamente lo lee.
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data
    
# Funcion que permite colocar datos en el json.
def write_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f) # json.dump va a tomar los datos y va a reescribirlos dentro del archivo.