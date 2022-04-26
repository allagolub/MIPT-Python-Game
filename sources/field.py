import pygame

from .constants import WHITE, block_size, left_margin
from .constants import upper_margin, down_margin
from .constants import LETTERS, screen, font


class Field:
    def __init__(self, name, shift_field):
        self.name = name
        self.shift_field = shift_field
        self.draw_field_of_play()
        self.name_field()
        self.draw_num()

    def draw_field_of_play(self):
        for i in range(11):
            pygame.draw.line(screen, WHITE, (left_margin + self.shift_field,
                             upper_margin + i * block_size),
                             (left_margin + 10 * block_size + self.shift_field,
                              upper_margin + i * block_size), 2)
            pygame.draw.line(screen, WHITE, (left_margin + i * block_size +
                                             self.shift_field, upper_margin),
                             (left_margin + i * block_size + self.shift_field,
                              upper_margin + 10 * block_size), 2)

    def draw_num(self):
        for i in range(10):
            num = font.render(str(i + 1), True, WHITE)
            letters_hor = font.render(LETTERS[i], True, WHITE)
            screen.blit(num, (left_margin - int(block_size / 1.5),
                              upper_margin + i * block_size +
                              int(block_size / 5)))
            screen.blit(num,
                        (left_margin - int(block_size / 1.5) + 15 *
                         block_size, upper_margin + i * block_size +
                         int(block_size / 5)))
            screen.blit(letters_hor,
                        (left_margin + i * block_size + int(block_size / 3),
                         upper_margin - int(block_size / 1.2)))
            screen.blit(letters_hor,
                        (left_margin + i * block_size + int(block_size / 3) +
                         15 * block_size, upper_margin -
                         int(block_size / 1.2)))

    def name_field(self):
        player = font.render(self.name, True, WHITE)
        screen.blit(player, (left_margin + 4 * block_size + self.shift_field,
                             upper_margin - block_size * 2))
