from datetime import date
from Auto import Auto

class AutoUsado(Auto):
    __patente=""
    __anio=0
    __kilometraje=0

    def __init__(self,modelo,puertas,color,precioBase,marca,patente,anio,kilometraje):
        super().__init__(modelo,puertas,color,precioBase,marca)
        self.__patente=patente
        self.__anio=anio
        self.__kilometraje=kilometraje

    def getPatente(self):
        return self.__patente

    def getAnio(self):
        return self.__anio

    def getKilometraje(self):
        return self.__kilometraje

    def getImporteVenta(self):
        aux=0
        if self.getKilometraje()>1000000:
            aux=0.02
        antiguedad=self.getAntiguedad()
        auxiliar=antiguedad/100
        total=super().getPrecioBase()*(1-(aux+auxiliar))
        return total

    def getAntiguedad(self):
        hoy=date.today()
        antiguedad=hoy.year - self.__anio
        return antiguedad

    def setPrecioBase(self,nuevoPrecio):
        super().setPrecioBase(nuevoPrecio)
        print("Precio de venta: ${:.2f}".format(self.getImporteVenta()))


    def __str__(self):
        cadena= super().__str__()
        importe=  "{:.2f}".format(self.getImporteVenta())
        cadena += ("${:<12} |".format(importe))
        return cadena

    def toJson(self):

        d = dict(__class__ = self.__class__.__name__,
                 __atributos__ = dict(
                     modelo      = super().getModelo(),
                     puertas     = super().getPuertas(),
                     color       = super().getColor(),
                     precioB     = super().getPrecioBase(),
                     marca       = super().getMarca(),
                     patente     = self.getPatente(),
                     anio        = self.__anio,
                     kilometraje = self.getKilometraje()
                 ))
        return d