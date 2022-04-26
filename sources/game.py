import pygame
from sources.constants import WHITE, RED, BLACK, block_size, left_margin
from sources.constants import right_margin, upper_margin, down_margin, screen
from sources.field import Field
from sources.messages import Messages
from sources.drawing_ship import DrawingShip
from sources.drawing_kill import DrawingKill

human_ships_to_draw_second = set()
human_ships_to_draw_first = set()
pygame.display.set_caption("Sea Battle")

hit_blocks_first = set()
dotted_set_first = set()
hit_blocks_second = set()
dotted_set_second = set()
around_last_computer_hit_set = set()
dotted_set_for_computer_not_to_shoot = set()
hit_blocks_for_computer_not_to_shoot = set()
hit_blocks = set()
dotted_set = set()
len_ship = 0

field_ship_first = [[0] * 100 for i in range(1, 100)]
field_ship_second = [[0] * 100 for i in range(1, 100)]
count = 0
length_of_remaining_ships = [0] * 26


class Game:
    def play_game(self):
        screen.fill(BLACK)
        opponents_ships_list_first = human_ships_to_draw_second
        game_over = False
        computer_turn = False
        drawing = False
        final_mes = Messages(RED)
        screen.fill(BLACK)
        num_ships_list = [0] * 4
        screen.fill(BLACK)
        human_ships_to_draw = []
        human_ships_set = set()
        ship_not_created = True
        count = 1

        ship_drawing = DrawingShip(RED)
        ship_drawing.draw_ship_with_rules_first(human_ships_to_draw_first,
                                                num_ships_list,
                                                human_ships_to_draw,
                                                human_ships_set, count, final_mes,
                                                ship_not_created, drawing,
                                                length_of_remaining_ships,
                                                field_ship_first)
        screen.fill(BLACK)
        num_ships_list = [0] * 4
        screen.fill(BLACK)
        human_ships_to_draw = []
        human_ships_set = set()
        count = 11
        ship_drawing.draw_ship_with_rules_second(human_ships_to_draw_second,
                                                 num_ships_list,
                                                 human_ships_to_draw,
                                                 human_ships_set, count,
                                                 final_mes, ship_not_created,
                                                 drawing,
                                                 length_of_remaining_ships,
                                                 field_ship_second)
        opponents_ships_list_second = human_ships_to_draw_first
        game_over = False
        computer_turn = False
        end_game = False
        ship_drawing_k = DrawingKill()
        first_grid = Field("Second", 0)
        second_grid = Field("First", 15 * block_size)
        while not game_over:
            for event in pygame.event.get():
                if computer_turn and not end_game:
                    final_mes.shoot_text_delete(0)
                    final_mes.shoot_text("The second player makes a shoot", 15)
                elif not end_game:
                    final_mes.shoot_text_delete(15 * block_size)
                    final_mes.shoot_text("The first player makes a shoot", 0)
                pygame.display.update()
                if event.type == pygame.QUIT:
                    game_over = True
                elif not computer_turn and event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (left_margin < x < left_margin + 10 * block_size) and (
                            upper_margin < y < upper_margin + 10 * block_size):
                        fired_block = ((x - left_margin) // block_size + 1,
                                       (y - upper_margin) // block_size + 1)
                        if fired_block in human_ships_to_draw_second:
                            opponents_ships_list_first.remove(fired_block)
                            length_of_remaining_ships[field_ship_second[fired_block[0]][fired_block[1]]] -= 1
                            if (length_of_remaining_ships[field_ship_second[fired_block[0]][fired_block[1]]] == 0):
                                ship_drawing_k.draw_ship_is_kill_end(
                                                                     fired_block,
                                                                     0,
                                                                     dotted_set_first,
                                                                     field_ship_second)
                            hit_blocks_first.add(fired_block)
                            ship_drawing_k.draw_hit_blocks(hit_blocks_first)
                            if len(opponents_ships_list_first) == 0:
                                final_mes.shoot_text_delete(0)
                                final_mes.shoot_text_delete(15 * block_size)
                                final_mes.game_over_name(
                                    "The first player won")
                                end_game = True
                                pygame.display.update()
                        else:
                            dotted_set_first.add(fired_block)
                            ship_drawing_k.draw_from_dotted_set(
                                dotted_set_first)
                            computer_turn = True
                    pygame.display.update()
                elif computer_turn and event.type == pygame.MOUSEBUTTONDOWN:

                    x, y = event.pos
                    if (left_margin + 15 * block_size <
                        x < left_margin + 25 * block_size) and (
                            upper_margin < y < upper_margin + 10 * block_size):
                        fired_block = ((x - left_margin) // block_size + 1,
                                       (y - upper_margin) // block_size + 1)
                        if fired_block in human_ships_to_draw_first:
                            opponents_ships_list_second.remove(fired_block)
                            length_of_remaining_ships[field_ship_first[fired_block[0]][fired_block[1]]] -= 1
                            if (length_of_remaining_ships[field_ship_first[fired_block[0]][fired_block[1]]] == 0):
                                ship_drawing_k.draw_ship_is_kill_end(
                                                                     fired_block,
                                                                     15, dotted_set_second,
                                                                     field_ship_first)
                            hit_blocks_second.add(fired_block)
                            ship_drawing_k.draw_hit_blocks(hit_blocks_second)
                            if len(opponents_ships_list_second) == 0:
                                final_mes.shoot_text_delete(0)
                                final_mes.shoot_text_delete(15 * block_size)
                                final_mes.game_over_name(
                                    "The second player won")
                                end_game = True
                                pygame.display.update()

                        else:
                            dotted_set_second.add(fired_block)
                            ship_drawing_k.draw_from_dotted_set(
                                dotted_set_second)
                            computer_turn = False
                    pygame.display.update()