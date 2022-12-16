class DonkeyKong:
    
    def __init__(self, x, y):
        self.__posX = x
        self.__posY = y
        self.__b = 0 #we will use this to change the image of our Donkey
        self.__image = 0
        
    @property
    def posX(self):
        return self.__posX
    
    @property
    def posY(self):
        return self.__posY
    
    @property
    def image(self):
        return self.__image
    
    @property
    def b(self):
        return self.__b
    
    @b.setter
    def b(self, value):
        self.__b = value
    
    @image.setter
    def image(self, value):
        self.__image = value

    def movement(self): #With this function we create the movement of the Donkey Kong, so he can move
        if self.b < 8:
            self.__image = 0
            self.b += 1
        elif self.b < 32:
            self.__image = 2
            self.b += 1
        elif self.b < 40:
            self.b = 0
        else:
            self.b += 1