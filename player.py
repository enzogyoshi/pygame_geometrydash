from setup import *

class Player:

    width, height = 50, 50
    gravity = pygame.Vector2(0, 3500)
    colour = (255, 0, 0)

    outline_color = (128, 0, 0)
    outline_width = 4

    jump_velocity = -970
    jump_cooldown_amount = 0

    def __init__(self):
        self.position = pygame.Vector2(SCREEN_WIDTH//5, SCREEN_HEIGHT*3//4)
        self.velocity = pygame.Vector2(0,0)
        self.acceleration = pygame.Vector2(0, self.gravity.y)

        self.on_ground = False
        self.jumped = False
        self.jump_cooldown = 0

    def update(self, delta, tiles, spikes):
 
        self.jump_cooldown = max(0, self.jump_cooldown - delta)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.jump()

        self.velocity.y += self.acceleration.y * delta
        self.position.y += self.velocity.y * delta
        self.on_ground = False

        for spike in spikes:
            if self.colliding(spike.position.x, spike.position.y, spike.width, spike.height):
                return PLAYER_DEAD
            
        for tile in tiles:
            if self.colliding(tile.position.x, tile.position.y, tile.width, tile.height):
                if tile.__class__.__name__ == 'Spike':
                    return PLAYER_DEAD
                if self.velocity.y > 0 and (self.position.y + self.height - self.velocity.y * delta) <= tile.position.y + 10:
                    self.position.y = tile.position.y - self.height
                    self.velocity.y = 0
                    self.on_ground = True
                elif self.velocity.y < 0 and (self.position.y - self.velocity.y * delta) >= tile.position.y + tile.height - 10:
                    self.position.y = tile.position.y + tile.height
                    self.velocity.y = 0
                    return PLAYER_DEAD
                else:
                    return PLAYER_DEAD
                

    def colliding(self, x, y, width, height):
        if (self.position.x < x + width and
                self.position.x + self.width > x and
                self.position.y < y + height and
                self.position.y + self.height > y):
            return True
        return False


    def jump(self):
        if self.jump_cooldown > 0 or not self.on_ground:
            return
        
        self.velocity.y = self.jump_velocity
        self.jump_cooldown = self.jump_cooldown_amount
        self.jumped = True

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.position.x, self.position.y, self.width, self.height))
        pygame.draw.rect(screen, self.outline_color, (self.position.x, self.position.y, self.width, self.height),
                         self.outline_width)