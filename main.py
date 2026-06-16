from setup import *
from game import Game

scene = Game()

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
        
    scene.draw(screen)

    pygame.display.update()

pygame.quit()