import pygame

import random
from time import sleep
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
width=1280
height=720
bg=1280
player_width=width*0.05
player_height=height*0.45
enemy_width=190
enemy_height=186
enemy2_width=190
enemy2_height=186
gameDisplay = pygame.display.set_mode((width,height))
pygame.mixer.set_num_channels(3)
pygame.mixer.Channel(0).play(pygame.mixer.Sound('C:/Users/MyCom/Desktop/자바/엘리니아.wav'))
                 
# Player의 Hp를 표시해주는 함수
def drawHp(hp):
    global gamepad
    font=pygame.font.SysFont(None,40)
    text=font.render('Player HP : ' + str(hp),True,white)
    gamepad.blit(text,(13,15))
# Player의 Skill 게이지를 표시해주는 함수
def drawSkill(skill):
    global gamepad
    font=pygame.font.SysFont(None,40)
    text=font.render('SKill : ' + str(skill),True,white)
    gamepad.blit(text,(13,55))
def drawSkillReady(Skill):
    global gamepad
    font=pygame.font.SysFont(None,40)
    if skill>=100:

        skill=100
        text=font.render('SKill is Ready ' + str(skill),True,white)
    else:
        text=font.render('SKill is Ready ' + str(skill),True,white)
    gamepad.blit(text,(13,55))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def textobj(text,font):
    textsurface=font.render(text,True,red)
    return textsurface,textsurface.get_rect()
def dispmessage(text):
    global gamepad

    largetext=pygame.font.Font('freesansbold.ttf',115)
    textsurf,textrect=textobj(text,largeText)
    TextRect.center=((width/2),(height/2))
    gamepad.blit(textsurf,textrect)
    pygame.display.update()
    sleep(2)
    rungame()
def dobject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))

