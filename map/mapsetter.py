import pygame

settedmap = [[0]*50]*50

seting_x = 0
seting_y = 0

pygame.init() 

screen_width = 480 
screen_height = 320
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Title")

running = True 
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            print("W")
            seting_y += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            print("A")
            seting_y -= 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            print("S")
            seting_x -=1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            print("D") 
            seting_x +=1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("l")
            settedmap[seting_x,seting_y] = 0

pygame.quit()
print(settedmap)