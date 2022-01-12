from typing import Sized
import pygame
import random
import math
from os import path
from pygame import sprite
from pygame.mixer import fadeout



WIDTH = 1000
HEIGHT = 800
FPS = 60
STEP = 7
SIZE = 40

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FlexibleSnake")
clock = pygame.time.Clock()



#class
class Segment(pygame.sprite.Sprite):
    
    def __init__(self,x,y,direcion):
        pygame.sprite.Sprite.__init__(self)
        self.image = segment_img
        self.rect = self.image.get_rect()
        self.radius = 19
        self.direction = direcion
        self.rect.x=x
        self.rect.y=y
        self.lista_x_dozdobycia=[]
        self.lista_y_dozdobycia=[]
        self.direction_dozdobycia=[]
        self.x_move=0
        self.y_move=0

    def spawn(self,x,y,direction):
        if(direction=='right'):
            self.rect.x=x-40
            self.rect.y=y
        if(direction=='left'):
            self.rect.x=x+40
            self.rect.y=y
        if(direction=='up'):
            self.rect.x=x
            self.rect.y=y+40
        if(direction=='down'):
            self.rect.x=x
            self.rect.y=y-40
    
    def keep_distance_x_when_greater(self,front_square_x):
        calculate= front_square_x - self.rect.x 
        out_of_the_range=abs(calculate)-SIZE
        if(abs(calculate)>SIZE):
            if calculate>0:
                self.rect.x+= out_of_the_range
            else:
                self.rect.x+= -out_of_the_range
    def keep_distance_y_when_greater(self,front_square_y):
        calculate= front_square_y - self.rect.y 
        out_of_the_range=abs(calculate)-SIZE
        if(abs(calculate)>SIZE):
            if calculate>0:
                self.rect.y += out_of_the_range
            else:
                self.rect.y += -out_of_the_range
    def keep_distance_y_when_lower(self,front_square_y):
        calculate= front_square_y - self.rect.y 
        out_of_the_range=abs(calculate)-SIZE
        if(abs(calculate)<SIZE):
            if calculate>0:
                self.rect.y += out_of_the_range
            else:
                self.rect.y += -out_of_the_range
    def keep_distance_x_when_lower(self,front_square_x):
        calculate= front_square_x - self.rect.x 
        out_of_the_range=abs(calculate)-SIZE
        if(abs(calculate)<SIZE):
            if calculate>0:
                self.rect.x += out_of_the_range
            else:
                self.rect.x += -out_of_the_range

    def keep_in_frame_y(self):
        if self.rect.y % SIZE != 0:
            if  self.rect.y % SIZE > (SIZE/2):
                self.rect.y += 1
            else:
                self.rect.y -= 1
    def keep_in_frame_x(self):
        if self.rect.x % SIZE != 0:
            if  self.rect.x % SIZE > (SIZE/2):
                self.rect.x += 1
            else:
                self.rect.x -= 1

    def to_waypoint_y(self,distance_to_y):
        if abs(distance_to_y)>STEP:
            if distance_to_y>0:
                self.rect.y+= STEP
            else:
                self.rect.y+= -STEP
        else:
            self.rect.y+= distance_to_y
    def to_waypoint_x(self,distance_to_x):
        if abs(distance_to_x)>STEP:
            if distance_to_x>0:
                self.rect.x+= STEP
            else:
                self.rect.x+= -STEP
        else:
            self.rect.x+= distance_to_x

    def update2(self):
        if len(player.direction_dozdobycia)!=0:
            self.direction=player.direction_dozdobycia[0]

        position=listaSegmentow.index(self)
        
        if position==1:
            if len(player.lista_x_dozdobycia)==0:
                self.rect.y+=player.y_move
                self.rect.x+=player.x_move
                #print(player.x_move)
                #print(player.x_move)

                if self.direction =='right' or self.direction == 'left':
                    self.keep_in_frame_y()
                    self.keep_distance_x_when_lower(player.rect.x)
                else:
                    self.keep_in_frame_x()
                    self.keep_distance_y_when_lower(player.rect.y)

                self.keep_distance_y_when_greater(player.rect.y)
                self.keep_distance_x_when_greater(player.rect.x)

            else:
                if(abs(player.lista_x_dozdobycia[0]-self.rect.x)<STEP and abs(player.lista_y_dozdobycia[0]-self.rect.y)<STEP):

                    player.lista_x_dozdobycia.pop(0)
                    player.lista_y_dozdobycia.pop(0)
                    player.direction_dozdobycia.pop(0)
                    self.update()  
                else:
                    distance_to_y= player.lista_y_dozdobycia[0]- self.rect.y
                    distance_to_x= player.lista_x_dozdobycia[0]- self.rect.x
               
                    self.to_waypoint_y(distance_to_y)
                    self.to_waypoint_x(distance_to_x)
                    
    def update(self):
            self.y_move=self.rect.y
            self.x_move=self.rect.x
            position=listaSegmentow.index(self)

            #self.direction=listaSegmentow[position-1].direction

            if len(listaSegmentow[position-1].direction_dozdobycia)!=0:
                self.direction=listaSegmentow[position-1].direction_dozdobycia[0]
        
            if len(listaSegmentow[position-1].lista_x_dozdobycia)==0:
                self.rect.y+=listaSegmentow[position-1].y_move
                self.rect.x+=listaSegmentow[position-1].x_move
                #print(player.x_move)
                #print(player.x_move)

                if self.direction =='right' or self.direction == 'left':
                    pass
                    self.keep_in_frame_y()
                    self.keep_distance_x_when_lower(listaSegmentow[position-1].rect.x)
                else:
                    self.keep_in_frame_x()
                    self.keep_distance_y_when_lower(listaSegmentow[position-1].rect.y)

                self.keep_distance_y_when_greater(listaSegmentow[position-1].rect.y)
                self.keep_distance_x_when_greater(listaSegmentow[position-1].rect.x)
            else:
                if(abs(listaSegmentow[position-1].lista_x_dozdobycia[0]-self.rect.x)<STEP-1 and abs(listaSegmentow[position-1].lista_y_dozdobycia[0]-self.rect.y)<STEP-1):
                    
                    if((len(listaSegmentow)-1)>position):
                        self.lista_x_dozdobycia.append(listaSegmentow[position-1].lista_x_dozdobycia.pop(0))
                        self.lista_y_dozdobycia.append(listaSegmentow[position-1].lista_y_dozdobycia.pop(0))
                        self.direction_dozdobycia.append(listaSegmentow[position-1].direction_dozdobycia.pop(0))
                    else:
                        listaSegmentow[position-1].lista_x_dozdobycia.pop(0)
                        listaSegmentow[position-1].lista_y_dozdobycia.pop(0)
                        listaSegmentow[position-1].direction_dozdobycia.pop(0)

                    self.update()  
                else:
                    distance_to_y= listaSegmentow[position-1].lista_y_dozdobycia[0]- self.rect.y
                    distance_to_x= listaSegmentow[position-1].lista_x_dozdobycia[0]- self.rect.x
               
                    self.to_waypoint_y(distance_to_y)
                    self.to_waypoint_x(distance_to_x)

            self.y_move=self.rect.y-self.y_move
            self.x_move=self.rect.x-self.x_move

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.transform.scale(player_img, (50, 38))
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 15
        pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        #self.rect.centerx = WIDTH / 2
        #self.rect.bottom = HEIGHT - 10
        self.rect.x=300
        self.rect.y=600
        self.direction = 'up'
        self.listofmoves = []
        self.lista_x_dozdobycia=[]
        self.lista_y_dozdobycia=[]
        self.direction_dozdobycia=[]
        self.x_move=0
        self.y_move=0
        #self.lista_x_dozdobycia.append(self.rect.x)
        #self.lista_y_dozdobycia.append(self.rect.y)

    def outofmap(self):
        if self.rect.x+SIZE > WIDTH or self.rect.x <0:
            return True
        if self.rect.y+SIZE > HEIGHT or self.rect.y <0:
            return True
        return False

    def update(self):

        #self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.direction!='right':
            self.lista_x_dozdobycia.append(self.rect.x)
            self.lista_y_dozdobycia.append(self.rect.y)
            self.direction = 'left'
            self.direction_dozdobycia.append(self.direction)
        if keystate[pygame.K_RIGHT] and self.direction!='left':
            self.lista_x_dozdobycia.append(self.rect.x)
            self.lista_y_dozdobycia.append(self.rect.y)    
            self.direction = 'right'
            self.direction_dozdobycia.append(self.direction)
        if keystate[pygame.K_UP] and self.direction!='down':
            self.direction = 'up'
            self.lista_x_dozdobycia.append(self.rect.x)
            self.lista_y_dozdobycia.append(self.rect.y) 
            self.direction_dozdobycia.append(self.direction)   
        if keystate[pygame.K_DOWN] and self.direction!='up':
            self.lista_x_dozdobycia.append(self.rect.x)
            self.lista_y_dozdobycia.append(self.rect.y)    
            self.direction = 'down'
            self.direction_dozdobycia.append(self.direction)
       
        self.y_move=self.rect.y
        self.x_move=self.rect.x
        #update head
        if self.direction == 'left':
            self.rect.x -= STEP
        if self.direction == 'right':
            self.rect.x += STEP
        if self.direction == 'up':
            self.rect.y -= STEP
        if self.direction == 'down':
            self.rect.y += STEP

        #koryguj
        #Wygładza ruch i sprowadza węza do "ramek"
        if self.rect.y % SIZE != 0:
            if  self.rect.y % SIZE > (SIZE/2):
                self.rect.y += 1
            else:
                self.rect.y -= 1
        if self.rect.x % SIZE != 0:
            if  self.rect.x % SIZE > (SIZE/2):
                self.rect.x += 1
            else:
                self.rect.x -= 1

        self.y_move=self.rect.y-self.y_move
        self.x_move=self.rect.x-self.x_move

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(appple_img, (40, 40))
        #self.image = appple_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randint(1,24)*SIZE
        self.rect.y = random.randint(1,19)*SIZE



