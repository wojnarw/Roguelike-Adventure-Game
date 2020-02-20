import random
import main
import stats
import copy
import ui
from const import *
from maps import *
from helpers import key_pressed, clear_screen


def create_board(width, height, maps=""):
    '''
    Creates game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    board = []
    if not maps:
        for line in range(height):
            board.append([])
            for e in range(width):
                board[line].append("")
        return board

    chosen_map = MAPS[random.randint(0, len(MAPS)-1)]
    chosen_map = chosen_map.split("\n")
    if len(chosen_map) < height:
        for y in range(height - len(chosen_map)):
            chosen_map.append("")

    for line in range(height):
        board.append([])
        for e in range(width):
            if len(chosen_map[line]) < width:
                board[line].append(chosen_map[line][e] *
                                   (width - len(chosen_map[line])))
            board[line].append(chosen_map[line][e])
    return board

    """try:
        with open(filename,"r") as file:
            for line in file:
                board.append([])
                for e in range(width):
                    board[line].append(line[e])

    except FileNotFoundError:
        print(f"\tFile '{path_and_filename}' not found!")
        input()"""


def put_player_on_board(original_board, player):
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
    # player["height"]
    # player["width"]

    board = copy.deepcopy(original_board)

    # EMOJIS TAKE 2 SPACES EACH WHEN DISPLAYED
    board[y-1][x] = player["icon"]["head"]
    board[y-1][x+1] = ""

    board[y][x-1] = player["icon"]["leftHand"]
    board[y][x] = player["icon"]["body"]
    #board[y][x+1] = player["icon"]["rightHand"]
    board[y][x+1] = ""
    #board[y][x+3] = ""

    board[y+1][x] = player["icon"]["legs"]
    board[y+1][x+1] = ""

    # old version with X and Y of player in its right top corner
    """board[y][x-3] = player["icon"]["head"]
    board[y][x-2] = ""

    board[y+1][x-4] = player["icon"]["leftHand"]
    board[y+1][x-3] = player["icon"]["body"]
    board[y+1][x-2] = player["icon"]["rightHand"]
    board[y+1][x-1] = ""
    board[y+1][x] = ""

    board[y+2][x-3] = player["icon"]["legs"]
    board[y+2][x-2] = ""
    """

    return board


def customize_character(player, new_head="", new_body="", new_legs=""):

    player = change_body_part(player, "head")
    player = change_body_part(player, "body")
    player = change_body_part(player, "legs")
    return player


def change_body_part(player, new_body_part_type, id=0):

    clear_screen()
    print()

    if new_body_part_type == "head":
        part_type = BODY_PARTS["heads"]
        print(f"\t{new_body_part_type.upper()}: ◄ {part_type[id]} ►")
        print(f"\tBODY:   {PLAYER_ICON['body']}  ")
        print(f"\tLEGS:   {PLAYER_ICON['legs']}  ")
    elif new_body_part_type == "body":
        part_type = BODY_PARTS["bodies"]
        print(f"\tHEAD:   {PLAYER_ICON['head']}  ")
        print(f"\t{new_body_part_type.upper()}: ◄ {part_type[id]} ►")
        print(f"\tLEGS:   {PLAYER_ICON['legs']}  ")
    elif new_body_part_type == "legs":
        part_type = BODY_PARTS["legs"]
        print(f"\tHEAD:   {PLAYER_ICON['head']}  ")
        print(f"\tBODY:   {PLAYER_ICON['body']}  ")
        print(f"\t{new_body_part_type.upper()}: ◄ {part_type[id]} ►")

    key = key_pressed()
    if key in KEY_BINDINGS["left"] and id > 0:
        change_body_part(player, new_body_part_type, id-1)
    elif key in KEY_BINDINGS["right"] and id < len(part_type)-1:
        change_body_part(player, new_body_part_type, id+1)
    elif key == 10:  # test ENTERa
        input()
        pass
    elif key in KEY_BINDINGS["exit"]:
        PLAYER_ICON[new_body_part_type] = part_type[id]
        return player
    else:
        change_body_part(player, new_body_part_type, id)


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


def generate_random_things_on_map(board, item, max_items_in_row=4, max_items_in_column=2):

    board_width = len(board[0])
    board_height = len(board)

    if isinstance(item, list):

        item_height = len(item)
        item_width = len(max(item))
        for i in range(item_height):
            if len(item[i]) < item_width:
                difference = item_width - len(item[i])
                item[i] = item[i] + (" " * difference)

        itemsY = random.sample(
            range(1, board_height - item_height), max_items_in_column)
        itemsY = sorted(itemsY)
        itemsX = random.sample(
            range(1, board_width - (item_width * max_items_in_row)), max_items_in_row)

        #print(itemsX, itemsY)
        # input()
        for i in range(0, min([len(itemsX), len(itemsY)])):
            for h in range(item_height):
                for w in range(item_width):
                    if item[h][w] != " ":
                        board[itemsY[i]+h][itemsX[i]+w] = item[h][w]

    elif isinstance(item, str):
        item_width = len(item)

        for i in range(1, len(board)-1):
            itemsX = random.sample(
                range(1, board_width - item_width), max_items_in_row)
            for e in range(max_items_in_row):
                board[i][itemsX[e]] = item

    return board


def high_score(player):
    with open('Score.csv', 'a') as file:
        nickname = input("Congratulations!\n You achived top score \n"
                         "What's your name ?")
        file.write("\n" + nickname + "|" +
                   "Highscore = " + str(stats.player_score) +
                   "|" + "Level = " + str(player["lvl"]) +
                   "|" + "Monsters killed = " + str(stats.monsters_kill))


def max_player_weight_reached():    # Everytime player tries to store something
    if stats.max_player_carry == ui.inv_weight:
        print("You reached maximum weight limit")
    if stats.max_player_carry > ui.inv_weight:
        print("You can't carry this item")
        ui.inv.pop[-1]


def small_monster_kill(player):
    stats.monsters_kill += 1
    stats.player_score += 10
    player["experience"] += 20


def boss_monster_kill(player):
    stats.monsters_kill += 1
    stats.player_score += 250
    
