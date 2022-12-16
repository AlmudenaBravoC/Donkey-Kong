class Princess:
    
    def __init__(self, x, y): #to define the position of the princess
        self.__posX = x
        self.__posY = y
        
    @property
    def posX(self):
        return self.__posX
    
    @property
    def posY(self):
        return self.__posY