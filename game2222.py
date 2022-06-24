import pygame
import random
import time
pygame.init()
dx=500
dy=500
game=pygame.display.set_mode((dx,dy))
pygame.display.set_caption("new game")
clock=pygame.time.Clock()
white=(255,120,155)
pimg=pygame.image.load("road.jpg")
img=pygame.image.load("racecar.png")
x=dx//2
y=dy-100

def objects(x,y):
    #pygame.draw.arc(game,(255,255,255),(x,y,x+50,y+50),0,3.14,70)
    pygame.draw.circle(game,(255,255,255),(x,y),30)
##    pygame.draw.ellipse(game,(255,100,200),(x-100,y-20,x,y))
##    pygame.draw.polygon(game,(180,100,20),((300,10),(400,10),(400,90)))
##    pygame.draw.rect(game,(30,40,50),(300,100,400,200))
def  car(hx,hy):
    game.blit(img,(hx,hy))
def comment(score):
    font=pygame.sysfont.SysFont("times",20,bold=True)
    text=font.render("SCORE:"+str(score),True,(255,255,255))
    game.blit(text,(0,0))
    
def crash(score):
    a=pygame.mixer.music.load("crash.mp3")
    pygame.mixer.music.play()
    font=pygame.sysfont.SysFont("times",40,bold=True)
    text=font.render("CRASHED final score:"+str(score),True,(255,255,255))
    game.blit(text,(10,250))
    pygame.display.update()
    


def gameloop():
    a=pygame.mixer.music.load("doom.mp3")
    pygame.mixer.music.play()
    x=dx//2
    y=dy-100
    object_x=random.randrange(0,dx)
    object_y=0
    object_add=2
    score=0
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            elif event.type==pygame.KEYDOWN:
                if (event.key==pygame.K_LEFT) and (x>-20):
                    x-=25+object_add*5
                if (event.key==pygame.K_RIGHT) and(x<390):
                    x+=25+object_add*5
                if event.key==pygame.K_UP:
                    y-=5+object_add*5
                if event.key==pygame.K_DOWN:
                    y+=5+object_add*5
        game.fill(white)
        game.blit(pimg,(0,0))
        if object_y<=dy:
            object_y+=object_add
        else:
            object_x=random.randrange(0,dx)
            object_y=0
            score+=object_add
            object_add=random.randrange(1,20)
        objects(object_x,object_y)
        car(x,y)
        comment(score)
        if (object_x in range(x-25,x+158)) and (object_y in range(y-40,y+158)):
            crash(score)
            time.sleep(2)
            gameloop()
            break
        pygame.display.update()
        clock.tick(60)
    
gameloop()
