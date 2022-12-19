import pyxel
import player
import barril
import kong
import stairs
import barras
import princess
import constants
from random import randint #we import randint to be able to use the random variable



class Game:
    
    def __init__(self):

        self.sticker = player.Player(constants.m_posX, constants.m_posY) #we establish the variable Mario in our Main program
        self.donkey = kong.DonkeyKong(constants.d_posX, constants.d_posY) #do we as well with the Donkey Knog
        self.princess = princess.Princess(constants.p_posX, constants.p_posY) #and with the princess
        self.barrels = [] #we create a list to add the barrels in the game
        self.stairs = [] #a list that we will use to draw the stairs and for Mario to go up them
        self.ladders = [] #a list with the first units of the stairs to the barrels go down
        self.bars = [] #as the stairs[], this is a list for draw the bars
        self.floor = [] #as for the ladders[], is a list for Mario and barrels to move
        self.corazon = False #if is False, the heart is not in the screen
        self.help = True #if is True, the "HELP" is in the screen
        self.counter = 0 #to calculate the time of the jump of Mario
        self.fin = 0 #to calculate the time of the end-screen to close after some time
        self.fin2= 0 #to calculate the time of the end-screen to show up after the game ends and Mario gets to the last floor
        
        #TO CREATE THE STAIRS
        for i in range(8): #8 is for the size of ours stairs
            stairsobj = stairs.Stairs(constants.s1_posX, constants.s1_posY - 6*i) #6 the size of the stairs in the pyxres document
            self.stairs.append(stairsobj)
            if i == 0:
                self.ladders.append(stairsobj) #we add only the first to later use with the barrels
        
        for i in range(8):
            stairsobj = stairs.Stairs(constants.s2_posX, constants.s2_posY - 6*i)
            self.stairs.append(stairsobj)
            if i == 0:
                self.ladders.append(stairsobj)
        
        for i in range(8):
            stairsobj = stairs.Stairs(constants.s3_posX, constants.s3_posY - 6*i)
            self.stairs.append(stairsobj)
            if i == 0:
                self.ladders.append(stairsobj)
        
        for i in range(8):
            stairsobj = stairs.Stairs(constants.s4_posX, constants.s4_posY - 6*i)
            self.stairs.append(stairsobj)
            if i == 0:
                self.ladders.append(stairsobj)
            
        for i in range(8):
            if i != 3 and i != 4:
                stairsobj = stairs.Stairs(constants.hs1_posX, constants.s1_posY - 6*i)
                #constants.s1_posY += 6
            self.stairs.append(stairsobj)
            if i == 0:
                self.ladders.append(stairsobj)
            
        for i in range(8):
            if i != 3 and i != 4:
                stairsobj = stairs.Stairs(constants.hs2_posX, constants.s2_posY - 6*i)
            self.stairs.append(stairsobj)
            if i == 0:
                self.ladders.append(stairsobj)
            
        for i in range(8):
            if i != 3 and i != 4:
                stairsobj = stairs.Stairs(constants.hs3_posX, constants.s3_posY - 6*i)
            self.stairs.append(stairsobj)
            if i == 0:
                self.ladders.append(stairsobj)
            
            #LARGE STAIRS
        for i in range(15): #15 is the size of the large stairs
            stairsobj = stairs.Stairs(constants.ls1_posX, constants.ls_posY + 6*i)
            self.stairs.append(stairsobj) #this stairs we don't need to append it to the lsit because Mario doesn't use them
        
        for i in range(15):
            stairsobj = stairs.Stairs(constants.ls2_posX, constants.ls_posY + 6*i)
            self.stairs.append(stairsobj)
        
        #TO CREATE THE FLOORS
        for i in range(32): #32 is the size
            barobj = barras.Barras(constants.b1_posX + 8*i, constants.b1_posY)
            self.bars.append(barobj) #we DON'T use this list because we had check that if we use it the Mario GOES SO FAST THAT IS IMPOSSIBLE TO PLAY
            if i == 0:
                self.floor.append(barobj) #like with the stairs, we add only the ones we will need 
            
        for i in range(32):
            barobj = barras.Barras(constants.b2_posX + 8*i, constants.b2_posY)
            self.bars.append(barobj)
            if i == 0:
                self.floor.append(barobj)
        
            
        for i in range(32):
            barobj = barras.Barras(constants.b3_posX + 8*i, constants.b3_posY)
            self.bars.append(barobj)
            if i == 0:
                self.floor.append(barobj)
            
        for i in range(32):
            barobj = barras.Barras(constants.b4_posX + 8*i, constants.b4_posY)
            self.bars.append(barobj)
            if i == 0:
                self.floor.append(barobj)
            
        for i in range(10):
            barobj = barras.Barras(constants.b5_posX + 8*i, constants.b5_posY)
            self.bars.append(barobj)
            if i == 0:
                self.floor.append(barobj)
        
            
            
        
        # The first thing to do is to create the screen
        pyxel.init(constants.WIDTH, constants.HEIGHT, title=constants.CAPTION) #we use the constanst that we establish in the CONSTANT file
        pyxel.load("assets/Mario.pyxres") #the folder and file name of the pictures 
        
        pyxel.run(self.update, self.draw) #to run our game (it runs every 1sec)
        

        
   
    
    def update_Mario(self):
        """We create this fuction to all the update that Mario needs, taking the information of the buttons that are pressed, 
        the direction that is taking, the position and therefore, the move that can or cannot do, and the animation """
        if not pyxel.btn(pyxel.KEY_RIGHT) or not pyxel.btn(pyxel.KEY_LEFT) or not pyxel.btn(pyxel.KEY_UP) or not pyxel.btn(pyxel.KEY_DOWN):
            if self.sticker.direction == "left": #to show the Mario picture stop while any button is not press. This picture also depends in the last direction that teh program has.
                self.sticker.Image = 2
            else: #in the case to be right
                self.sticker.Image = 3
        
        
                #For Mario only going down in the holes 
        if (self.sticker.posX == constants.WIDTH-26) and (self.sticker.posY < self.floor[2].posY-16):
            self.sticker.move(self.sticker.posX, self.sticker.posY+2) #with this Mario goes down until he gets to the next floor
        if (self.sticker.posX == constants.WIDTH-25) and (self.sticker.posY < self.floor[0].posY-16) and (self.sticker.posY > self.floor[1].posY-17):
            self.sticker.move(self.sticker.posX, self.sticker.posY+2)
        if (self.sticker.posX == 10) and (self.sticker.posY < self.floor[1].posY-16): 
            self.sticker.move(self.sticker.posX, self.sticker.posY+2)
        
        
                #to end the game and WIN
        if (self.sticker.posY == self.floor[4].posY-16) and self.fin2 == 0:
            self.corazon = True #now the Heart is in the screen adn the Help is not
            self.help = False
            self.sticker.direction = "left" #we establish the direction that Mario has to take so he stares at the princess
            self.fin2 = pyxel.frame_count #start of the time to show the end-screen 
        
        if self.fin2 != 0: #only if it is different, and therefore Mario has achive the last floor it checks if the remain is 150 
            if pyxel.frame_count-self.fin2 == 150: #if it is, then the death variable is TRUE and we start to use the FIN variable for the end-screen
                self.sticker.death = True
                self.fin = pyxel.frame_count
        
       
                #to establish that Mario doesn't go out of the limit of the game-screen
        if self.sticker.posX < 0:
            self.sticker.posX = 1
        if self.sticker.posX > constants.WIDTH-16:
            self.sticker.posX = constants.WIDTH-17            
        
        #MOVEMENT
                #for this we use the function of newmove() to move Mario (like we saw in the file of PLAYER)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.sticker.newmove('left',bars=self.floor[:4]) #we don't put the last floor because it that last one he cannot move
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.sticker.newmove('right',bars=self.floor[:4])
        elif pyxel.btn(pyxel.KEY_UP):
            self.sticker.newmove('up',stairs=self.stairs)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.sticker.newmove('do',stairs=self.stairs) 
        if pyxel.btnp(pyxel.KEY_SPACE):
            if not self.sticker.salta:
                self.counter=pyxel.frame_count #to start counting the time of jump that Mario has
                self.sticker.newmove('jump',bars=self.floor[:4])
                for i in self.barrels: #this we use to check if Mario is jumping a barrel and therefore to increment the score
                        if i.posY in range(self.sticker.posY, self.sticker.posY+40):
                            if i.posX in range (self.sticker.posX-15, self.sticker.posX+15):
                                self.sticker.sumPoints("jump") #we put jump because is 100 points
        if self.sticker.salta and pyxel.frame_count-self.counter==4:
            self.sticker.jumpNo()
            self.counter=0 #we establish the original so he doesn't stay jumping while we dont press the button again
            
    
    def update_Barrels(self):
        """Like with Mario, we create a individual update_Barrels to add randomly a barrel and analysing them every time the pyxel executes"""
        if (len(self.barrels) < 10): #only if the length is less than 10, we can continue adding barrels randomly
            if randint(0, 100) == 2: #to add randomly a barrel in the list
                self.barrel = barril.Barril(constants.barrel_posX, constants.barrel_posY, "right") #with start direction right
                self.barrels.append(self.barrel)
                
        #CHECKING EVERY BARREL
        for i in self.barrels: 
                #first the direction(we create two variables 'right' because if not the programm confuses the positions)
            if (i.direct == "right") and (i.posX != constants.WIDTH-20): #the numbers are for the barrels to go down at the holes
                i.gira("right")
                i.move(i.posX+2, i.posY)
            elif (i.direct == "right2") and (i.posX != constants.WIDTH-22):
                i.gira("right2")
                i.move(i.posX+2, i.posY)
            elif (i.direct == "left") and (i.posX != 11):
                i.gira("left")
                i.move(i.posX-2, i.posY)
            elif (i.direct == "do"):
                i.gira("do")
            
                #Mario’s crashes with the barrels
            if not self.sticker.salta:
                    #left size
                if (self.sticker.posX - i.posX < 10) and (self.sticker.posX - i.posX > 0) and (i.posY in range(self.sticker.posY-10, self.sticker.posY+16)):
                    #we establish a range of positive numbers (for that the >0) and of the width of the barrel picture, and the position y in case the barrel crash with Mario at the top of him 
                    self.sticker.perderVidas() #call the function loosing lifes
                    self.restart() #we restart the original values
                    if (self.sticker.lives == 0): #in the case of lives == 0 then is because Mario has no more lives left, then it opnes the end-screen
                        self.sticker.death = True
                        self.fin=pyxel.frame_count #to start with the time to close the screen of the game
                    #right size (the same that with the left)
                if (i.posX - self.sticker.posX < 10) and (i.posX - self.sticker.posX > 0) and (i.posY in range(self.sticker.posY-10, self.sticker.posY+16)):
                    self.sticker.perderVidas()
                    self.restart()
                    if (self.sticker.lives == 0):
                        self.sticker.death = True
                        self.fin=pyxel.frame_count
            
            
                #Down the barrels through the holes
            if (i.posX == constants.WIDTH-20): #at this position then we check the position Y
                if (i.posY < constants.b3_posY-10):
                    i.move(i.posX, i.posY+2)
                    if (i.posY == constants.b3_posY-10): #if the barrel is in the correct position then we move the x position of the barrel
                        i.move(i.posX-1, i.posY)
                        i.direct = "left"
            
            if (i.posX == 11): #we do the same with the other holes
                if (i.posY < constants.b2_posY-11):
                    i.move(i.posX, i.posY+2)
                    if (i.posY == constants.b2_posY-10):
                        i.move(i.posX+1, i.posY)
                        i.direct = "right2"
                        
            if (i.posX == constants.WIDTH-22):
                if (i.posY < constants.b1_posY-10):
                    i.move(i.posX, i.posY+2)
                    if (i.posY == constants.b1_posY-10):
                        i.move(i.posX-1, i.posY)
                        i.direct = "left"
            
            
                #Barrels are removed in the initial position
            if (i.posX == 13) and (i.posY == constants.b1_posY-10):
                self.barrels.remove(i)
                self.sticker.sumPoints("remove") #we call the function sumPoints() using 'remove' so it increments 50 the points
            
                #Barrels down the stairs
            for s in range(len(self.ladders)): #using the list and if they have the same position, then it goes down
                if i.posX == self.ladders[s].posX:
                    if i.posY == self.ladders[s].posY-58:
                        if i.num != 0: #if the num is different of 0, then we use the randint to compute randomly if the barrel goes down or not
                            if randint(0,3)==0:
                                i.direct = "do"
                                i.image = 0
                                i.num = 0
                    if i.num == 0: #if it is TRUE, the it goes down
                        if i.posY < self.ladders[s].posY-10:
                            i.move(i.posX, i.posY+2)
                        elif i.posY == self.floor[1].posY-10: #depending of the position, the direction will be different
                            i.direct = "right"
                            i.move(i.posX+1, i.posY)
                            i.num = 6
                        else:
                            i.direct = "left"
                            i.move(i.posX-1, i.posY)
                            i.num = 6
                            
    def restart(self):
        """We create a function to reset the values in case of dying or press R"""
        self.sticker.posX = constants.m_posX
        self.sticker.posY = constants.m_posY
        self.sticker.direction = "right"
        self.sticker.Image = 3
        self.sticker.death = False
        self.corazon = False
        self.barrels.clear()
        
        
    def update(self):
        """The update contains all the different updates and the posibilities of pressing Q (quit) or R (reset)"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R) and self.sticker.death:
            self.restart()
            self.sticker.restart_lives()
            self.fin = 0
            
        
        #FIRE
        self.kind = randint(0, 3) #we do it randomly (the image)
        
        
        self.update_Mario()
        self.update_Barrels()
        self.donkey.movement() #call the movement function of KONG file
            
    def draw_death(self):
        """only if death is TRUE it appears the end-screen (if Mario dies or wins)"""
        pyxel.cls(0)
        score = "{:06}".format(self.sticker.score) #to create the score (of length 6) in the format of score that is an integer
        pyxel.text(90, 88, "G A M E     O V E R ", 7)
        pyxel.text(95, 99, "S C O R E : " + score, 7)
        pyxel.text(95, 130, "( Q ) U I T", 7)
        pyxel.text(95, 155, "( R ) E S T A R T", 7)
        
        if pyxel.frame_count-self.fin == 150:
            pyxel.quit()
        
            
            
    def draw(self): 
        """ to draw all the pictures in the screen
        For most of them, uses the variables of the images that depends on the number
        also the posX and posY that change in the case of the barrels and Mario"""
        
        if not self.sticker.death: #if death is FALSE we draw all the barrels, floor, stairs ...
            pyxel.cls(0)
            pyxel.blt(self.donkey.posX, self.donkey.posY, 0, self.donkey.image*48, 56, 48, 40, colkey=0)
            pyxel.blt(self.princess.posX, self.princess.posY, 0, 0, 176, 24, 26, colkey=0)
            pyxel.blt(constants.b_posX, constants.b_posY, 1, 16, 0, 24, 36, colkey=0)
            pyxel.blt(constants.bfire_posX, constants.bfire_posY, 0, 8, 0, 16, 16, colkey=0)
            pyxel.blt(constants.fire_posX, constants.fire_posY, 0, 24 + self.kind*15, 0, 15, 16, colkey=0)
            
            #TEXTS AND SCORES
            score = "{:06}".format(self.sticker.score)
            pyxel.blt(constants.text_posX, constants.text_posY, 0, 181, 100, 44, 20, colkey=0)
            pyxel.text(constants.text_posX+9, constants.text_posY+9, score, 7)
            #pyxel.text(constants.text_posX, constants.text_posY + 8, score, 7)
            pyxel.text(constants.lives_posX, 5, "LIVES", pyxel.frame_count%10)
            pyxel.blt(constants.lives_posX, constants.lives_posY, 1, 16, 32, (self.sticker.lives*8), 8, colkey=0)
            #ponemos que cuando mario llega el "HELP" se va y aparece el corazon
            
            #STAIRS
            for i in self.stairs:
                pyxel.blt(i.posX, i.posY, 0, 0, 18, 8, 6, colkey=0)          
                        
            #BARRAS
            for i in self.bars:
                pyxel.blt(i.posX, i.posY, 0, 0, 8, 8, 8)
           
            #BARRELS
            for i in self.barrels:
                if i.direct == "do":
                    pyxel.blt(i.posX, i.posY, 0, 128 + i.image*16, 104, 16, 10, colkey=0)
                else:
                    pyxel.blt(i.posX, i.posY, 0, 32 + i.image*16, 104, 12, 10, colkey=0)
                
            #MARIO      
            pyxel.blt(self.sticker.posX, self.sticker.posY, 1, 0, self.sticker.Image *16, 16, 16, colkey=0) 
    
            #HEART
            if self.corazon:
                pyxel.blt(constants.c_posX, constants.c_posY, 0, 184, 176, 15, 12, colkey=0)
            
            #HELP
            if self.help:
                pyxel.blt(constants.c_posX, constants.c_posY, 0, 152, 176, 32, 16, colkey=0)
            
            #SCORE
            if self.sticker.sco:
                pyxel.text(self.sticker.posX+16, self.sticker.posY-3, "100", 7)
                if pyxel.frame_count%11 == 0: #only stays 11s
                    self.sticker.sco = False
        else:
            self.draw_death() #we draw the end-screen

# main          
Game()
