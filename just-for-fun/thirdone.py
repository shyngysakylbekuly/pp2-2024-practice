import pygame

pygame.init()
screen=pygame.display.set_mode((600,300))
pygame.display.set_caption("Shyngys")


square=pygame.Surface((50,170))
square.fill('Blue')
myfont=pygame.font.Font()

running=True
while running:
    screen.blit(square,(200,100))

    pygame.draw.circle(screen,'Red',(250,150),30)

    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            

        
    