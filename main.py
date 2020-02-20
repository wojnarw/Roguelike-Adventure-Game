from helpers import key_pressed, clear_screen
from const import *
import engine
import ui
import stats


def init():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = engine.draw_walls_and_background(board, WALL, BACKGROUND)
    board = engine.generate_random_things_on_map(board, GRASS, 20, 5)
    #board = engine.generate_random_things_on_map(board, ENEMIES["small"]["icon"], 1, 1)

    #board = enemies.place_enemies(board)
    #board = engine.generate_random_things_on_map(board, "🌷", 1, 5)

    board = engine.generate_random_things_on_map(board, TREE3, 4, 3)
    board = engine.generate_random_things_on_map(board, TREE4, 4, 3)
    #board = engine.generate_random_things_on_map(board, BUSH, 2, 2)
    main(player, board)


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "height": 3,
        "width": 5, # body + 2 arms, emojis are wider than single character
        "HP": 5,
        "MP": 10,
        "lvl": 1,
        "experience": 0,
        "max_experience": 100,    # Exp needed to lvl up
        "intelligence": 1,   # Stat making spells and potions deal/heal more
        "strength": 1,      # Stat increasing attack dmg
        "endurance": 1,     # Stat increasing max carry and max hp
        "charisma": 1,      # Make it possible to get bonuses from events
        "max_hp": 10,
        "max_player_carry": 10,    # Maximum carrying size
        "attack": 1   # Dmg Player deal to enemies
    }
    return player


def main(player, board):

    board_with_player = engine.put_player_on_board(board, player)

    clear_screen()
    ui.display_board(board_with_player, player)
    print(f"\n\tPLAYER X:{player['x']} Y:{player['y']}")
    
    key = key_pressed()
    # vertical movement
    if key in KEY_BINDINGS["up"] and board[player["y"]-1][player["x"]] in PASSABLE:
        player["y"] -= 1
    elif key in KEY_BINDINGS["down"] and board[player["y"] + player["height"]][player["x"]] in PASSABLE:
        player["y"] += 1
    # horiontal movement
    elif key in KEY_BINDINGS["left"] and board[player["y"]][player["x"]-player["width"]] in PASSABLE:
        player["x"] -= 1
    elif key in KEY_BINDINGS["right"] and board[player["y"]][player["x"]+1] in PASSABLE:
        player["x"] += 1
    # diagonal movement
    elif key in KEY_BINDINGS["leftUP"] and board[player["y"]-1][player["x"]-player["width"]] in PASSABLE:
        player["x"] -= 1
        player["y"] -= 1
    elif key in KEY_BINDINGS["rightUP"] and board[player["y"]-1][player["x"]+1] in PASSABLE:
        player["x"] += 1
        player["y"] -= 1
    elif key in KEY_BINDINGS["leftDOWN"] and board[player["y"] + player["height"]][player["x"]-player["width"]] in PASSABLE:
        player["x"] -= 1
        player["y"] += 1
    elif key in KEY_BINDINGS["rightDOWN"] and board[player["y"] + player["height"]][player["x"]+1] in PASSABLE:
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
        ui.verbal_attack(board_with_player, player)

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