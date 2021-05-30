from sys import version
from Nodo import Nodo
from AutoNuevo import AutoNuevo
from AutoUsado import AutoUsado
from zope.interface import implementer

class Lista:
    __comienzo=None
    __actual=None
    __index=0
    __tope=0


    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__index=0
        self.__tope=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index==self.__tope:
            self.__actual=self.__comienzo
            self.__index=0
            raise StopIteration
        else:
            self.__index+=1
            dato=self.__actual.getAuto()

    def getTope(self):
        return self.__tope

    #CLAVE puede ser patente o posicion
    def getNoto(self,clave):
        band=False
        retorno=None
        #Posicion
        if type(clave)==int:
            if clave<self.__tope:
                while not band and self.__index<=self.__tope:
                    if clave==self.__index:
                        retorno=self.__actual.getAuto()
                        band=True
                    else:
                        self.__actual=self.__actual.getSiguiente()
                        self.__index+=1
        #PATENTE
        else:
            while not band and self.__index<self.__tope:
                dato=self.__actual.getAuto()
                if isinstance(dato,AutoUsado):
                    if dato.getPatente()==clave.lower():
                        retorno=dato
                        band=True
                self.__actual=self.__actual.getSiguiente()
                self.__index+=1
            if band==False:
                print("No encontrado.")
            else:
                print("Fue encontrado.")
            self.__actual=self.__comienzo
            self.__index=0
            return retorno

    def crearAuto(self):
        band=False
        retorno=None
        while not band:
            print("1. Auto Nuevo \n2. Auto Usado")
            try:
                op=int(input("\nIngrese opcion: "))
            except:
                print("\nOpcion erronea, intente de nuevo. ")
            else:
                band=op in [1,2]
                if not band:
                    print("\nOpcion erronea, intente de nuevo. ")
        modelo= input("Modelo: ")
        puertas=int(input("Cantidad de puertas: "))
        color=input("Color: ")
        precioBase=float(input("Precio base: "))
        
        if op==1:
            try:
                print("\nMarca Fiat")
                marca= 'Fiat'
                version=int(input("\nVersion del auto\n1. Base\n2.Full\nIngrese opcion: "))
                while version not in[1,2]:
                    print("\nError,intente de nuevo.")
                    version=int(input("\nVersion del auto\n1. Base\n2.Full\nIngrese opcion: "))
                if version==1:
                    version='base'
                else:
                    version='full'
                auto=AutoNuevo(modelo,puertas,color,precioBase,marca,version)
                retorno=auto
            except:
                print("Error en los datos agregados.")
        else:
            marca=input("\Marca: ")
            patente=input("Patente: ")
            anio=int(input("Anio: "))
            kilometraje=float(input("Kilometraje: "))
            auto=AutoUsado(modelo,puertas,color,precioBase,marca,patente,anio,kilometraje)
            retorno=auto
        return auto

    def insertar(self,posicion,elemento):
        band=False
        band2=False
        anterior=None
        if posicion>=self.__tope:
            print("\nPosicion fuera del alcance.")
            band2=True
        if band2==False:
            if posicion==0:
                band=True
                self.__tope+=1
                nuevoNodo=Nodo(elemento)
                if self.__comienzo==None:
                    self.__comienzo=nuevoNodo
                else:
                    nuevoNodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nuevoNodo
            else:
                anterior=self.__actual
                self.__actual=self.__actual.getSiguiente()
                self.__index+=1
            while not band and self.__index<self.__tope:
                if self.__index==posicion:
                    nuevoNodo=Nodo(elemento)
                    nuevoNodo.setSiguiente(self.__actual)
                    anterior.setSiguiente(nuevoNodo)
                    self.__tope+=1
                    band=True
                else:
                    anterior=self.__actual
                    self.__actual=self.__actual.getSiguiente()
                    self.__index+=1
        self.__actual=self.__comienzo
        self.__index=0

    def agregar(self,elemento):
        nodo=Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=self.__comienzo
        self.__tope+=1

    def mostrarTipoObjeto(self,posicion):
        auto=self.getNodo(posicion)

    def cambiarPrecioBase(self,patente,precioNuevo):
        auto=self.getNoto(patente)
        if auto==None:
            print("Patente no encontrada.")
        else:
            auto.setPrecioBase(precioNuevo)

    def mostrarMasEconomico(self):
        economico=None
        menor= 50000000000 #poner un numero absurdo
        for x in self.__iter__():
            importeVenta=x.getImporteVenta()
            if importeVenta<menor:
                menor=importeVenta
                economico=x
        print("\n-------------------------------------------------------------------------------------------------")
        print("{} {} {} {} {} {}".format("Modelo","Puertas","Color","Precio Base","Marca","Precio Total"))
        print("--------------------------------------------------------------------------------------------------")
        print(economico)
        print("--------------------------------------------------------------------------------------------------")

    def mostrar(self):
        print("\n-------------------------------------------------------------------------------------------------")
        print("{} {} {} {} {} {}".format("Modelo","Puertas","Color","Precio Base","Marca","Precio Total"))
        print("--------------------------------------------------------------------------------------------------")
        for elemento in self.__iter__():
            print(elemento)
        print("--------------------------------------------------------------------------------------------------")


    def toJson(self):
        d = dict(
            __clas__ = self.__class__.__name__,
            autos=[auto.toJson() for auto in self.__iter__()]
        )
        return d