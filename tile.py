from setup import *


class Tile:
    width, height = 50, 50
    colour= (0, 0 ,0)
    outline_colour = (200, 200, 200)
    outline_width = 4


    def __init__(self, position):
        self.position = pygame.Vector2(position)

    def update(self, delta, camera_speed):
        self.position.x -= camera_speed * delta 

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.position.x, self.position.y, self.width, self.height))
        pygame.draw.rect(screen, self.outline_colour, (self.position.x, self.position.y, self.width, self.height),
                          self.outline_width)

        