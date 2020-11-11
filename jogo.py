import pygame, random
from pygame.locals import *

pygame.init() 
screen = pygame.display.set_mode((600, 600)) 
pygame.display.set_caption('Cobra Lombriguenta')

CIMA = 0 
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

direcao = ESQUERDA

cobra = [(200, 200), (210, 200), (220,200)]
cobra_skin = pygame.Surface((10,10)) 
cobra_skin.fill((50,205,50))

def on_grid_random(): 
    x = random.randint(0,590)
    y = random.randint(0,590) 
    return (x//10 * 10, y//10 * 10) 

maca_pos = on_grid_random()
maca = pygame.Surface((10,10)) 
maca.fill((255,0,0))

clock = pygame.time.Clock()

game_over = False
while not game_over:
    
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
        score = 0
        
    def collision(c1, c2):
        return (c1[0] == c2[0]) and (c1[1] == c2[1]) 

    if collision(cobra[0], maca_pos): 
        maca_pos = on_grid_random() 
        cobra.append((0,0))
        score = score + 1
    
    if cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0: 
        game_over = True
        break
    
    for i in range(1, len(cobra) - 1): 
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            game_over = True
            break

    if event.type == KEYDOWN:
        if event.key == K_UP and direcao != BAIXO:
            direcao = CIMA
        if event.key == K_DOWN and direcao != CIMA:
            direcao = BAIXO
        if event.key == K_LEFT and direcao != DIREITA:
            direcao = ESQUERDA 
        if event.key == K_RIGHT and direcao != ESQUERDA:
            direcao = DIREITA
            
    for i in range(len(cobra) - 1, 0, -1): 
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])
      
    if direcao == CIMA:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == BAIXO:

        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == DIREITA:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao == ESQUERDA:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    screen.fill((0,0,0)) 

    screen.blit(maca, maca_pos)
    
    for x in range(0, 600, 10):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600)) 
    for y in range(0, 600, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

    font = pygame.font.Font('freesansbold.ttf', 18)
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (480, 10)
    screen.blit(score_font, score_rect)
    
    for pos in cobra:
        screen.blit(cobra_skin,pos)
    pygame.display.update() 

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect() 
    game_over_rect.midtop = (300, 10) 
    screen.blit(game_over_screen, game_over_rect) 
    pygame.display.update() 
    pygame.time.wait(500) 

    while True: 
        for event in pygame.event.get():
            if event.type == QUIT: 
                pygame.quit() 
                exit()  