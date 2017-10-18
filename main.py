# Init
import pygame, math, sys
from pygame.locals import *
#Set FPS
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60
deltat = clock.tick(FRAMES_PER_SECOND)
#Create Window
screen = pygame.display.set_mode((1024, 768))


# Check out more functions of pygame.sprite.Sprite
class CarSprite(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 10
    ACCELERATION = 2
    TURN_SPEED = 5

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0

    def update(self, deltat):
        # SIMULATION
        self.speed += (self.k_up + self.k_down)
        if self.speed > self.MAX_FORWARD_SPEED:
            self.speed = self.MAX_FORWARD_SPEED
        if self.speed < -self.MAX_REVERSE_SPEED:
            self.speed = -self.MAX_REVERSE_SPEED
        self.direction += (self.k_right + self.k_left)
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed*math.sin(rad)
        y += -self.speed*math.cos(rad)
        self.position = (x, y)
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

# Creating the Car and running the thing
rect = screen.get_rect()
car = CarSprite('\dataPython\game\img\car.png', rect.center)
car_group = pygame.sprite.RenderPlain(car)

# Really Shoddy 'Main Loop'
while 1:
    # User Input
    deltat = clock.tick(60)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN
        if event.key == K_RIGHT: car.k_right = down * -5
        elif event.key == K_LEFT: car.k_left = down * 5
        elif event.key == K_UP: car.k_up = down * 2
        elif event.key == K_DOWN: car.k_down = down * -2
        elif event.key == K_ESCAPE: sys.exit(0)
    # Rendering
    screen.fill((0,0,0))
    car_group.update(deltat)
    car_group.draw(screen)
    pygame.display.flip()