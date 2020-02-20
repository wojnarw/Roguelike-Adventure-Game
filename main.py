from helpers import key_pressed, clear_screen
from const import *
import engine
import ui
import stats


def init():
    player = stats.create_player(PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, "map1")
    #board = engine.draw_walls_and_background(board, WALL, BACKGROUND)
    #board = engine.generate_random_things_on_map(board, GRASS, 20, 5)

    #board = engine.generate_random_things_on_map(board, TREES[0], 4,4)
    #board = engine.generate_random_things_on_map(board, TREES[1], 3,3)
    #board = engine.generate_random_things_on_map(board, TREES[2], 4,4)
    main(player, board)


def main(player, board):
    global word_used
    
    board_with_player = engine.put_player_on_board(board, player)

    clear_screen()
    ui.display_board(board_with_player, player)
    print(f"\n\tPLAYER X:{player['x']} Y:{player['y']}")
    
    key = key_pressed()
    around_player = 2
    
    # collisions check
    no_obstacle_on_up = board[player["y"]-around_player][player["x"]] in PASSABLE
    no_obstacle_on_down = board[player["y"] + around_player][player["x"]] in PASSABLE
    no_obstacle_on_left = board[player["y"]][player["x"]-around_player] in PASSABLE and board[player["y"]+1][player["x"]-around_player] in PASSABLE
    no_obstacle_on_right = board[player["y"]][player["x"]+around_player] in PASSABLE and board[player["y"]+1][player["x"]+around_player] in PASSABLE
    no_obstacle_on_leftUP = board[player["y"]-around_player][player["x"]-around_player] in PASSABLE
    no_obstacle_on_rightUP = board[player["y"]-around_player][player["x"]+around_player] in PASSABLE
    no_obstacle_on_leftDOWN = board[player["y"] + around_player][player["x"]-around_player] in PASSABLE
    no_obstacle_on_rightDOWN = board[player["y"] + around_player][player["x"]+around_player] in PASSABLE

    # vertical movement
    if key in KEY_BINDINGS["up"] and no_obstacle_on_up:
        player["y"] -= 1
    elif key in KEY_BINDINGS["down"] and no_obstacle_on_down:
        player["y"] += 1
    # horiontal movement
    elif key in KEY_BINDINGS["left"] and no_obstacle_on_left:
        player["x"] -= 1
    elif key in KEY_BINDINGS["right"] and no_obstacle_on_right:
        player["x"] += 1
    # diagonal movement
    elif key in KEY_BINDINGS["leftUP"] and no_obstacle_on_leftUP:
        player["x"] -= 1
        player["y"] -= 1
    elif key in KEY_BINDINGS["rightUP"] and no_obstacle_on_rightUP:
        player["x"] += 1
        player["y"] -= 1
    elif key in KEY_BINDINGS["leftDOWN"] and no_obstacle_on_leftDOWN:
        player["x"] -= 1
        player["y"] += 1
    elif key in KEY_BINDINGS["rightDOWN"] and no_obstacle_on_rightDOWN:
        player["x"] += 1
        player["y"] += 1
    # key binded options
    elif key in KEY_BINDINGS["overlay"]: # OVERLAY TEST
        ui.show_overlay(board_with_player)
        clear_screen()
        ui.display_board(board_with_player, player)
        input()
    
    elif key in KEY_BINDINGS["customize"]:
        engine.customize_character(player)
    elif key in KEY_BINDINGS["logo"]:
        ui.show_logo_animation(LOGO)
    elif key in KEY_BINDINGS["story"]:
        ui.show_story()
    elif key in KEY_BINDINGS["verbal_attack"]:
        word_used = ui.verbal_attack(board_with_player, player, word_used)
        key_pressed()

    elif key in KEY_BINDINGS["inventory"]:
        ui.display_inv()
        print("1.Heal", "2.Regen", "~~~Enter to Exit")
        option = input()
        if option == "1":
            if "HP Potion" in ui.inv:
                player["HP"] += 1 + player["intelligence"]
                # If current HP >= maxHP currentHP=MaxHP
                if player["HP"] >= player["max_hp"]:
                    player["HP"] = player["max_hp"]
                ui.inv.remove("HP Potion")
            else:
                print("No potions")
                pass
        if option == "2":
            if "Mana Potion" in ui.inv:
                player["MP"] += 10 + player["intelligence"]
                ui.inv.remove("Mana Potion")
        else:
            print("No potions")
        if option == "3":
            #pass
            player["experience"] += 60   # Cheat
            player["HP"] += 5
            player["max_hp"] += 5
            stats.level_up(player)
    elif key in KEY_BINDINGS["stats"]:
        stats.display_advenced_stats(player)  # Display stats like attack dmg
        engine.fight_with_monsters(player)
        pass
    elif key in KEY_BINDINGS["exit"]:
        return

    main(player, board)


if __name__ == '__main__':
    init()