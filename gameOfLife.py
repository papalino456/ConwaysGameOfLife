import pygame
import random
import numpy as np

width, height = 900, 500
winSize = (width, height)
array = []

pygame.init()
pygame.display.set_caption("The game of life")
screen = pygame.display.set_mode(winSize)

clock = pygame.time.Clock()

class cell():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 1 if random.random() > 0.9 else 0
        self.next = self.state

    def draw(self):
        if self.state == 1:
            square = pygame.draw.rect(screen,(50,50,255),(self.x*10,(self.y*10),9,9))
        else:
            square = pygame.draw.rect(screen,(255,255,255),(self.x*10,(self.y*10),9,9))

def spawn():
    for x in range(90):
        tempArray = []
        for y in range(40):
            Cell = cell(x,y)
            Cell.draw()
            tempArray.append(Cell)
        array.append(tempArray)

def run():
    """ 
            array[x][y] is the cell
             
            [[1,0,1]
             [1,0,0]
             [0,0,0]]

          [ [ (x-1|y-1), (x+0|y-1), (x+1|y-1) ]

            [ (x-1|y+0),   (x|y)  , (x+1|y+0) ]

            [ (x-1|y+1), (x+0|y+1), (x+1|y+1) ] ]

    """
    for x in range(90):
        for y in range(40):
            N=[]
            count = 0
            try:
                N.append(array[x-1][y-1].state)
            except IndexError:
                N.append(0)
            try:
                N.append(array[x][y-1].state)
            except IndexError:
                N.append(0)
            try:
                N.append(array[x+1][y-1].state)
            except IndexError:
                N.append(0)

            try:    
                N.append(array[x-1][y].state)
            except IndexError:
                N.append(0)
            try:    
                N.append(array[x+1][y].state)
            except IndexError:
                N.append(0)

            try:
                N.append(array[x-1][y+1].state)
            except IndexError:
                N.append(0)
            try:
                N.append(array[x][y+1].state)
            except IndexError:
                N.append(0)
            try:
                N.append(array[x+1][y+1].state)
            except IndexError:
                N.append(0)

            for i in N:
                if i == 1:
                    count = count + 1

            if array[x][y].state == 1 and count < 2: #rule 1: Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                array[x][y].next = 0
            if array[x][y].state == 1 and (count == 2 or count == 3): #rule 2: Any live cell with two or three live neighbours lives on to the next generation.
                array[x][y].next = 1
            if array[x][y].state == 1 and count > 3: #rule 3: Any live cell with more than three live neighbours dies, as if by overpopulation.
                array[x][y].next = 0
            if array[x][y].state == 0 and count == 3: #rule 4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                array[x][y].next = 1

def update():
    for x in range(90):
        for y in range(40):
            array[x][y].state = array[x][y].next
            array[x][y].draw()


def main():
    
    running = True
    spawn()
    
    while running:

        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                running = False

        run()
        update()
        pygame.display.update()
        clock.tick(5)

    pygame.quit()



if __name__ == "__main__":
    main()

