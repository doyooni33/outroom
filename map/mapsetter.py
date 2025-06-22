import pygame

settedmap = []

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

pygame.quit()
print(settedmap)