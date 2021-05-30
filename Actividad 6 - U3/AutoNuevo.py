from Auto import Auto

class AutoNuevo(Auto):
    __version=""

    def __init__(self,modelo,puertas,color,precioBase,marca,version):
        super().__init__(modelo,puertas,color,precioBase,marca)
        self.__version=version

    def getVersion(self):
        return self.__version

    def getImporteVenta(self):
        aux=0
        if self.__version=='full':
            aux=0.02
        aux+=1.10
        total=super().getPrecioBase()*aux
        return total

    def __str__(self):
        cadena = super().__str__()
        importe = "{:.2f}".format(self.getImporteV())
        cadena += ("${:<12} |".format(importe))
        return cadena

    #JSON
    def toJson(self):

        d = dict(__class__ = self.__class__.__name__,
                 __atributos__ = dict(
                     modelo  = super().getModelo(),
                     puertas = super().getPuertas(),
                     color   = super().getColor(),
                     precioB = super().getPrecioBase(),
                     marca   = super().getMarca(),
                     version = self.getVersion()

                 ))
        return d