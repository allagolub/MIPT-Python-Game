import pygame

from .constants import WHITE, BLACK, block_size, left_margin, upper_margin, RED
from .constants import screen, font, down_margin
from .field import Field

human_ships_to_draw_second = set()
human_ships_to_draw_first = set()
hit_blocks_first = set()
hit_blocks_second = set()
dotted_set_second = set()
around_last_computer_hit_set = set()
dotted_set_for_computer_not_to_shoot = set()
hit_blocks_for_computer_not_to_shoot = set()
hit_blocks = set()
dotted_set = set()

field_ship_first = [[0] * 100 for i in range(1,100)]
field_ship_second = [[0] * 100 for i in range(1,100)]
count = 0
length_of_remaining_ships = [0] * 26

class DrawingShip:
    def __init__(self, color):
        self.color = color

    def near_safe(self, ship, near_ship_set):
        for block in ship:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    near_ship_set.add((block[0] + i, block[1] + j))
        return near_ship_set

    def draw_ship_with_rules_first(self, human_ships_to_draw_first, num_ships_list, human_ships_to_draw, human_ships_set, count, final_mes,
                                   ship_not_created, drawing, length_of_remaining_ships, field_ship_first):
        flag = True
        start = (0, 0)
        ship_size = (0, 0)
        near_ship_set = set()
        human_ships_to_draw_first
        while ship_not_created:
            final_mes.arrange_the_ships("First player arranges the ships", 17)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    ship_not_created = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    drawing = True
                    x_start, y_start = event.pos
                    start = x_start, y_start
                    ship_size = (0, 0)
                elif drawing and event.type == pygame.MOUSEMOTION:
                    x_end, y_end = event.pos
                    end = x_end, y_end
                    ship_size = x_end - x_start, y_end - y_start
                elif drawing and event.type == pygame.MOUSEBUTTONUP:
                    x_end, y_end = event.pos
                    drawing = False
                    ship_size = (0, 0)
                    start_block = ((x_start - left_margin) // block_size + 1,
                                   (y_start - upper_margin) // block_size + 1)
                    end_block = ((x_end - left_margin) // block_size + 1,
                                 (y_end - upper_margin) // block_size + 1)

                    max_len = max(
                        abs((y_start - upper_margin) // block_size + 1 - (
                                    (y_end - upper_margin) // block_size + 1)),
                        abs((x_start - left_margin) // block_size + 1 - (
                                    (x_end - left_margin) // block_size + 1))) + 1
                    if start_block > end_block:
                        start_block, end_block = end_block, start_block
                    temp_ship = []
                    wrong = 15 < start_block[0] < 26 and 0 < start_block[1] < 11 and 15 < end_block[
                        0] < 26 and 0 < end_block[1] < 11
                    screen.fill(BLACK)
                    if wrong:

                        screen.fill(BLACK)
                        if start_block[0] == end_block[0] and (end_block[1] - start_block[1]) < 4:
                            for block in range(start_block[1], end_block[1] + 1):
                                temp_ship.append((start_block[0], block))
                        elif start_block[1] == end_block[1] and (end_block[0] - start_block[0]) < 4:
                            for block in range(start_block[0], end_block[0] + 1):
                                temp_ship.append((block, start_block[1]))
                    if temp_ship:
                        for i in temp_ship:
                            human_ships_to_draw_first.add(i)
                        temp_ship_set = set(temp_ship)
                        if (not (temp_ship_set.intersection(near_ship_set))):
                            if (5 - max_len) > num_ships_list[max_len - 1]:
                                num_ships_list[max_len - 1] += 1
                                human_ships_to_draw.append(temp_ship)
                                human_ships_set |= temp_ship_set
                                near_ship_set = self.near_safe(temp_ship, near_ship_set)
                                field_count(start_block, end_block, field_ship_first, count)
                                length_of_remaining_ships[count] = max_len
                                count += 1
                            else:
                                flag = False

                if len(human_ships_to_draw) == 10:
                    ship_not_created = False
            if (flag):
                pygame.draw.rect(screen, WHITE, (start, ship_size), 3)
                draw_ships(human_ships_to_draw)
            else:
                pygame.display.update()
            flag = True
            pygame.display.update()
            first_grid = Field("Second", 0)
            second_grid = Field("First", 15 * block_size)
        screen.fill(BLACK)
        first_grid = Field("Second", 0)
        second_grid = Field("First", 15 * block_size)
        pygame.display.update()

    def draw_ship_with_rules_second(self,human_ships_to_draw_second,num_ships_list, human_ships_to_draw,
                                    human_ships_set, count, final_mes, ship_not_created, drawing, length_of_remaining_ships, field_ship_second):
        flag = True
        start = (0, 0)
        ship_size = (0, 0)
        near_ship_set = set()
        human_ships_to_draw_second
        while ship_not_created:
            final_mes.arrange_the_ships("Second player arranges the ships", 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    ship_not_created = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    drawing = True
                    x_start, y_start = event.pos
                    start = x_start, y_start
                    ship_size = (0, 0)
                elif drawing and event.type == pygame.MOUSEMOTION:
                    x_end, y_end = event.pos
                    end = x_end, y_end
                    ship_size = x_end - x_start, y_end - y_start
                elif drawing and event.type == pygame.MOUSEBUTTONUP:
                    x_end, y_end = event.pos
                    drawing = False
                    ship_size = (0, 0)
                    start_block = ((x_start - left_margin) // block_size + 1,
                                   (y_start - upper_margin) // block_size + 1)
                    end_block = ((x_end - left_margin) // block_size + 1,
                                 (y_end - upper_margin) // block_size + 1)

                    max_len = max(
                        abs((y_start - upper_margin) // block_size + 1 - ((y_end - upper_margin) // block_size + 1)),
                        abs((x_start - left_margin) // block_size + 1 - ((x_end - left_margin) // block_size + 1))) + 1
                    if start_block > end_block:
                        start_block, end_block = end_block, start_block
                    temp_ship = []
                    wrong = 0 < start_block[0] < 11 and 0 < start_block[1] < 11 and 0 < end_block[0] < 11 and 0 < end_block[1] < 11
                    screen.fill(BLACK)
                    if wrong:
                        screen.fill(BLACK)
                        if start_block[0] == end_block[0] and (end_block[1] - start_block[1]) < 4:
                            for block in range(start_block[1], end_block[1] + 1):
                                temp_ship.append((start_block[0], block))
                        elif start_block[1] == end_block[1] and (end_block[0] - start_block[0]) < 4:
                            for block in range(start_block[0], end_block[0] + 1):
                                temp_ship.append((block, start_block[1]))
                    if temp_ship:
                        for i in temp_ship:
                            human_ships_to_draw_second.add(i)
                        temp_ship_set = set(temp_ship)
                        if (not (temp_ship_set.intersection(near_ship_set))):
                            if (5 - max_len) > num_ships_list[max_len - 1]:
                                num_ships_list[max_len - 1] += 1
                                human_ships_to_draw.append(temp_ship)
                                human_ships_set |= temp_ship_set
                                near_ship_set = self.near_safe(temp_ship, near_ship_set)
                                field_count(start_block, end_block, field_ship_second, count)
                                length_of_remaining_ships[count] = max_len
                                count += 1
                            else:
                                flag = False
                if len(human_ships_to_draw) == 10:
                    ship_not_created = False
            if (flag):
                pygame.draw.rect(screen, WHITE, (start, ship_size), 3)
                draw_ships(human_ships_to_draw)


            else:
                pygame.display.update()
            flag = True
            pygame.display.update()
            first_grid = Field("Second", 0)
            second_grid = Field("First", 15 * block_size)
        screen.fill(BLACK)

        pygame.display.update()

def field_count(start_block, end_block, field_ship, count):
    if start_block[0] == end_block[0]:
        for i in range(start_block[1], end_block[1] + 1):
                field_ship[start_block[0]][i] = count
    else:
        for i in range(start_block[0], end_block[0] + 1):
            field_ship[i][start_block[1]] = count
def draw_ships(ships_coordinates_list):
    for elem in ships_coordinates_list:
        ship = sorted(elem)
        x_start = ship[0][0]
        y_start = ship[0][1]
        ship_width = block_size * len(ship)
        ship_height = block_size
        if len(ship) > 1 and ship[0][0] == ship[1][0]:
            ship_width, ship_height = ship_height, ship_width
        x = block_size * (x_start - 1) + left_margin
        y = block_size * (y_start - 1) + upper_margin
        pygame.draw.rect(screen, RED, ((x, y), (ship_width, ship_height)), width=block_size // 8)