def rungame():
    global gamepad,clock,player,bg1,bg2,enemy,ball,enemy2
    shoot=False
    hit=False
    boom_count=0
    die_count=0
    k=0
    h=0
    e=0
    eb=0
    effectview=0
    ball_xy=[]
    attack_xy=[]
    effect_xy=[]
    effectball_xy=[]
    hp=100
    skill=0
    x=width*0.05
    y=height*45
    x_change=0
    y_change=0
    enemy_x=width
    enemy_y=550
    enemy2_x=width
    enemy2_y=550
    ultra=0

    bg1_x=0
    bg2_x=bg

    crashed=False
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
        if event.type==pygame.KEYDOWN:
                #왼쪽 화살표를 누르면 플레이어 왼쪽으로 이동 
            if event.key==pygame.K_LEFT:
                x_change=-10
                #오른쪽 화살표를 누르면 플레이어 오른쪽으로 이동
            elif event.key==pygame.K_RIGHT:
                x_change=10
                #불공격 조건 SPACE바, 공격의 위치
            elif event.key==pygame.K_UP:

                
                effectball_x=x+player_width-10
                effectball_y=y+73
                if eb==0:
                    effectball_xy.append([effectball_x,effectball_y])
                    
                
                ball_x=x+player_width
                ball_y=y+73
                if k==0:
                    ball_xy.append([ball_x,ball_y])
                #얼음공격 조건 DOWN 누르기, 공격 위치
            elif event.key==pygame.K_DOWN:
                effect_x=x+player_width-10
                effect_y=y+73
                if e==0:
                    effect_xy.append([effect_x,effect_y])
                    
                attack_x=x+player_width-5
                attack_y=y+73
                if h==0:
                    attack_xy.append([attack_x,attack_y])

                
                
        
                
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_change=0
            if event.key==pygame.K_UP:
                eb=0
                try:
                    effectball_xy.remove(ebxy)
                except:
                    pass
            if event.key==pygame.K_DOWN:
                e=0
                try:
                    effect_xy.remove(exy)
                except:
                    pass
           
                
        
        # 배경화면 출력화면 
        bg1_x-=2
        bg2_x-=2
        
        if bg1_x==-bg:
            bg1_x=bg
        if bg2_x==-bg:
            bg2_x=bg

        if bg1_x==-bg:
            bg1_x=bg
        if bg2_x==-bg:
            bg2_x=bg
        dobject(bg1,bg1_x,0)
        dobject(bg2,bg2_x,0)
        
        #적 위치
       
        enemy_x-=6
        if enemy_x<=0:
            enemy_x=width
            enemy_y=580

        enemy2_x-=12
        if enemy2_x<=0:
            enemy2_x=width
            enemy2_y=550
            
        
        

        #플레이어 위치
        x+=x_change
        y+=y_change
        if x<0:
            x=0
        elif x>width-player_width :
            x=width-player_width
        if y<0:
            y=0
        elif y>height*0.65:
            y=height*0.65

        #얼음 공격이 날아가는 위치
        if len(attack_xy)!=0:
                for i,axy in enumerate(attack_xy):
                    h=1
                    axy[0]+=15
                    attack_xy[i][0]=axy[0]
           
            #얼음 공격이 적에게 타격될때의 조건 x,y축 고려
                    if axy[0]>enemy2_x:
                        if axy[1]>=enemy_y-30:
                            
                            attack_xy.remove(axy)
                            hit=True
                            h=0

                        if enemy2_x-x>=0:
                            if axy[0]>=x+(enemy2_x-x)/1.5:
                                h=0
                        else:
                            if axy[0]>x+(width-x)/4:
                                h=0
                        if axy[0]>=width:
                            
                            attack_xy.remove(axy)
                            
               
                    
            #얼음 공격이 불 공격을 해야하는 적에게 타격될때 조건 x,y축 고려
                    if axy[0]>=enemy_x:
                        if axy[1]>=enemy_y-30:
                            try:   
                                attack_xy.remove(axy)
                                hit=True
                                h=0
                            except:
                                pass
                        if enemy_x-x>=0:
                           if axy[0]>=x+(enemy_x-x)/(1.5):
                                h=0
                        else:
                           if axy[0]>=x+(width-x)/4:
                                h=0
                   
        #얼음 공격 이펙트
        if len(effect_xy)!=0:
            for j,exy in enumerate(effect_xy):
                e=1
                exy[0]=x+player_width+100
                effect_xy[j][0]=exy[0]
                
        #불 공격 이펙트
        if len(effectball_xy)!=0:
            for l,ebxy in enumerate(effectball_xy):
                eb=1
                ebxy[0]=x+player_width+100
                effectball_xy[l][0]=ebxy[0]
        

        
        #불 공격이 날아가는 위치
        if len(ball_xy)!=0:
                for i,bxy in enumerate(ball_xy):
                    k=1
                    bxy[0]+=15
                    ball_xy[i][0]=bxy[0]
                    #불 공격이 적에게 타격될때의 조건 x,y축 고려 
                    if bxy[0]>enemy_x:
                        if bxy[1]>=enemy_y-30:
                            ball_xy.remove(bxy)
                            shoot=True
                            k=0
                    if enemy_x-x>=0:
                        if bxy[0]>=x+(enemy_x-x)/(1.5):
                            k=0
                    else:
                        if bxy[0]>=x+(width-x)/4:
                            k=0
                    if bxy[0]>=width:
                        try:
                            ball_xy.remove(bxy)
                        except:
                            pass
                    #불 공격이 얼음 공격을 해야하는 적에게 타격될때 조건 x,y축 고려
                    if bxy[0]>=enemy2_x:
                        if bxy[1]>enemy2_y-30:
                            ball_xy.remove(bxy)
                            shoot=True
                            k=0
                    if enemy2_x-x>=0:
                        if bxy[0]>=x+(enemy2_x-x)/1.5:
                            k=0
                    else:
                        if bxy[0]>=x+(width-x)/4:
                            k=0
                   

                
        
        #HP 감소하는 조건
        
        # 1. 얼음공격 
        if enemy2_x<=x+player_width+30:
            hp-=5
            enemy2_x=width
            enemy2_y=550
        
        # 2. 불공격        
        if enemy_x<=x+30:
            hp-=5
            enemy_x=width
            enemy_y=550
            
        if hp<=0:
            hp=0





        #플레이어 위치 구현
        dobject(player,x,y)
        #HP 구현
        drawHp(hp)
        #Skill 퍼센트 구현
        drawSkill(skill)
        
        #불공격의 위치가 변할때 마다 구현
        if len(ball_xy)!=0:
            for bx,by in ball_xy:
                dobject(ball,bx,by)
                
        #불공격을 안했을때 구현 목록
        if  shoot == 0:
            dobject(enemy,enemy_x,enemy_y)
            dobject(enemy2,enemy2_x,enemy2_y)
        #불공격을 했을때 enemy는 boom이 되어 사라진다 하지만 다른 enemy들은 변화 없음
        else:
            if bxy[0]>enemy_x:
                dobject(enemy2,enemy2_x,enemy2_y)
                dobject(boom,enemy_x,enemy_y)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('C:/Users/MyCom/Desktop/자바/Die.wav'))
                if skill>=100:
                    skill =100
                    enemy_x=width
                    enemy_y=500
                    shoot=False
                else:
                    skill+=1
                    enemy_x=width
                    enemy_y=550
                    shoot=False
            elif bxy[0]>enemy2_x:
                 dobject(miss,enemy2_x-24,enemy2_y-50)
                 dobject(enemy,enemy_x,enemy_y)
                 pygame.mixer.Channel(1).play(pygame.mixer.Sound('C:/Users/MyCom/Desktop/자바/Die.wav'))
                 bxy[0]=0 
                 hp-=5
                 shoot=False
                    
        if len(effectball_xy)!=0:
            for ebx,eby in effectball_xy:
                dobject(effectball,ebx,eby)
                
        # 얼음 공격의 이펙트를 위치에 구현
        if len(effect_xy)!=0:
            for ex,ey in effect_xy:
                dobject(effect,ex,ey)
               
        # 얼음 공격의 위치가 변할떄 마다 구현
        if len(attack_xy)!=0:
            for ax,ay in attack_xy:
                dobject(attack,ax,ay)

       
        #얼음공격을 안했을때 구현 목록
        if  hit == 0:
            dobject(enemy,enemy_x,enemy_y)
            dobject(enemy2,enemy2_x,enemy2_y)
        #얼음공격을 했을때 enemy2는 boom이 되어 사라진다 하지만 다른 enemy들은 변화 없음
    
        else:
            if axy[0]>enemy2_x:
                dobject(enemy,enemy_x,enemy_y)
                dobject(boom,enemy2_x,enemy2_y)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('C:/Users/MyCom/Desktop/자바/Die.wav'))
                if skill>=100:
                    skill =100
                    enemy2_x=width
                    enemy2_y=500
                    hit=False
                else:
                    skill+=1
                    enemy2_x=width
                    enemy2_y=550
                    hit=False
            elif axy[0]>enemy_x:
                
                 dobject(enemy2,enemy2_x,enemy2_y)
                 dobject(miss,enemy_x-24,enemy_y-70)
                 pygame.mixer.Channel(1).play(pygame.mixer.Sound('C:/Users/MyCom/Desktop/자바/Die.wav'))
                 axy[0]=0
                 hp-=5
                 hit=False
        if hp==0:
            gameover()
        if skill>=10:
            ultra=1
            dobject(ultra1img,900,0)
        if skill>=20:
            ultra=2
            dobject(ultra2img,1100,0)
        if ultra==1:
            if event.key==pygame.K_q:
                hp+=20
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('C:/Users/MyCom/Desktop/자바/Recovery.wav'))
                skill-=10
                ultra=0
        if ultra==2:
            if event.key==pygame.K_w:
                dobject(boom,enemy2_x,enemy2_y)
                dobject(boom,enemy_x,enemy_y)
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('C:/Users/MyCom/Desktop/자바/nuclear.wav'))
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('C:/Users/MyCom/Desktop/자바/Die.wav'))
                boom_count+=1
                if boom_count>5:
                    boom_count=0
                enemy_x=width
                enemy_y=550
                enemy2_x=width
                enemy2_y=550
                dobject(enemy,enemy_x,enemy_y)
                dobject(enemy2,enemy2_x,enemy2_y) 
                skill-=20
                ultra=0
        pygame.display.update()
        clock.tick(60)
          

    pygame.quit()
    pygame.mixer.quit()
    quit()


