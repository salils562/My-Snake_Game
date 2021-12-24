import pygame
import os
import random
pygame.init()
pygame.mixer.init()
# Setting up colors
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

screen_wid=800
screen_hei=500
display_window=pygame.display.set_mode((screen_wid,screen_hei))
pygame.display.set_caption("Snake Game")
fps=60
# backGround Image
bgimg=pygame.image.load('images\snake.png')
bgimg=pygame.transform.scale(bgimg,(screen_wid,screen_hei)).convert_alpha()
bgimgover=pygame.image.load('images\Game_over.jpg')
bgimgover=pygame.transform.scale(bgimgover,(screen_wid,screen_hei)).convert_alpha()
# setting up clock
clock=pygame.time.Clock()
def Text_display(text,color,x,y):
    font=pygame.font.SysFont(None,40)
    txt=font.render(text,True,color)
    display_window.blit(txt,[x,y])
def built_snake(color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(display_window,color,[x,y,snake_size,snake_size])  
def welcome():
    exit_game=False
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load('sounds\snake_Theme.mp3')
                    pygame.mixer.music.play()
                    gameLoop()
        display_window.blit(bgimg,(0,0)) 
        Text_display("Welcome To Snakes",white,240,300) 
        Text_display("Press Space_key to play-game",white,180,350) 
        pygame.display.update()                 
              
def gameLoop():
    if (not os.path.exists('HighScore.txt')):
        f=open('HighScore.txt','w')
        f.close()
    # setting up score
    score=0
    highscore=0
    # setting snake 
    snake_x=45
    snake_y=55
    snake_size=30
    velocity_x=0
    velocity_y=0
    speed=5
    snk_list=[]
    snk_length=1
    # setting food
    food_x=random.randint(20,screen_wid/2)
    food_y=random.randint(20,screen_wid/2)
    food_size=30
    # exit option
    exit_game=False
    over_game=False
    f=open('HighScore.txt','r')
    HighScore=f.read()
    if HighScore=='':
        highscore=0
    else:
        highscore=int(HighScore)  
    f.close()      
    while not exit_game:
        if over_game:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
            display_window.blit(bgimgover,(0,0))
            Text_display("SAAP MARR GAYA!!",red,280,150)
            Text_display("Press ENTER to play again",red,250,200)
            pygame.display.update()
        else:                
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP: 
                            velocity_y=-(speed)
                            velocity_x=0    
                    if event.key==pygame.K_DOWN:    
                            velocity_y=speed
                            velocity_x=0
                    if event.key==pygame.K_LEFT:    
                            velocity_x=-(speed)
                            velocity_y=0
                    if event.key==pygame.K_RIGHT:    
                            velocity_x=speed
                            velocity_y=0
                    if event.key==pygame.K_MINUS:
                        if speed>1:
                            speed-=1
                    if event.key==pygame.K_EQUALS:
                        if speed<11:
                            speed+=1        
            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                food_x=random.randint(20,screen_wid/2)            
                food_y=random.randint(20,screen_wid/2)
                score+=10
                snk_length+=5
                if highscore<score:
                    highscore=score
                    f=open('HighScore.txt','w')
                    f.write(str(highscore))
                    f.close()
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if snake_x<0 or snake_x>screen_wid or snake_y<0 or snake_y>screen_hei:
                over_game=True  
                pygame.mixer.music.load('sounds\Game_over.mp3') 
                pygame.mixer.music.play() 
            if head in snk_list[0:-1]:
                over_game=True    
                pygame.mixer.music.load('sounds\Game_over.mp3') 
                pygame.mixer.music.play() 
            snake_x=snake_x+velocity_x            
            snake_y=snake_y+velocity_y                       
            display_window.fill(green)
            built_snake(black,snk_list,snake_size)
            pygame.draw.rect(display_window,red,[food_x,food_y,food_size,food_size])
            Text_display("Score: "+str(score),red,5,5)
            Text_display("HighScore: "+str(highscore),red,550,5)
            clock.tick(fps)
            pygame.display.update()            
welcome()