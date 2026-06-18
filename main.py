import setup
from setup import *
from game import Game

scene = Game('level1')

delta_time = 0
last_time = pygame.time.get_ticks()

font_hud = pygame.font.SysFont("Arial", 30, bold=True)
game_over = False
won = False

is_running = True
while is_running:

    current_time = pygame.time.get_ticks()
    delta_time = (current_time - last_time) / 1000
    last_time = current_time


    if not won:
        status = scene.update(delta_time)
        
        if status == COMMAND_QUIT:
            is_running = False

        elif status == COMMAND_RESTART:
            setup.ATTEMPTS += 1
            scene = Game("level1")
            
        elif status == COMMAND_WIN:
            won = True
            
  
    scene.draw(delta_time)


    text_attempts = font_hud.render(f"ATTEMPT {setup.ATTEMPTS}", True, (255, 255, 255))
    screen.blit(text_attempts, (SCREEN_WIDTH // 2 - text_attempts.get_width() // 2, 50))

 
    if won:
        text_win = font_hud.render("FASE CONCLUÍDA!", True, (0, 255, 0))
        screen.blit(text_win, (SCREEN_WIDTH // 2 - text_win.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.update()

pygame.quit()