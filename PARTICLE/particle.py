import pygame
import random
import pickle
pygame.init()
size=width,height=(1000,800)
screen=pygame.display.set_mode(size)

particle=[]
px=width/2
py=height/2+200
clock=pygame.time.Clock()
run=True
count=0

while run:
    clock.tick(60)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    moup=pygame.mouse.get_pressed()
    moupos=pygame.mouse.get_pos()
    x,y=moupos
    particle.append([x,y,random.randint(-1,1),random.randint(-3,-1),random.randint(0,20)])
    for i in particle:
        i[0]+=i[2]
        i[1]+=i[3]
        i[4]-=0.1
        i[4]+=0.03
        i[3]+=0.03
        if i[4]<=0:
            particle.pop(particle.index(i))
        pygame.draw.circle(screen,((255,255,255)),(i[0],i[1]),i[4])

    
    pygame.display.update()
pygame.quit()
