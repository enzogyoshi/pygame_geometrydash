from setup import *
from player import Player
from tile import Tile, HalfTile
from spike import Spike

class Game:



    def __init__(self, level):
        self.player = Player()
        self.tiles = []
        self.spikes = []

        self.camera_speed = pygame.Vector2(480, 0)   

        self.level = level
        self.import_level()

    def import_level(self):
        with open('pygame_geometrydash/levels/' + self.level + '.txt') as f:
            lines = f.readlines()
            for y, line in enumerate(lines):
                for x, tile_type in enumerate(line.replace(",", "")):
                    if tile_type == "1":
                        self.tiles.append(Tile((x * Tile.width, y * Tile.height)))
                    elif tile_type == "2":
                        self.tiles.append(HalfTile((x * Tile.width, y * Tile.height)))
                    elif tile_type == "3":
                        self.tiles.append(Spike((x * Tile.width, y * Tile.height), 0))




    def update(self, delta):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return COMMAND_QUIT

        player_status = self.player.update(delta, self.tiles, self.spikes)

        if player_status == PLAYER_DEAD:
            return COMMAND_RESTART

        for tile in self.tiles:
            tile.update(delta, self.camera_speed.x)
        for spike in self.spikes:
            spike.update(delta, self.camera_speed.x)

    def draw(self, delta):
        screen.fill((0, 0, 0))
        self.player.draw(screen)
        for tile in self.tiles:
            tile.draw(screen)
        for spike in self.spikes:
            spike.draw(screen)
        
