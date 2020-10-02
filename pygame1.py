import pygame

pygame.init()

#colors 

blue = (127, 255, 212)
purple = (138, 43, 226)
orange_red = (255, 69, 0)

#display resoulion   ====  width and height for game window
display_width = 800
display_height = 600

gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Python Game Race")

clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()