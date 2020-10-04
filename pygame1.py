import pygame

pygame.init()

#colors 

blue = (127, 255, 212)
purple = (138, 43, 226)
orange_red = (255, 69, 0)
white = (255,255,255)
#display resoulion   ====  width and height for game window
display_width = 800
display_height = 600

gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Python Game Race")

clock = pygame.time.Clock()

carimg = pygame.image.load('gg.png')

x = (display_width * 0.45)
y = (display_height * 0.8)

x_change = 0

def car(x,y):
    gameDisplay.blit(carimg,(x,y))

GameExit = False

while not GameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0 
            
            
    x += x_change          
    gameDisplay.fill(white) 
    car(x,y)   
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()