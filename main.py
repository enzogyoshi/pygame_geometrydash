from setup import *
from player import Player


p = Player()

delta_time = 0
last_time = pygame.time.get_ticks()

is_running = True
while is_running:

    current_time = pygame.time.get_ticks()
    delta_time = (current_time - last_time) / 1000
    last_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    p.update(delta_time)

    screen.fill((0, 0, 0))
    p.draw(screen)

    pygame.display.update()

pygame.quit()