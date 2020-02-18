import random

def create_board(width, height):
    '''
    Creates game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board  
    '''
    board = []
    for i in range(height):
        board.append([])
        for e in range(width):
            board[i].append("")
    return board


def put_player_on_board(board, player):
    '''
    Puts the player icon on the board on player coordinates.

    Args:
    list: The game board
    dictionary: The player information - the icon and coordinates

    Returns:
    list: The game board with the player sign on it
    '''
    y = player["y"]
    x = player["x"]

    board[y][x-1] = player["icon"]["head"]

    board[y+1][x-2] = player["icon"]["body"][0]
    board[y+1][x-1] = player["icon"]["body"][1]
    board[y+1][x] = player["icon"]["body"][2]

    board[y+2][x-1] = player["icon"]["legs"]

    return board

    
def customize_character():
    pass


def draw_walls_and_background(board, WALL, BACKGROUND):

    BOARD_HEIGHT = len(board)
    BOARD_WIDTH = len(board[0])

    for i in range(BOARD_HEIGHT):
        for e in range(BOARD_WIDTH):
            if i == 0 or e == 0 or i == BOARD_HEIGHT-1 or e == BOARD_WIDTH-1:
                board[i][e] = WALL
            else:
                board[i][e] = BACKGROUND
    return board


def draw_randomly(board, item, max_items_in_row = 2):

    row_width = len(board[0])

    if isinstance(item, list):
        item_width = len(max(item))
        pass
    elif isinstance(item, str):
        item_width = len(item)

    max_items_in_row = row_width / item_width / 4
    

    return board
