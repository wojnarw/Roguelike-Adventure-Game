from helpers import key_pressed, clear_screen
from const import *
import engine
import ui
import stats
import enemies


def init():
    player = stats.create_player(PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, "map1")
    clear_screen(0)
    main(player, board)


def main(player, board):
    global word_used
    
    board_with_player = engine.put_player_on_board(board, player)

    clear_screen(40)
    ui.display_board(board_with_player, player)
    print(f"\n\tPLAYER X:{player['x']} Y:{player['y']}")
    
    key = key_pressed()
    around_player = 2
    
    # collisions check
    no_obstacle_on_up = board[player["y"]-around_player][player["x"]] in PASSABLE and board[player["y"]-around_player][player["x"]+1] in PASSABLE
    no_obstacle_on_down = board[player["y"] + around_player][player["x"]] in PASSABLE and board[player["y"] + around_player][player["x"]+1] in PASSABLE
    no_obstacle_on_left = board[player["y"]][player["x"]-around_player] in PASSABLE and board[player["y"]+1][player["x"]-around_player] in PASSABLE
    no_obstacle_on_right = board[player["y"]][player["x"]+around_player] in PASSABLE and board[player["y"]+1][player["x"]+around_player] in PASSABLE
    no_obstacle_on_leftUP = board[player["y"]-around_player][player["x"]-around_player] in PASSABLE
    no_obstacle_on_rightUP = board[player["y"]-around_player][player["x"]+around_player] in PASSABLE
    no_obstacle_on_leftDOWN = board[player["y"] + around_player][player["x"]-around_player] in PASSABLE
    no_obstacle_on_rightDOWN = board[player["y"] + around_player][player["x"]+around_player] in PASSABLE
    # move keys pressed
    move_keys = sum(KEY_BINDINGS_MOVE.values(),[])

    if key in move_keys:
        # vertical movement
        if key in KEY_BINDINGS_MOVE["up"] and no_obstacle_on_up:
            player["y"] -= 1
        elif key in KEY_BINDINGS_MOVE["down"] and no_obstacle_on_down:
            player["y"] += 1
        # horiontal movement
        elif key in KEY_BINDINGS_MOVE["left"] and no_obstacle_on_left:
            player["x"] -= 1
        elif key in KEY_BINDINGS_MOVE["right"] and no_obstacle_on_right:
            player["x"] += 1
        # diagonal movement
        elif key in KEY_BINDINGS_MOVE["leftUP"] and no_obstacle_on_leftUP:
            player["x"] -= 1
            player["y"] -= 1
        elif key in KEY_BINDINGS_MOVE["rightUP"] and no_obstacle_on_rightUP:
            player["x"] += 1
            player["y"] -= 1
        elif key in KEY_BINDINGS_MOVE["leftDOWN"] and no_obstacle_on_leftDOWN:
            player["x"] -= 1
            player["y"] += 1
        elif key in KEY_BINDINGS_MOVE["rightDOWN"] and no_obstacle_on_rightDOWN:
            player["x"] += 1
            player["y"] += 1
        
        fight_result = False
        # enemy collision
        if board[player["y"]][player["x"]] in ENEMIES["small"]["icon"] or board[player["y"]][player["x"]+1] in ENEMIES["small"]["icon"]:
            fight_result = enemies.fight_with_monsters_small(player)
        if board[player["y"]][player["x"]] in ENEMIES["big"]["icon"] or board[player["y"]][player["x"]+1] in ENEMIES["big"]["icon"]:
            fight_result = enemies.fight_with_monsters_large(player)

        if fight_result:
            board[player["y"]][player["x"]-1] = " "
            board[player["y"]][player["x"]] = "†"
            board[player["y"]][player["x"]+1] = " "
            ui.player_say(board_with_player, player, "Another one bites the dust!")
            key_pressed()

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
    elif key in KEY_BINDINGS["generator"]:
        engine.generate_new_map(board, player)
    
    elif key in KEY_BINDINGS["clear"]:    
        clear_screen(0)
        
    elif key in KEY_BINDINGS["inventory"]:
        ui.display_inv()
        print("1.Heal", "2.Regen", "~~~Enter to Exit")
        option = input()
        if option == "1":
            if "HP Potion" in ui.inv:
                player["HP"] += 4 + player["intelligence"]
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
            player["experience"] += 100   # Cheat
            player["HP"] += 5
            player["max_hp"] += 5
            stats.level_up(player)
    elif key in KEY_BINDINGS["stats"]:
        stats.display_advenced_stats(player)  # Display stats like attack dmg
        enemies.fight_with_monsters_small(player)
        pass
    elif key in KEY_BINDINGS["exit"]:
        return

    main(player, board)


if __name__ == '__main__':
    init()