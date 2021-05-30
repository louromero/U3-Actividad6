import abc
from abc import ABC

class Auto(ABC):
    __modelo=""
    __puertas=0
    __color=""
    __precioBase=0.00
    __marca=""

    def __init__(self,modelo,puertas,color,precioBase,marca):
        self.__modelo=modelo
        self.__puertas=puertas
        self.__color=color
        self.__precioBase=precioBase
        self.__marca=marca

    def getModelo(self):
        return self.__modelo

    def getPuertas(self):
        return self.__puertas

    def getColor(self):
        return self.__color

    def getPrecioBase(self):
        return self.__precioBase

    def getMarca(self):
        return self.__marca

    def setPrecioBase(self,precioNuevo):
        self.__precioBase=precioNuevo


    def __str__(self):
        precioB="{:.2f}".format(self.getPrecioBase())
        cadena ="\n {:<12} {:<12} {:<10} {:<10} ${:<12} ".format(self.getMarca()[0:12].title(),self.getModelo()[0:12].title(),self.getPuertas(),self.getColor()[0:12].title(),precioB)
        return cadena

    @abc.abstractclassmethod
    def getImporteVenta(self):
        pass

    @abc.abstractclassmethod
    def toJson(self):
        pass