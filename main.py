from helpers import *
from const import *
import engine
import ui
import stats


def init():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = engine.draw_walls_and_background(board, WALL, BACKGROUND)
    board = engine.generate_random_things_on_map(board, GRASS, 10, 5)
    #board = engine.generate_random_things_on_map(board, "🌷", 1, 5)
    board = engine.generate_random_things_on_map(board, TREE, 4, 3)
    board = engine.generate_random_things_on_map(board, BUSH, 2, 2)
    main(player, board)


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["icon"] = PLAYER_ICON
    player["height"] = 3
    player["width"] = 5 # body + 2 arms, emojis are wider than single character
    #player = stats.add_stats(player)
    return player
    

def main(player, board):

    board_with_player = engine.put_player_on_board(board, player)

    clear_screen()
    ui.display_board(board_with_player)
    print(player)
    stats.display_basic_stats()
    
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
    elif key in KEY_BINDINGS["inventory"]:
        ui.display_inv()
        print("1.Heal", "2.Regen", "~~~Enter to Exit")
        option = input()
        if option == "1":
            if "HP Potion" in ui.inv:
                stats.HP += 1 + stats.Inteligence
                # If current HP >= maxHP currentHP=MaxHP
                if stats.HP >= stats.max_hp:
                    stats.HP = stats.max_hp
                ui.inv.remove("HP Potion")
            else:
                print("No potions")
                pass
        if option == "2":
            if "Mana Potion" in ui.inv:
                stats.MP += 10 + stats.Inteligence
                ui.inv.remove("Mana Potion")
        else:
            print("No potions")
        if option == "3":
            #pass
            stats.experience += 7
            engine.level_up()
    elif key in KEY_BINDINGS["stats"]:
        stats.display_advenced_stats()  # Display stats like attack dmg
        pass
    elif key in KEY_BINDINGS["customize"]:
        engine.customize_character(player)
    elif key in KEY_BINDINGS["exit"]:
        return

    main(player, board)


if __name__ == '__main__':
    init()