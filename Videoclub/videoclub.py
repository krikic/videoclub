#-------------------------------------------------------------------------------

class Socio():
    def __init__ (self):
        self.__numSocio=""
        self.__nombre = ""
        self.__compras = []    # LISTA DE Jugadores
        self.__alquileres = []     # LISTA DE Partidos jugados

    def getNumSocio(self):
        return self.__numSocio

    def setNumSocio(self,numSocio):
        self.__numSocio = numSocio


    def getNombre(self):
        return self.__Nombre

    def setNombre(self,Nombre):
        if len(Nombre) > 20:
            print ("ERROR")
            return
        self.__Nombre = Nombre


    def addAlquiler (self,alq):
        self.__alquileres.append(alq)

    def addCompra (self,comp):
        self.__compras.append(comp)

    def getAlquileres(self):
        return self.__alquileres

    def getCompras(self):
        return self.__compras

    def Imprimir (self):
        print ("Num de socio ",self.getNumSocio())
        print ("Nombre",self.getNombre())





class Pelicula():
    def __init__ (self):
        self.__codpelicula=""
        self.__titulo = ""
        self.__ejemplares=0
        self.__compras=[]
        self.__alquileres=[]

    def getCodPelicula(self):
        return self.__codpelicula

    def setCodPelicula(self,codpelicula):
        self.__codpelicula = codpelicula

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self,titulo):
        self.__titulo = titulo


    def getEjemplares(self):
        return self.__ejemplares

    def setEjemplares(self,ejemplares):
        self.__ejemplares = ejemplares

    def addAlquiler (self,alq):
        self.__alquileres.append(alq)

    def addCompra (self,comp):
        self.__compras.append(comp)

    def getAlquileres(self):
        return self.__alquileres

    def getCompras(self):
        return self.__compras


    def Imprimir (self):
        print ("Codigo pelicula ",self.getCodPelicula())
        print ("Titulo",self.getTitulo())
        print ("Ejemplares",self.getEjemplares())


class Compra():

    def __init__(self,socio,pelicula,fecha):
        self.__socio = socio
        self.__pelicula=pelicula
        self.__fecha=fecha

    def getSocio(self):
        return self.__socio

    def getPelicula(self):
        return self.__pelicula

    def getFecha(self):
        return self.__fecha



class Alquiler():

    def __init__(self,socio,pelicula,fecha):
        self.__socio = socio
        self.__pelicula=pelicula
        self.__fecha=fecha
        self.__retornada=False
        self.__fechaRetorno=""

    def getSocio(self):
        return self.__socio

    def getPelicula(self):
        return self.__pelicula

    def getFecha(self):
        return self.__fecha

    def retornar (self,fecha):
        self.__retornada=True
        self.__fechaRetorno = fecha

    def getRetornada(self):
        return self.__retornada

    def getFechaRetorno (self):
        return self.__fechaRetorno