class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50
        self.listaSegmentowDeadx=[]
        self.listaSegmentowDeady=[]
    def update(self):

        
        i=0
        if self.frame==0:
            for x in listaSegmentow:
                self.listaSegmentowDeadx.append(x.rect.x)
                self.listaSegmentowDeady.append(x.rect.y)
                i+=1
               
        i=0
        for x in listaSegmentow:
            x.rect.x=self.listaSegmentowDeadx[i]
            x.rect.y=self.listaSegmentowDeady[i]
            i+=1


        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
                the_end_list[0]=True
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                
                self.rect = self.image.get_rect()
                self.rect.center = center

                

# Load all game graphics
background = pygame.image.load("bettergrass2.png").convert()
background_rect = background.get_rect()
segment_img = pygame.image.load("block.jpg").convert()
player_img = pygame.image.load("block.jpg").convert()
appple_img = pygame.image.load("apple5.png").convert()


explosion_anim = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (90, 90))
    explosion_anim.append(img_lg)



def drawLine():
    for i in range(1,25):
        pygame.draw.line(screen,BLACK,(i*SIZE,0),(i*SIZE,HEIGHT),1)
    for i in range(1,25):
        pygame.draw.line(screen,BLACK,(0,i*SIZE),(WIDTH,i*SIZE),1)


