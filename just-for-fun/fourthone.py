import pygame, time

pygame.init()
screen=pygame.display.set_mode((612,367))
pygame.display.set_caption("Shyngysgame")
bg=pygame.image.load("just-for-fun/istockphoto-1333010525-612x612.jpg")
walk_right=[
    pygame.image.load("just-for-fun/run1.png"),
    pygame.image.load("just-for-fun/run2.png"),
    pygame.image.load("just-for-fun/run3.png"),
    pygame.image.load("just-for-fun/run4.png"),
    pygame.image.load("just-for-fun/run5.png"),
    pygame.image.load("just-for-fun/run6.png"),
    pygame.image.load("just-for-fun/run7.png"),
]
player_anim_count=0
bg_x=0

player_speed=5
player_x=150
player_y=250

is_jump=False
jump_count=7
fps = 60
f = pygame.time.Clock()

running=True
while running:

    screen.blit(bg, (0,0))
    screen.blit(bg,(bg_x+618,0))
    screen.blit(walk_right[player_anim_count],(player_x,234))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x+=player_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump=True
    else:
        if is_jump>=-7:
            if jump_count>0:
                player_y-=(jump_count**2)/2
            else:
                player_y+=(jump_count**2)/2
            jump_count-=1    
        else:
            is_jump=False
            jump_count=7        
            
    if player_anim_count==6:
        player_anim_count=0
    else:
        player_anim_count+=1  
    if bg_x==-618:
        bg_x=0
    else:
        bg_x-=2    
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()

    f.tick(30)
            
