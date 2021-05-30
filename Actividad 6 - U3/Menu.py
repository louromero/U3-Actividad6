from ObjetEncoder import ObjectEncoder

class Menu:
    __switcher=None

    def __init__(self):
        self.__switcher={ 1:self.opcion1,
                        2:self.opcion2,
                        3:self.opcion3,
                        4:self.opcion4,
                        5:self.opcion5,
                        6:self.opcion6,
                        7:self.opcion7,
                        0:self.salir
                        }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self,opcion,lista):
        funcion=self.__switcher.get(opcion,lambda:print("\nOpcion no valida."))
        funcion(lista)

    #---------------------------------------------------------------OPCION 1
    def opcion1(self,lista):
        print("\nCrear Auto: ")
        auto=lista.crearAuto()
        print("Indice maximo posible: {}".format(lista.getTope()-1))
        posicion=int(input("Posicion: "))
        while auto==None:
            print("Error al intentar crear. Intente de nuevo.")
            auto=lista.crearAuto()
        lista.insertar(posicion,auto)

    #---------------------------------------------------------------OPCION 2
    def opcion2(self,lista):
        print("Crear Auto: ")
        auto = lista.crearAuto()
        while auto == None:
            print("Error al intentar crear, intente de nuevo")
            auto = lista.crearAuto()
        lista.agregar(auto)

    #---------------------------------------------------------------OPCION 3
    def opcion3(self,lista):
        try:
            print("\nIndice maximo posible: {}".format(lista.getTope()-1))
            posicion=int(input("Posicion: "))
            assert posicion >=0
        except:
            print("\nPosicion ingresada invalida.")
        else:
            lista.mostrarTipoObjeto(posicion)

    #---------------------------------------------------------------OPCION 4
    def opcion4(self,lista):
        patente=input("Patente: ")
        precioNuevo=float(input("Precio nuevo: "))
        lista.cambiarPrecioBase(patente,precioNuevo)

    #---------------------------------------------------------------OPCION 5
    def opcion5(self,lista):
        lista.mostrarMasEconomico()

    #---------------------------------------------------------------OPCION 6
    def opcion6(self,lista):
        lista.mostrar()
    
    #---------------------------------------------------------------OPCION 7
    def opcion7(self,lista):
        dic=lista.toJson()
        encoder = ObjectEncoder()
        try:
            encoder.guardarJSONarchivo(dic,"vehiculos.json")
        except:
            print("\nError al guardar.")
        else:
            print("\nGuardado exitoso.")

    #---------------------------------------------------------------SALIR
    def salir(self,lista):
        print("\nChau :)")