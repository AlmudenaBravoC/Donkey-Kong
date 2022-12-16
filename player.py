class Player:
    
    def __init__(self,x,y): #first we define our variables
        self.__posX = x
        self.__posY = y
        self.__lives = 3 #the lives of Mario
        self.a = 0 #for the animation of Mario going up and down
        self.b = 0 #for the animation of Mario going to the left and right
        self.__Image = 3 #initial image for Mario (stop looking to the right side)
        self.salta = False #for the function jump
        self.__direction = "right" #to know the direction that has Mario
        self.__score = 0 #the score 
        self.__sco = False #for the text of score to appear in the Game
        self.__death = False #when Mario has no more lives then death is True and appear the end screen 
    
    
    @property
    def posX(self):
        return self.__posX
    
    @property
    def posY(self):
        return self.__posY
    
    @property
    def lives(self):
        return self.__lives
    
    @property
    def direction(self):
        return self.__direction
    
    @property
    def Image(self):
        return self.__Image
    
    @property
    def score(self):
        return self.__score
    
    @property
    def sco(self):
        return self.__sco
    
    @property
    def death(self):
        return self.__death
    
    @posX.setter
    def posX(self, value):
        self.__posX = value
        
    @posY.setter
    def posY(self, value):
        self.__posY = value
        
    @lives.setter
    def lives(self, value):
        self.__lives = value
    
    @direction.setter
    def direction(self, value):
        self.__direction = value
    
    @Image.setter
    def Image(self, value):
        self.__Image = value
    
    @sco.setter
    def sco(self, value):
        self.__sco = value
    
    @death.setter
    def death(self, value):
        self.__death = value
    
    def newmove(self, d, bars=[], stairs=[]): #to move Mario using the floor and ladders lists
        """This function uses the direction variable and therefore being able to know what direction has Mario
        to take. Using other functions like run(simulate Mario running) and move(Move Mario in the screen) we
        are able to create a function that depending of the direction (d) moves Mario.
        Also we had to create with the 'for' a loop so the program compares the position of Mario with the 
        different possitions of the floor and stairs.
        For the directions up and down we need to introduce two more 'if' that helped the program to identify
        the position of Mario during the up and down so he can go to the end of the stairs"""
        for b in range(len(bars)):
            if self.__posY == bars[b].posY-16:
                if d == 'left':
                    self.move(self.__posX-2, self.__posY)
                    self.run()
                    self.__direction = "left"
                if d == 'right':
                    self.move(self.__posX+2, self.__posY)
                    self.run() 
                    self.__direction = "right"
        if d == 'jump':
            for b in range(len(bars)):
                if self.__posY == bars[b].posY-16:
                    self.__Image =0
                    self.jump()
        if d == 'up':
            for s in range(len(stairs)):
                if self.__posX >= stairs[s].posX-16 and self.__posX <= stairs[s].posX:
                    if self.__posY <= stairs[s].posY-16 and self.__posY >= stairs[s].posY-21:
                        self.move(self.__posX, self.__posY-1)
                        self.__direction = "up"
        if d == 'do':
            for s in range(len(stairs)):
                if self.__posX > stairs[s].posX-16 and self.__posX < stairs[s].posX:
                    if self.__posY <= stairs[s].posY-17 and self.__posY >= stairs[s].posY-22:
                        self.move(self.__posX, self.__posY+1)
                        self.__direction = "do"

    def move(self,x,y): #like method of move of the 'barril.py' that has also the animation of the up and down Mario
        self.__posX = x
        self.__posY = y
        if self.__direction == "up" or self.__direction == "do":
            if self.a < 4:
                self.__Image = 4
                self.a += 1
            elif self.a < 8:
                self.__Image = 5
                self.a += 1
            elif self.a < 12:
                self.__Image = 5
                self.a = 0
            else:
                self.a += 1
        
    def jump(self): #function for Mario to jump
        """ this method uses the direction to know if the x position of Mario has to increment or decrease, 
        aslo it increment his y position"""
        if self.__direction == "left": 
            self.__Image = 0
            self.__posX-=15
        elif self.__direction == "right":
            self.__Image = 1
            self.__posX+=15
        self.__posY-=15
        self.salta=True
        
        
    def jumpNo(self): #function for Mario to come back to the floor
        """ as the method jump(), this function uses the direction and decrease the y position of Mario"""
        if self.__direction == "left":
            self.__Image = 0
            self.__posX-=15
        elif self.__direction == "right":
            self.__Image = 1
            self.__posX+=15
        self.__posY+=15   
        self.salta=False
      
        
    def run(self): #like method gira of 'barril.py'
        if self.__direction == "left":
            if self.b < 2:
                self.__Image = 0
                self.b += 1
            elif self.b < 4:
                self.__Image = 2
                self.b += 1
            elif self.b < 6:
                self.b = 0
            else:
                self.b += 1
        elif self.__direction == "right":
            if self.b < 2:
                self.__Image = 1
                self.b += 1
            elif self.b < 4:
                self.__Image = 3
                self.b += 1
            elif self.b < 6:
                self.b = 0
            else:
                self.b += 1
    
    
    def perderVidas(self): #to decrease the lives of Mario after touching a barrel
        self.__lives -=1 
        if self.__lives !=0:
            self.__score = 0 #the score of the bonus part after dying is 0 except the last time that saws the score at the end-screen
    
    def restart_lives(self): #to restart the lives after pressing R 
        self.__lives = 3
    
    def sumPoints(self, tipo): #to increment the score, it has the original (after jump a barrel) and when a barrel is remove of our screen
        if tipo == "remove":
            self.__score +=50
        else:
            self.__score += 100
            self.__sco = True #to saw the text of 100 point in the game

