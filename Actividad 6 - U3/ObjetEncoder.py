import json
from pathlib import Path

class ObjectEncoder:
    def guardarJSONarchivo(self,diccionario,archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
        destino.close()