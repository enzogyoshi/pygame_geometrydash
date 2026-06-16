import pygame


pygame.init()

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 640
dimensions = pygame.Vector2(SCREEN_WIDTH, SCREEN_WIDTH)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

COMMAND_QUIT = 0
COMMAND_RESTART = 1

PLAYER_DEAD = 2

pygame.display.set_caption("Jumping Cube")

icon = pygame.Surface((32,32))
icon.fill((0,0,0))

font = pygame.font.SysFont("Arial", 20)
text = font.render("JC", True, (255, 255, 255))
text = pygame.transform.scale(text, (28,28))
icon.blit(text, (2,2))
pygame.display.set_icon(icon)