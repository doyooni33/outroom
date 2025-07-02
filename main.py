import pygame

settedmap = []

pygame.init() 


clock = pygame.time.Clock()
screen_width = 480 
screen_height = 320
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game Title")

running = True 
while running:
    df = clock.tick(60)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    
    

    pygame.display.flip()
pygame.quit()
print(settedmap)