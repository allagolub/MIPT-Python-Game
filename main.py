import pygame
from sources.constants import WHITE, RED, BLACK, block_size, left_margin
from sources.constants import right_margin, upper_margin, down_margin
from sources.constants import size, LETTERS, font_size, screen, font
from sources.game import Game
from sources.field import Field
from sources.messages import Messages
from sources.drawing_ship import DrawingShip
from sources.drawing_kill import DrawingKill


pygame.init()
pygame.font.init()



def main():
    screen.fill(BLACK)
    first_grid = Field("Second", 0)
    second_grid = Field("First", 15 * block_size)
    game = Game()
    game.play_game()
if __name__ == "__main__":
    main()
    pygame.quit()
