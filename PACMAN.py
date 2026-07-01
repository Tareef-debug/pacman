import pygame
import random
pygame.init()
#screen
screen = pygame.display.set_mode((600,600)) #width 1st height 2nd
#title
pygame.display.set_caption("Pacman Game")
#init ur fonts(u win and game oveer)
score_font=pygame.font.SysFont(None,30)#30-fontsize
over_font= pygame.font.SysFont(None,60)
#init images
pacman=pygame.transform.scale(pygame.image.load("pacman.png"),(30,30))
food=pygame.transform.scale(pygame.image.load("EATINGFOOD.png")(10,10))
ghost=pygame.transform.scale(pygame.image.load("Ghost.png")(30,30))
#plyer pos
px,py=300,300
ghosts=[[100,400],[300,250],[500,450]]
foods=[]
for x in range(60,550,60):
    for y in range(60,550,60):
        foods.append([x,y])
score=0
lives=5
game_over = False
win=False
while True:
    screen.fill(pygame.color("violet"))
    #get events
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()#close pygame
    #check if game over
    if not game_over and not win:
        keys = pygame.key.get_pressed()
        #W A S D keys
        if keys[pygame.k_d]:
            px-=5
        if keys[pygame.k_a]:
            px+=5
        if keys[pygame.k_w]:
            py-=5
        if keys[pygame.k_s]:
            py+=5
