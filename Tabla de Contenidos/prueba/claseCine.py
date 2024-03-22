#EJERCICIO 4
#TAREA ACADÉMICA 2
#ELABORADO POR ANEL RAMIREZ-MICAELA HORNY-JENNY CUSICUNA
class Cine:
    def __init__(self,pelicula,cant,num,duracion,ed,director):
        self.pelicula=pelicula
        self.cantidadAsientos=72
        self.numeroAsiento=num
        self.asientos=[[(1,'A'), (1,'B'),(1,'C'),(1,'D'),(1,'E'), (1,'F'),(1,'G'),(1,'H'),(1,'I')],
                       [(2,'A'), (2,'B'),(2,'C'),(2,'D'),(2,'E'), (2,'F'),(2,'G'),(2,'H'),(2,'I')],
                       [(3,'A'), (3,'B'),(3,'C'),(3,'D'),(3,'E'), (3,'F'),(3,'G'),(3,'H'),(3,'I')],
                       [(4,'A'), (4,'B'),(4,'C'),(4,'D'),(4,'E'), (4,'F'),(4,'G'),(4,'H'),(4,'I')],
                       [(5,'A'), (5,'B'),(5,'C'),(5,'D'),(5,'E'), (5,'F'),(5,'G'),(5,'H'),(5,'I')],
                       [(6,'A'), (6,'B'),(6,'C'),(6,'D'),(6,'E'), (6,'F'),(6,'G'),(6,'H'),(6,'I')],
                       [(7,'A'), (7,'B'),(7,'C'),(7,'D'),(7,'E'), (7,'F'),(7,'G'),(7,'H'),(7,'I')],
                       [(8,'A'), (8,'B'),(8,'C'),(8,'D'),(8,'E'), (8,'F'),(8,'G'),(8,'H'),(8,'I')]]
        self.precioEntrada=precio 
        self.duracion=duracion 
        self.edadMinima= ed
        self.director=director

    def setPelicula(self,pelicula):
        pelicula=input("ingrese la pelicula que desea ver(Doctor Strange o El conjuro): ")
        self.pelicula=pelicula

    def getPelicula(self):
        return self.pelicula
    
    def setPrecio(self,precio):
        if self.pelicula=='Doctor Strange':
            precio=25
        elif self.pelicula=='El conjuro':
            precio=22
        self.precioEntrada=precio

    def getPrecio(self):
        return self.precioEntrada

    def setDuracion(self,duracion):
        if self.pelicula=='Doctor Strange':
            duracion=120
        elif self.pelicula=='El conjuro':
            duracion=125
        self.duracion=duracion

    def getDuracion(self):
        return self.duracion

    def setEdadMinima(self,ed):
        if self.pelicula=='Doctor Strange':
            ed=12
        elif self.pelicula=='El conjuro':
            ed=16
        self.edadMinima=ed

    def getEdadMinima(self):
        return self.edadMinima

    def setDirector(self,director):
        if self.pelicula=='Doctor Strange':
            director="Sam Raimi"
        elif self.pelicula=='El conjuro':
            director="James Wan"
        self.director=director

    def getDirector(self):
        return self.director

    def Asientos(self):
        if self.numeroAsiento in self.asientos:
            self.asientos.remove(self.numeroAsientos)
            print("el asiento está disponible")
            self.numAsientos=self.numAsientos-1
            return True
        elif self.cantidadAsientos!=0:
            m=self.asientos[0]
            print("su asiento es: ",m)
            self.cantidadAsientos = self.cantidadAsientos-1
            return True
        else:
            print("No hay asientos disponibles")
            return False
        
