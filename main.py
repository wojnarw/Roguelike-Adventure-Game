from helpers import *
import engine
import ui

KEY_BINDINGS = set()
KEY_BINDINGS = {"left": ("a", "4"),
                "right": ("d", "6"),
                "up": ("w", "8"),
                "down": ("s", "2"),
                "leftUP": ("q", "7"),
                "leftDOWN": ("z", "1"),
                "rightUP": ("e", "9"),
                "rightDOWN": ("c", "3"),
                "inventory": ("i"),
                "exit": ("`", "x"),
                }
PLAYER_ICON = { "head":  "☻",
                "body": "/▒\\", # body should be widest
                "legs":  "∏"
                }
PLAYER_START_X = 4
PLAYER_START_Y = 3

BOARD_WIDTH = 80
BOARD_HEIGHT = 30

GRASS = "ˇ"
WALL = "█"
OBSTACLES = set()
OBSTACLES.add(WALL)
BACKGROUND = " "

def init():
    player = create_player()
    main(player)


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
    player["height"] = len(PLAYER_ICON)
    player["width"] = len(PLAYER_ICON["body"])
    return player


def main(player):

    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    board = engine.draw_walls_and_background(board, WALL, BACKGROUND)
    board = engine.put_player_on_board(board, player)

    clear_screen()
    ui.display_board(board)
    print(player)
    ui.display_stats()
    
    key = key_pressed()
    # I WILL REMOVE MAGIC NUMBERS BELOW LATER
    # vertical movement
    if key in KEY_BINDINGS["up"] and board[player["y"]-1][player["x"]] not in OBSTACLES:
        player["y"] -= 1
    elif key in KEY_BINDINGS["down"] and board[player["y"] + player["height"]][player["x"]] not in OBSTACLES:
        player["y"] += 1
    # horiontal movement
    elif key in KEY_BINDINGS["left"] and board[player["y"]][player["x"]-player["width"]] not in OBSTACLES:
        player["x"] -= 1
    elif key in KEY_BINDINGS["right"] and board[player["y"]][player["x"]+1] not in OBSTACLES:
        player["x"] += 1
    # diagonal movement
    elif key in KEY_BINDINGS["leftUP"] and board[player["y"]-1][player["x"]-player["width"]] not in OBSTACLES:
        player["x"] -= 1
        player["y"] -= 1
    elif key in KEY_BINDINGS["rightUP"] and board[player["y"]-1][player["x"]+1] not in OBSTACLES:
        player["x"] += 1
        player["y"] -= 1
    elif key in KEY_BINDINGS["leftDOWN"] and board[player["y"] + player["height"]][player["x"]-player["width"]] not in OBSTACLES:
        player["x"] -= 1
        player["y"] += 1
    elif key in KEY_BINDINGS["rightDOWN"] and board[player["y"] + player["height"]][player["x"]+1] not in OBSTACLES:
        player["x"] += 1
        player["y"] += 1
    # key binded options
    elif key in KEY_BINDINGS["inventory"]:
        ui.display_inv()
        print("1.Heal", "2.Regen", "3.Exit")
        option = input()
        if option == "1":
            if "HP Potion" in ui.inv:
                ui.HP += 1
                ui.inv.remove("HP Potion")
            else:
                print("No potions")
                pass
        if option == "3":
            pass
    elif key in KEY_BINDINGS["exit"]:
        return

    main(player)


if __name__ == '__main__':
    init()