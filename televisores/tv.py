class TV:
    numTV=0
    def __init__(self,marca,estado):
        self.marca=marca
        self.canal=1
        self.volumen=1
        self.precio=500
        self.estado=estado
        self.control=None
        TV.numTV+=1

    def turnOff(self):
        if self.estado==True:
            self.estado=False

    def turnOn(self):
        if self.estado==False:
            self.estado=True

    def canalUp(self):
        if self.estado==True:
            if self.canal>=1 and self.canal<120:
                canal+=1

    def canalDown(self):
        if self.estado==True:
            if self.canal>1 and self.canal<=120:
                canal-=1

    def volumenUp(self):
        if self.estado==True:
            if self.volumen>=0 and self.volumen<7:
                self.volumen+=1

    def volumenDown(self):
        if self.estado==True:
            if self.volumen>0 and self.volumen<=7:
                self.volumen-=1

    def getEstado(self):
        return  self.estado                
 

    def getMarca(self):
        return  self.marca

    def setMarca(self,marca):
        self.marca=marca

    def getControl(self):
        return  self.control

    def setControl(self,control):
        self.control=control

    def getPrecio(self):
        return  self.precio

    def setPrecio(self,precio):
        self.precio=precio
        
    def getVolumen(self):
        return  self.volumen

    def setVolumen(self,volumen):

        if volumen>=0 and volumen<=7:
            self.volumen=volumen  
        

    def getCanal(self):
        return  self.canal

    def setCanal(self,canal):

        if canal>=1 and canal<=120 and self.estado==True:
            self.canal=canal 

    def getNumTV(self):
        return self.numTV
	
    def setNumTV(self, numTV):
	    TV.numTV = numTV