def button(msg,x,y,w,h,ic,ac,action=None):
    pygame.init()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",80)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
def game_intro():
    pygame.init()
    intro=True
    global gamepad
    gamepad=pygame.display.set_mode((width,height))
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        introimg=pygame.image.load('C:/Users/MyCom/Desktop/자바/introimg.jpg')
        largeText = pygame.font.Font(None,115)
        dobject(introimg,0,0)
        TextSurf, TextRect = text_objects('Wizard 1st exam', largeText)
        TextRect.center=((width/2),(height/2))
        gameDisplay.blit(TextSurf,TextRect)
        button("GO!",(width/2)-150,450,300,150,white,green,teach)
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(15)
def teach():
    pygame.init()
    teach=True
    global gamepad
    gamepad=pygame.display.set_mode((width,height))
    while teach:
        for event in pygame.event.get():
            print(event)
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        teachimg=pygame.image.load('C:/Users/MyCom/Desktop/자바/teaching.png')
        dobject(teachimg,0,0)
        button("GO!",(width/2)-150,550,300,150,white,green,initgame)
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(15)
def gameover():
    pygame.init()
    gameDisplay.fill(black)
    gameover=True
    global gamepad
    gameoverimg=pygame.image.load('C:/Users/MyCom/Desktop/자바/gameover.jpg')
    gamepad=pygame.display.set_mode((width,height))
    dobject(gameoverimg,(width/2)-300,100)
    while gameover:
        for event in pygame.event.get():
            print(event)
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
          
        button("RETRY",(width/2)-150,450,300,150,white,green,initgame)
        pygame.display.update()
        clock=pygame.time.Clock()
        clock.tick(15)



