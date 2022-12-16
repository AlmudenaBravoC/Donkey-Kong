class Barril:

    def __init__(self,x,y, direct): #first we define our variables
        self.__posX = x
        self.__posY = y
        self.__direct = direct 
        self.__num = 5
        self.a = 0 #this is for create the animation of our barrels
        self.__image = 0 #initial image of the barrel
        
    @property
    def posX(self):
        return self.__posX
    
    @property
    def posY(self):
        return self.__posY
    
    @property
    def direct(self):
        return self.__direct
    
    @property
    def image(self):
        return self.__image
    
    @property
    def num(self):
        return self.__num
    
    @image.setter
    def image(self, value):
        self.__image = value
    
    @direct.setter
    def direct(self, value):
        self.__direct = value
        
    @num.setter
    def num(self, value):
        self.__num = value
        
    
    def move(self,x,y): #function that produces the movement in the screen of the barrels
        self.__posX = x
        self.__posY = y
    
    def gira(self,direct): #function that simulate the animation of the barrels roll around
        """this function uses the variable direction that helps us to identify what sequence use to simulate 
        the rotation.
        We use also the varibale image that establishes a number that before (in the Main.py) is able to change 
        the image by a multiplication moving the x position in the pyxres document"""
        self.__direct = direct
        if (self.__direct == "right") or (self.direct == "right2") :
            if self.a == 0:
                self.__image = 0
                self.a+=1
            elif self.a == 5:
                self.__image = 1
                self.a+=1
            elif self.a == 10:
                self.__image = 2
                self.a+=1
            elif self.a == 15:
                self.__image = 3
                self.a+=1
            elif self.a == 20:
                self.a = 0
            else:
                self.a += 1
        
        elif (self.__direct == "left"):
            if self.a == 0:
                self.__image = 3
                self.a+=1
            elif self.a == 5:
                self.__image = 2
                self.a+=1
            elif self.a == 10:
                self.__image = 1
                self.a+=1
            elif self.a == 15:
                self.__image = 0
                self.a+=1
            elif self.a == 20:
                self.a = 0
            else:
                self.a += 1
        
        elif (self.__direct == "do"):
            if self.a == 0:
                self.__image = 0
                self.a+=1
            elif self.a == 5:
                self.__image = 1
                self.a+=1
            elif self.a == 20:
                self.a = 0
            else:
                self.a += 1
                
            
            
        