import pygame

from .constants import WHITE, BLACK, block_size, left_margin, upper_margin, RED
from .constants import screen, font, down_margin
from .field import Field
from .drawing_ship import DrawingShip


class DrawingKill:
    def draw_from_dotted_set(self, dotted_set_to_draw_from):
        for elem in dotted_set_to_draw_from:
            pygame.draw.circle(screen, WHITE, (block_size * (
                    elem[0] - 0.5) + left_margin, block_size * (elem[1] - 0.5) + upper_margin), block_size // 10)

    def draw_hit_blocks(self, hit_blocks_to_draw_from):
        for block in hit_blocks_to_draw_from:
            x1 = block_size * (block[0] - 1) + left_margin
            y1 = block_size * (block[1] - 1) + upper_margin
            pygame.draw.line(screen, WHITE, (x1, y1),
                             (x1 + block_size, y1 + block_size), block_size // 6)
            pygame.draw.line(screen, WHITE, (x1, y1 + block_size),
                             (x1 + block_size, y1), block_size // 6)

    def draw_ship_is_kill_end(self, fire_block, shift, dotted_set, fild_ship):
        len = 0
        min_coord = (100, 100)
        max_coord = (0, 0)
        dif_min = 0
        dif_max = 0
        for i in range(1, 26):
            for j in range(1, 26):
                if fild_ship[i][j] == fild_ship[fire_block[0]][fire_block[1]]:
                    len += 1
                    if (i < min_coord[0]) or (j < min_coord[1]):
                        min_coord = (i, j)
                    if (i > max_coord[0]) or (j > max_coord[1]):
                        max_coord = (i, j)
        if (min_coord[0] == max_coord[0]):
            dif_min = min_coord[1]
            dif_max = max_coord[1]
            for x in range(dif_min, dif_max + 1):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if ((i > 0) or (i < 0) or (j > 0) or (j < 0)) and (
                                1 + shift <= min_coord[0] + i <= 10 + shift) and (1 <= x + j <= 10):
                            dotted_set.add((min_coord[0] + i, x + j))
                            self.draw_from_dotted_set(dotted_set)


        else:
            dif_min = min_coord[0]
            dif_max = max_coord[0]
            same = min_coord[1]
            for x in range(dif_min, dif_max + 1):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if ((i > 0) or (i < 0) or (j > 0) or (j < 0)) and (1 + shift <= x + i <= 10 + shift) and (
                                1 <= min_coord[1] + j <= 10):
                            dotted_set.add((x + i, min_coord[1] + j))
                            self.draw_from_dotted_set(dotted_set)


