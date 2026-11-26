
class Nodo:
    def __init__(self, nombre, hijos=None):
        self.nombre = nombre
        self.hijos = hijos if hijos is not None else []

    def mostrar(self, prefijo="", ultimo=True):
        print(prefijo + ("└── " if ultimo else "├── ")
              + str(self.nombre))

        prefijo += "    " if ultimo else "│   "

        for i, hijo in enumerate(self.hijos):
            hijo.mostrar(prefijo, i == len(self.hijos) - 1)
