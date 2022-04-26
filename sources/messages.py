import pygame

from .constants import RED, BLACK, block_size, left_margin, upper_margin
from .constants import screen, font


class Messages:
    def __init__(self, color):
        self.color = color

    def game_over_name(self, player):
        text = font.render(player, True, RED)
        screen.blit(text, (left_margin + 9 * block_size,
                           upper_margin - 3 * block_size))

    def arrange_the_ships(self, player, shift):
        text = font.render(player, True, RED)
        screen.blit(text, (left_margin + shift * block_size,
                           upper_margin - 3 * block_size))

    def shoot_text(self, player, shift):
        text = font.render(player, True, RED)
        screen.blit(text, (left_margin + shift * block_size, upper_margin - 3 * block_size))

    def shoot_text_delete(self, shift):
        pygame.draw.rect(screen, BLACK, ((left_margin + shift, upper_margin - 3 * block_size),
                                         (block_size * 11.5, block_size)))
