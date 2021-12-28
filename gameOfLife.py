import pygame
import numpy as np
import time

pygame.init()

width,height = 650,650
screen = pygame.display.set_mode((height,width))
background=25,25,25
screen.fill(background)

xCells,yCells = 50,50
dimCellsWidth=width/xCells
dimCellsHeight=height/yCells

#Cell state -> alive=1; dead=0
stateOfGame=np.zeros((xCells,yCells))

#play/pause
pauseExect=False

#Inifinite loop (the game end when the user close the window)
while True:

    newStateOfGame = np.copy(stateOfGame)

    screen.fill(background)
    time.sleep(0.1)

    #Keyboard events
    ev=pygame.event.get()

    for event in ev:
        #Stop/play the game
        if event.type==pygame.KEYDOWN:
            pauseExect=not pauseExect

        mouseClick=pygame.mouse.get_pressed()

        #CHANGE STATE
        #Keeping pressed the left button: if dead => alive (pygame.mouse.get_pressed()==1)
        #Keeping pressed the right button: if alive => dead (pygame.mouse.get_pressed()==2)
        if sum(mouseClick)>0:
            posX,posY=pygame.mouse.get_pos()
            celX,celY=int(np.floor(posX/dimCellsWidth)),int(np.floor(posY/dimCellsHeight))
            newStateOfGame[celX,celY]= not mouseClick[2]

    for y in range(0,xCells):
        for x in range(0,yCells):
            if not pauseExect:
                #Number of closed neighbours
                n_neigh=stateOfGame[(x-1)%xCells,(y-1)%yCells] + \
                        stateOfGame[(x)%xCells,(y-1)%yCells] + \
                        stateOfGame[(x+1)%xCells,(y-1)%yCells] + \
                        stateOfGame[(x-1)%xCells,(y)%yCells] + \
                        stateOfGame[(x+1)%xCells,(y)%yCells] + \
                        stateOfGame[(x-1)%xCells,(y+1)%yCells] + \
                        stateOfGame[(x)%xCells,(y+1)%yCells] + \
                        stateOfGame[(x+1)%xCells,(y+1)%yCells]
                #the % (module) is for the boundary conditions, so we don't have borders
                #we known thar we're working on a grid (xCells*yCells) and we play with that dimensions: [xCells]=[0], [yCells]=[0]

                #1 Rule -> dead with 3 alive neighbours => alive
                if stateOfGame[x,y]==0 and n_neigh==3:
                    newStateOfGame[x,y]=1

                #2 Rule -> alive with less than 2 or more than 3 alive neighbours => dead
                elif stateOfGame[x,y]==1 and (n_neigh<2 or n_neigh>3):
                    newStateOfGame[x,y]=0

                #Is not necessary to implement this rule
                #elif stateOfGame[x,y]==1 and (n_neigh==2 or n_neigh==3):
                #    newStateOfGame[x,y]=1

            #Graphic operations (we sketch the actual situation of the game)
            cell = [((x)*dimCellsWidth,(y)*dimCellsHeight),
                    ((x+1)*dimCellsWidth,(y)*dimCellsHeight),
                    ((x+1)*dimCellsWidth,(y+1)*dimCellsHeight),
                    ((x)*dimCellsWidth,(y+1)*dimCellsHeight)]
            #Draw the cell for each couple x,y
            if newStateOfGame[x,y]==0:
                pygame.draw.polygon(screen,(128,128,128),cell,1)
            else:
                pygame.draw.polygon(screen,(255,255,255),cell,0)

    #update the game state
    stateOfGame=np.copy(newStateOfGame)
    pygame.display.flip()
