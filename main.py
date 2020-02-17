from helpers import *
import engine
import ui

PLAYER_ICON = { "head": "☻",
                "body": "/|\\",
                "legs": "∏"
                }
PLAYER_START_X = 4
PLAYER_START_Y = 3

BOARD_WIDTH = 80
BOARD_HEIGHT = 30

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

    if key == 'w' and board[player["y"]-1][player["x"]] not in OBSTACLES:
        player["y"] -= 1
    elif key == 's' and board[player["y"] + player["height"]][player["x"]] not in OBSTACLES:
        player["y"] += 1
    elif key == 'a' and board[player["y"]][player["x"]-3] not in OBSTACLES:
        player["x"] -= 1
    elif key == 'd' and board[player["y"]][player["x"]+1] not in OBSTACLES:
        player["x"] += 1
    elif key == 'i':
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
    elif key == 'x':
        return

    main(player)


if __name__ == '__main__':
    init()