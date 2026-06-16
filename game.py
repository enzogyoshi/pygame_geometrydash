from setup import *
from player import Player
from tile import Tile

class Game:



    def __init__(self):
        self.player = Player()
        self.tiles = [Tile((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))]
        self.camera_speed = pygame.Vector2(300, 0)    

    def update(self, delta):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_QUIT

        self.player.update(delta)
        for tile in self.tiles:
            tile.update(delta, self.camera_speed.x)

    def draw(self, delta):
        screen.fill((0, 0, 0))
        self.player.draw(screen)
        for tile in self.tiles:
            tile.draw(screen)
        