font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def show_go_screen():
    
    screen.blit(background, background_rect)
    draw_text(screen, "FlexibleSnake", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Użyj strzałek do poruszana się", 28,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Wcisnij strzałkę w górę aby rozpocząć", 22, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_UP]:
                waiting = False

def deathseqence():
    if len(the_end)==0:
        expl = Explosion(player.rect.center)
        all_sprites.add(expl)
        the_end.add(expl)
        print("przegrales")

# Game loop
game_over = True
the_end_list=[game_over]
running = True
while running:
    if the_end_list[0]:
        show_go_screen()
        all_sprites = pygame.sprite.Group()
        apples_sprites = pygame.sprite.Group()
        segments_sprites = pygame.sprite.Group()
        body_sprites= pygame.sprite.Group()
        the_end= pygame.sprite.Group()
        player = Player()
        segment = Segment(player.rect.x,player.rect.y,player.direction)
        apple = Apple()
        segments_sprites.add(segment)
        all_sprites.add(player)
        all_sprites.add(apple) 
        apples_sprites.add(apple)
        listaSegmentow=[player,segment]
        the_end_list[0]=False
        score = 0
    #drawLine()
    
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    segments_sprites.update()

    

    if player.outofmap():
        deathseqence()

    # check to see if a mob hit the player
    # Automatycznie usuwa obiekty które się dotknęły gdy jest true
    hits = pygame.sprite.spritecollide(player, apples_sprites, False, pygame.sprite.collide_circle)
    if hits:
        apple.kill()
        collide=True

        while collide:
            apple = Apple()
            all_sprites.add(apple)
            apples_sprites.add(apple)
            place= pygame.sprite.spritecollide(apple, segments_sprites, False, pygame.sprite.collide_circle)
            if place:
                continue
            else:
                collide=False


        segment = Segment(listaSegmentow[len(listaSegmentow)-1].rect.x, listaSegmentow[len(listaSegmentow)-1].rect.y,listaSegmentow[len(listaSegmentow)-1].direction)
        segment.spawn(listaSegmentow[len(listaSegmentow)-1].rect.x,listaSegmentow[len(listaSegmentow)-1].rect.y,listaSegmentow[len(listaSegmentow)-1].direction)
        segments_sprites.add(segment)
        body_sprites.add(segment)
        listaSegmentow.append(segment)
        score+=1

    hits = pygame.sprite.spritecollide(player, body_sprites, False, pygame.sprite.collide_circle)
    if hits:
        
        if len(the_end)==0:
            expl = Explosion(player.rect.center)
            all_sprites.add(expl)
            the_end.add(expl)
            print("przegrales")
        

        
        

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    segments_sprites.draw(screen)
    #drawRect()
    drawLine()
    draw_text(screen, str(score), 40, WIDTH / 2, 10)
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