class VideoClub():
    def __init__(self):
        self.__socios = []
        self.__peliculas= []
        self.__compras= []
        self.__alquileres=[]


    def cargarFichero (self):
        self.__socios = []
        self.__peliculas= []
        self.__compras= []
        self.__alquileres=[]


        try:
            F = open ("videoclub.txt","r")
            for x in F:
                datos = x.replace("\n","").split("\t")
                tipo = datos[0]
                if tipo == "SO":
                    J = Socio()
                    J.setNumSocio(datos[1])
                    J.setNombre(datos[2])
                    self.__socios.append(J)
                if tipo == "PE":
                    J=Pelicula()
                    J.setCodPelicula(datos[1])
                    J.setTitulo(datos[2])
                    J.setEjemplares(datos[3])
                    self.__peliculas.append(J)
                if tipo == "CO":
                    socio = [xx for xx in self.__socios if xx.getNumSocio() == datos[1]]
                    pelicula = [xx for xx in self.__peliculas if xx.getCodPelicula() == datos[2]]
                    J=Compra(socio[0],pelicula[0],datos[3])
                    socio[0].addCompra(J)
                    pelicula[0].addCompra(J)
                    self.__compras.append(J)

                if tipo == "AL":
                    socio = [xx for xx in self.__socios if xx.getNumSocio() == datos[1]]
                    pelicula = [xx for xx in self.__peliculas if xx.getCodPelicula() == datos[2]]
                    J=Alquiler(socio[0],pelicula[0],datos[3])
                    socio[0].addAlquiler(J)
                    pelicula[0].addAlquiler(J)
                    if datos[4] == "S":
                        J.retornar(datos[4])
                    self.__alquileres.append(J)

            F.close()
        except:
            print ("No encuentro el fichero")

    def guardarFichero(self):
        F = open("videoclub.txt","w")
        for x in self.__socios:
            F.write("SO" + "\t" + str(x.getNumSocio()) + "\t"+x.getNombre() +"\n")

        for x in self.__peliculas:
            F.write ("PE" + "\t" + str(x.getCodPelicula()) + "\t" + x.getTitulo()+ "\t" + str(x.getEjemplares()) + "\n")

        for x in self.__compras:
            F.write ("CO" + "\t" + str(x.getSocio().getNumSocio()) + "\t" +str(x.getPelicula().getCodPelicula()) + "\t" + x.getFecha()+ "\n")

        for x in self.__alquileres:
            strRetornada = "N"
            if x.getRetornada(): strRetornada = "S"
            F.write ("AL" + "\t" + str(x.getSocio().getNumSocio()) + "\t" +str(x.getPelicula().getCodPelicula()) + "\t" + x.getFecha()+ "\t" + strRetornada + "\t" + x.getFechaRetorno() + "\n")
        F.close()

    def agregarSocio (self,socio):
        jBuscar = [j for j in self.__socios if j.getNumSocio() == socio.getNumSocio()]
        if len(jBuscar) == 0:
            self.__socios.append(socio)
            return True
        else:
            return False

    def getSocios (self):
        return self.__socios

    def eliminarSocio (self,socio):

        jBorrar = [j for j in self.__alquileres if j.getSocio().getNumSocio() == socio.getNumSocio()]
        for j in jBorrar:
            if not j.getRetornada():
                j.getPelicula().setEjemplares(int(j.getPelicula().getEjemplares())+1)
            self.__alquileres.remove(j)
        jBorrar = [j for j in self.__compras if j.getSocio().getNumSocio() == socio.getNumSocio()]
        for j in jBorrar:
            self.__compras.remove(j)

        self.__socios.remove(socio)


    def agregarPelicula (self,pelicula):
        jBuscar = [j for j in self.__peliculas if j.getCodPelicula() == pelicula.getCodPelicula()]
        if len(jBuscar) == 0:
            self.__peliculas.append(pelicula)
            return True
        else:
            return False

    def getPeliculas (self):
        return self.__peliculas

    def eliminarPelicula (self,pelicula):
        jBorrar = [j for j in self.__alquileres if j.getPelicula().getCodPelicula() == pelicula.getCodPelicula()]
        for j in jBorrar:
            if not j.getRetornada():
                j.getPelicula().setEjemplares(int(j.getPelicula().getEjemplares())+1)
            self.__alquileres.remove(j)
        jBorrar = [j for j in self.__compras if j.getPelicula().getCodPelicula() == pelicula.getCodPelicula()]
        for j in jBorrar:
            self.__compras.remove(j)

        self.__peliculas.remove(pelicula)

    def alquilar (self,codSocio,codPelicula,fecha):
        socio = [x for x in self.__socios if x.getNumSocio() == codSocio]
        if len(socio) == 0:
            return False
        pelicula = [x for x in self.__peliculas if x.getCodPelicula() == codPelicula]
        if len(pelicula) == 0:
            return False
        if pelicula[0].getEjemplares() == 0:
            return False
        pelicula[0].setEjemplares(int(pelicula[0].getEjemplares())-1)
        alquiler = Alquiler(socio[0],pelicula[0],fecha)
        pelicula[0].addAlquiler(alquiler)
        socio[0].addAlquiler(alquiler)
        self.__alquileres.append(alquiler)
        return True

    def devolver (self,numSocio,numPeli,fecha):
        alq = [x for x in self.__alquileres if x.getSocio().getNumSocio() == numSocio and x.getPelicula().getCodPelicula() == numPeli and not x.getRetornada()]
        if len(alq) == 0:
            return False
        alq[0].getPelicula().setEjemplares(int(alq[0].getPelicula().getEjemplares())+1)
        alq[0].retornar(fecha)
        return True

    def comprar (self,codSocio,codPelicula,fecha):
        socio = [x for x in self.__socios if x.getNumSocio() == codSocio]
        if len(socio) == 0:
            return False
        pelicula = [x for x in self.__peliculas if x.getCodPelicula() == codPelicula]
        if len(pelicula) == 0:
            return False
        if pelicula[0].getEjemplares() == 0:
            return False
        pelicula[0].setEjemplares(int(pelicula[0].getEjemplares())-1)
        compra = Compra(socio[0],pelicula[0],fecha)
        pelicula[0].addCompra(compra)
        socio[0].addCompra(compra)
        self.__compras.append(compra)
        return True