def initgame():
    global gamepad,player,clock,bg1,bg2,enemy,ball,boom,enemy2,attack,miss,effect,effectball,ultra1img,ultra2img
    pygame.init()
    gamepad=pygame.display.set_mode((width,height))
    pygame.display.set_caption('법사 전직 시키기')
    player=pygame.image.load('C:/Users/MyCom/Desktop/자바/player.png')
    bg1=pygame.image.load('C:/Users/MyCom/Desktop/자바/background.jpg')
    enemy=pygame.image.load('C:/Users/MyCom/Desktop/자바/enemy.png')
    enemy2=pygame.image.load('C:/Users/MyCom/Desktop/자바/enemy2.png')
    miss=pygame.image.load('C:/Users/MyCom/Desktop/자바/miss.png')
    bg2=bg1.copy()
    boom=pygame.image.load('C:/Users/MyCom/Desktop/자바/boom.png')
    ball=pygame.image.load('C:/Users/MyCom/Desktop/자바/ball.png')
    attack=pygame.image.load('C:/Users/MyCom/Desktop/자바/attack.png')
    effect=pygame.image.load('C:/Users/MyCom/Desktop/자바/effect.png')
    effectball=pygame.image.load('C:/Users/MyCom/Desktop/자바/effectball.png')
    ultra1img=pygame.image.load('C:/Users/MyCom/Desktop/자바/hp.png')
    ultra2img=pygame.image.load('C:/Users/MyCom/Desktop/자바/bomb.png')
    pygame.mixer.init()
    clock=pygame.time.Clock()
    rungame()
    

game_intro()            
