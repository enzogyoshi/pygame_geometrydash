from setup import *
from player import Player
from tile import Tile

class Game:



    def __init__(self):
        self.player = Player()
        self.tiles = [Tile((i, SCREEN_HEIGHT - Tile.height)) for i in range(0, SCREEN_WIDTH * 3, Tile.width)]
        self.camera_speed = pygame.Vector2(300, 0)    

    def update(self, delta):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_QUIT

        self.player.update(delta, self.tiles)
        for tile in self.tiles:
            tile.update(delta, self.camera_speed.x)

    def draw(self, delta):
        screen.fill((0, 0, 0))
        self.player.draw(screen)
        for tile in self.tiles:
            tile.draw(screen)
        
