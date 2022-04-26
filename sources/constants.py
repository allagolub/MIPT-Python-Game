import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pygame.font.init()
block_size = 40
left_margin = block_size * 5
right_margin = left_margin + block_size * 25
upper_margin = block_size * 4
down_margin = upper_margin + block_size * 10
size = (right_margin + block_size * 5, down_margin + 4 * block_size)
screen = pygame.display.set_mode(size)
font_size = int(block_size)
font = pygame.font.SysFont('freesansbold.ttf', font_size)
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
