import pygame
import sys 
import random

pygame.init()

SW, SH = 800, 800

BLOCK_SIZE = 50 #taille de chaque bloc
FONT = pygame.font.Font("Police/font.ttf", BLOCK_SIZE*2) #police d'écriture

screen = pygame.display.set_mode((800, 800)) #taille de la fenetre
pygame.display.set_caption("Jeu snake !") #nom de la fentre
clock = pygame.time.Clock()

img = pygame.image.load('Image/Snake.png') #image de la fenetre
pygame.display.set_icon(img)


def drawGrid(): #creation de la grille
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#4c5e45", rect, 1) #couleur

class Snake: #creer le serpent
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE) #tete
        self.body = [pygame.Rect(self.x, self.y-BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)] #corp
        self.dead = False #on ne meurt pas dès le debut
      

    def update(self): #mouvement
        global apple

        for square in self.body:
             if self.head.x == square.x and self.head.y == square.y:
                 self.dead = True
             if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                 self.dead = True

        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.xdir = 1
            self.ydir = 0
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE) #tete
            self.body = [pygame.Rect(self.x, self.y-BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)] #corp
            self.dead = False
            apple = Apple()

        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE  
        self.head.y += self.ydir * BLOCK_SIZE 
        self.body.remove(self.head)


                          

class Apple:
    def __init__(self): #apparition
        self.x = int(random.randint(0, SW)/BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH)/BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self): #update   
        pygame.draw.rect(screen, "red", self.rect) #couleur de la pomme

drawGrid() #affichage de la grille  

score = FONT.render("1", True, 'black') #score 
score_rect = score.get_rect(center=(SW/2, SH/20)) #position du score
    
snake = Snake()
apple = Apple()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN: #mouvements
            if event.key == pygame.K_s: #s pressé -> bas
                snake.ydir = 1
                snake.xdir = 0 
            elif event.key == pygame.K_z:  #z pressé -> haut 
                snake.ydir = -1
                snake.xdir = 0   
            elif event.key == pygame.K_q:  #q pressé -> gauche 
                snake.ydir = 0
                snake.xdir = -1                
            elif event.key == pygame.K_d:  #d pressé -> droite
                snake.ydir = 0
                snake.xdir = 1      

    snake.update()    

    screen.fill('#c9fcb6')  
    drawGrid() #affichage de la grille  

    apple.update()

    score = FONT.render(f"{len(snake.body) - 1}", True, "black")

  
    pygame.draw.rect(screen, "#185900", snake.head) #couleur tete              
            
    for square in snake.body:
        pygame.draw.rect(screen, "green", square) #couleur corp

    screen.blit(score, score_rect)    

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))   
        apple = Apple()

    pygame.display.update()
    clock.tick(10)
