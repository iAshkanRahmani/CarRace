import pygame
import time
import random
pygame.init()

#colors 

blue = (127, 255, 212)
purple = (138, 43, 226)
orange_red = (255, 69, 0)
white = (255,255,255)
light_steel_blue = (176,196,222)

#display resoulion   ====  width and height for game window
display_width = 800
display_height = 600

gameDisplay=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Python Game Race")

clock = pygame.time.Clock()

carimg = pygame.image.load('gg.png')

def stuff(stuffx,stuffy,stuffw,stuffh,color):
    pygame.draw.rect(gameDisplay,color,[stuffx,stuffy,stuffw,stuffh])

def car(x,y):
    gameDisplay.blit(carimg,(x,y))
def text_objects(text,font):
    textSurface = font.render(text ,True , orange_red)
    return textSurface , textSurface.get_rect()
def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf',90)
    TextSurf , TextRect = text_objects(text,large_text)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop()
    
def crash():
    message_display('! YOU CRASHED !')  

car_width = 48
def game_loop():
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    x_change = 0
    
    stuff_startx = random.randrange(0,display_width)
    stuff_starty = -600
    stuff_speed = 8
    stuff_witdth = 100
    stuff_height = 100
    
    GameExit = False
    
    while not GameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameExit = True
                pygame.quit()
                quit()
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
        
        #stuff(stuffx,stuffy,stuffw,stuffh,color)
        stuff(stuff_startx,stuff_starty,stuff_witdth,stuff_height,purple)
        stuff_starty += stuff_speed
        
        car(x,y)   
        
        if x > display_width - car_width or x < 0:
            crash()
        
        if stuff_starty > display_height:
            stuff_starty = 0 - stuff_height
            stuff_startx = random.randrange(0,display_width)
            
        pygame.display.update()
        clock.tick(60)

game_loop()    
pygame.quit()
quit()