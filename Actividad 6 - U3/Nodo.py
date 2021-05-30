class Nodo:
    __auto=None
    __siguiente=None

    def __init__(self,auto):
        self.__auto=auto

    def getSiguiente(self):
        return self.__siguiente

    def getAuto(self):
        return self.__auto

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente