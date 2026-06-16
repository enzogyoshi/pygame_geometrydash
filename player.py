from setup import *

class Player:

    width, height = 50, 50
    gravity = pygame.Vector2(0, 1900)
    colour = (255, 0, 0)
    outline_color = (128, 0, 0)
    outline_width = 4


    def __init__(self):
        self.position = pygame.Vector2(SCREEN_WIDTH/5, SCREEN_HEIGHT*2/3)
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0, self.gravity.y)

    def update(self, delta):
        self.velocity += self.acceleration * delta
        self.position += self.velocity * delta

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.position.x, self.position.y, self.width, self.height))
        pygame.draw.rect(screen, self.outline_color, (self.position.x, self.position.y, self.width, self.height),
                          self.outline_width)

