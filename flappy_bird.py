from unittest import runner
import pygame
from pygame.locals import *




pygame.init()


DISPLAY_WIDTH = 864
DISPLAY_HEIGTH = 936

CLOCK = pygame.time.Clock()
FPS = 40

# Load imgages
BG = pygame.image.load('Assets/Flappy_bird/bg.png')
GROUND = pygame.image.load('Assets/Flappy_bird/ground.png')
BIRDS = []
for i in range(1,4):
    BIRDS.append(pygame.image.load(f'Assets/Flappy_bird/bird{i}.png'))

surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGTH))
pygame.display.set_caption('Flappy bird')



# ----- FUNCTIONS -----
def draw_background(ground_scroll):
    surface.blit(BG, (0,0))
    surface.blit(GROUND, (ground_scroll % -36, 768))










class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        # Bird image animation
        self.index = 0
        self.counter = 0
        self.images = BIRDS
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

        self.vel = 0

    def update(self):

        # Bird limits
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.bottom > 768:
            self.rect.bottom = 768
        
        # Rotate bird
        self.image = pygame.transform.rotate(self.images[self.index % 3], self.vel * -0.9)
        
    def animate_bird(self):
        self.counter += 1
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index +=1
        self.image = self.images[self.index % 3]
              
    def gravity(self):
        self.vel += 5
        if self.vel > 8:
            self.vel = 8

        self.rect.y += int(self.vel)

    def jump(self):
        self.vel = -35






# ----- INIT VARIABLES -----
game_scroll = 0
flying = False

bird_group = pygame.sprite.Group()
flappy = Bird(100, int(DISPLAY_HEIGTH/2))
bird_group.add(flappy)


# GAME LOOP
game_over = False
running = True
while running:        
    CLOCK.tick(FPS)
    
   
    # --- CHECK BIRD UPDATE ---
    game_over = flappy.update()
    if game_over == True:
        game_scroll = 0
    else:
        game_scroll -= 4
    
    # --- DRAW GAME ---
    draw_background(game_scroll)




    # --- DRAW AND ANIMATE BIRD ---
    bird_group.draw(surface)
    flappy.animate_bird()

    # --- ADD GRAVITY ---
    if flying == True:
        flappy.gravity()

    # --- ADD JUMP ---
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                flying = True
                flappy.jump()
        



        if event.type == QUIT:
            running = False











    pygame.display.flip()



pygame.quit()