class GestionVideoClub():
    def __init__(self):
        self.__video = VideoClub()
        self.__video.cargarFichero()

    def guardarFichero (self):
        self.__video.guardarFichero()

    def AgregarSocio(self):
        m = Socio()
        s = input ("Codigo socio: ")
        m.setNumSocio(s)
        s = input ("Nombre: ")
        m.setNombre(s)
        result=self.__video.agregarSocio(m)
        if not result:
            print ("No se ha podido agregar el socio")

    def VisualizarSocios (self):
        print ("Lista de socios")
        print ("================")
        for x in self.__video.getSocios():
            print (x.getNumSocio(),x.getNombre())
            print ("Pelis alquiladas")
            for p in x.getAlquileres():
                print (p.getFecha(),p.getPelicula().getCodPelicula(), p.getPelicula().getTitulo(),p.getRetornada())
            print ("Pelis compradas")
            for p in x.getCompras():
                print (p.getFecha(),p.getPelicula().getCodPelicula(), p.getPelicula().getTitulo())

    def AgregarPelicula(self):
        m = Pelicula()
        s = input ("Codigo pelicula: ")
        m.setCodPelicula(s)
        s = input ("Titulo: ")
        m.setTitulo(s)
        s = input ("Ejemplares: ")
        m.setEjemplares(s)
        result = self.__video.agregarPelicula(m)
        if not result:
            print ("No se ha podido agregar la pelicula")

    def VisualizarPelicula (self):
        print ("Lista de peliculas")
        print ("================")
        for x in self.__video.getPeliculas():
            print (x.getCodPelicula(),x.getTitulo(),x.getEjemplares())

    def borrarSocio (self):
        num = int(input("Codigo socio:"))
        socio = [x for x in self.__video.getSocios() if int(x.getNumSocio()) == num]
        if len(socio) == 0:
            print ("No existe")
            return
        self.__video.eliminarSocio(socio[0])

    def borrarPelicula (self):
        num = int(input("Codigo pelicula:"))
        pelicula = [x for x in self.__video.getPeliculas() if int(x.getCodPelicula()) == num]
        if len(pelicula) == 0:
            print ("No existe")
            return
        self.__video.eliminarPelicula(pelicula[0])


    def OrdPeliculasTitulo (self):
        print ("Lista de peliculas")
        print ("================")
        Num = 1
        Ordenados = sorted(self.__video.getPeliculas(),key=GestionVideoClub.ObtenerTitulo)
        for x in Ordenados:
         print (Num,x.getCodPelicula(),x.getTitulo())
         Num += 1

    @staticmethod
    def ObtenerTitulo (x):
        return x.getTitulo()

    def Alquilar (self):
        numSocio = input("Codigo del socio: ")
        numPelicula = input("Codigo de la pelicula: ")
        fecha = input("Fecha: ")
        result = self.__video.alquilar(numSocio,numPelicula,fecha)
        if not result:
            print ("No se ha podido alquilar la pelicula")

    def Devolver (self):
        numSocio = input("Codigo del socio: ")
        numPelicula = input("Codigo de la pelicula: ")
        fecha = input("Fecha: ")
        result = self.__video.devolver(numSocio,numPelicula,fecha)
        if not result:
            print ("No se ha podido devolver la pelicula")

    def Comprar (self):
        numSocio = input("Codigo del socio: ")
        numPelicula = input("Codigo de la pelicula: ")
        fecha = input("Fecha: ")
        result = self.__video.comprar(numSocio,numPelicula,fecha)
        if not result:
            print ("No se ha podido comprar la pelicula")


def Menu():
    print ("Menu:")
    print ("1 - Agregar socio")
    print ("2 - Visualizar socios")
    print ("3 - Agregar pelicula")
    print ("4 - Visualizar peliculas")
    print ("5 - Alquilar")
    print ("6 - Devolver")
    print ("7 - Comprar")
    print ("8 - Eiminar socio")
    print ("9 - Eliminar pelicula")
    print("10 - Ordenar peliculas por titulo")
    print ("0 - Salir")
    op = -1
    while op < 0 or op > 10:
        op = int(input("Introducir opcion: "))
    return op



def main():
    gestion = GestionVideoClub()
    opcion = -1
    while opcion != 0:
        opcion = Menu()
        if opcion == 1:
            gestion.AgregarSocio()
        elif opcion == 2:
            gestion.VisualizarSocios()
        elif opcion == 3:
            gestion.AgregarPelicula()
        elif opcion == 4:
            gestion.VisualizarPelicula()
        elif opcion == 5:
            gestion.Alquilar()
        elif opcion == 6:
            gestion.Devolver()
        elif opcion == 7:
            gestion.Comprar()
        elif opcion == 8:
            gestion.borrarSocio()
        elif opcion == 9:
            gestion.borrarPelicula()
        elif opcion ==10:
            gestion.OrdPeliculasTitulo()

    gestion.guardarFichero()


if __name__ == '__main__':
    main()









