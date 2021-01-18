import pygame
class Direction(object):
    DOWNLEFT =1
    DOWNRIGHT =3 
    UPLEFT = 7
    UPRIGHT =9
class Obj(object):
    def __init__(self):
        self.pos = pygame.Rect(200,200,20,20)
        self.MOVESPEED=4
        self.dir = Direction.UPLEFT
    def move(self):
        if self.dir == Direction.DOWNLEFT:
            self.pos.left -= self.MOVESPEED
            self.pos.top += self.MOVESPEED                              #1 if
        if self.dir == Direction.DOWNRIGHT:                             #2 if 
            self.pos.left += self.MOVESPEED                              
            self.pos.top += self.MOVESPEED
        if self.dir == Direction.UPLEFT:
            self.pos.left -= self.MOVESPEED
            self.pos.top -= self.MOVESPEED
        if self.dir == Direction.UPRIGHT:
            self.pos.left += self.MOVESPEED
            self.pos.top -= self.MOVESPEED
        if self.pos.top<0:
            if self.dir == Direction.UPLEFT:
                self.dir = Direction.DOWNLEFT
            if self.dir == Direction.UPRIGHT:
                self.dir = Direction.DOWNRIGHT
        if self.pos.bottom >600:
            if self.dir == Direction.DOWNLEFT:
                self.dir = Direction.UPLEFT
            if self.dir == Direction.DOWNRIGHT:
                self.dir = Direction.UPRIGHT
        if self.pos.left <0:
            if self.dir == Direction.DOWNLEFT:
                self.dir = Direction.DOWNRIGHT
            if self.dir == Direction.UPLEFT:
                self.dir = Direction.UPRIGHT
        if self.pos.right>800:
            if self.dir == Direction.DOWNRIGHT:
                self.dir = Direction.DOWNLEFT
            if self.dir == Direction.UPRIGHT:
                self.dir = Direction.UPLEFT
pygame.init()
WINDOWHEIGHT = 600
WINDOWWIDTH = 800
FPS = 25
WHITE =(255,255,255)
GREEN= (0,255,0)
window = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
clock = pygame.time.Clock()
nesne = Obj()
while True:
    window.fill(WHITE)
    nesne.move()
    pygame.draw.rect(window,GREEN,nesne.pos)
    pygame.display.flip()
    clock.tick(FPS)
    
             


