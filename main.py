from setup import *
from game import Game

scene = Game('level1')

delta_time = 0
last_time = pygame.time.get_ticks()

is_running = True
while is_running:

    current_time = pygame.time.get_ticks()
    delta_time = (current_time - last_time) / 1000
    last_time = current_time

    status = scene.update(delta_time)
    if status == COMMAND_QUIT:
        is_running = False

    elif status == COMMAND_RESTART:
        scene = Game("level1")
        
    scene.draw(screen)

    pygame.display.update()

pygame.quit()