class Control:
    

    def enlazar(self,tv):    
        self.tv=tv 
        tv.control=self




    def turnOff(self):
        if self.tv.estado==True:
            self.estado=False

    def turnOn(self):
        if self.tv.estado==False:
            self.estado=True

    def canalUp(self):
        if self.tv.estado==True:
            if self.canal>=1 and self.canal<120:
                self.canal+=1

    def canalDown(self):
        if self.tv.estado==True:
            if self.canal>1 and self.canal<=120:
                self.canal-=1

    def volumenUp(self):
        if self.tv.estado==True:
            if self.volumen>=0 and self.volumen<7:
                self.volumen+=1

    def volumenDown(self):
        if self.tv.estado==True:
            if self.volumen>0 and self.volumen<=7:
                self.volumen-=1

    def setCanal(self,canal):

        if canal>=1 and canal<=120 and self.tv.estado==True:
            self.tv.canal=canal 

    def getTv(self):
        return self.tv

    def setTv(self,tv):
        self.tv=tv    