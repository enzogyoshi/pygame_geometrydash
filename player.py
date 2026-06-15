from setup import *

class Player:

    width, height = 50, 50
    gravity = pygame.Vector2(0, 1900)
    colour = (255, 0, 0)


    def __init__(self, pos):
        self.position = pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.velocity = pygame.Vector2(70,0)
        self.acceleration = pygame.Vector2(0,0)

    def update(self, delta):
        self.velocity += self.acceleration * delta
        self.position += self.velocity * delta

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.position.x, self.position.y, self.width, self.height))

