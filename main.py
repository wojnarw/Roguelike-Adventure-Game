from helpers import *
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 80
BOARD_HEIGHT = 30

OBSTACLES = set()
OBSTACLES.add("#")

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
    return player


def main(player):

    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    #board = engine.put_player_on_board(board, player)

    for i in range(BOARD_HEIGHT):
        for e in range(BOARD_WIDTH):
            if i == 0 or e == 0 or i == BOARD_HEIGHT-1 or e == BOARD_WIDTH-1:
                board[i][e] = "#"
            elif i == player["y"] and e == player["x"]:
                board[i][e] = "@"
            else:
                board[i][e] = "."

    clear_screen()
    ui.display_board(board)
    key = key_pressed()

    if key == 'w' and board[player["y"]-1][player["x"]] not in OBSTACLES:
        player["y"] -= 1
    elif key == 's' and board[player["y"]+1][player["x"]] not in OBSTACLES:
        player["y"] += 1
    elif key == 'a' and board[player["y"]][player["x"]-1] not in OBSTACLES:
        player["x"] -= 1
    elif key == 'd' and board[player["y"]][player["x"]+1] not in OBSTACLES:
        player["x"] += 1
    elif key == 'x':
        return

    main(player)


if __name__ == '__main__':
    init()