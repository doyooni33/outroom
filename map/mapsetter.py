import pygame

settedmap = [[0]*10]*10

seting_x = 0
seting_y = 0

def changetile(tile):
    if tile == 4:
        tile=0
    else :
        tile+=1
    return tile

tile_0 = pygame.image.load("./img/안보이는곳타일.jpg")
tile_1 = pygame.image.load("./")

pygame.init() 

screen_width = 480 
screen_height = 320
size = [600, 480]
screen = pygame.display.set_mode(size, pygame.RESIZABLE) 

pygame.display.set_caption("out to ")

running = True 
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # 창 크기 조절 이벤트 처리
            size = [event.w, event.h]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
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
           # print(settedmap)
            print(settedmap[seting_x][seting_y]) 
            settedmap[seting_x][seting_y] = changetile(settedmap[seting_x][seting_y])
            print(settedmap[seting_x][seting_y])
    
pygame.quit() 
print(settedmap)