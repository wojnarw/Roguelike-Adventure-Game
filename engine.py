import random
import main
import stats
import copy
import ui
from const import *
from helpers import key_pressed, clear_screen


def create_board(width, height, filename = ""):
    '''
    Creates game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    board = []
    if not filename:
        for i in range(height):
            board.append([])
            for e in range(width):
                board[i].append("")
        return board

    try:
        with open(filename,"r") as file:
            for line in file:
                pass

    except FileNotFoundError:
        print(f"File '{path_and_filename}' not found!")


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
    #player["height"]
    #player["width"]

    board = copy.deepcopy(original_board)

    # EMOJIS TAKE 2 SPACES EACH WHEN DISPLAYED
    board[y][x-3] = player["icon"]["head"]
    board[y][x-2] = ""

    board[y+1][x-4] = player["icon"]["leftHand"]
    board[y+1][x-3] = player["icon"]["body"]
    board[y+1][x-2] = player["icon"]["rightHand"]
    board[y+1][x-1] = ""
    board[y+1][x] = ""

    board[y+2][x-3] = player["icon"]["legs"]
    board[y+2][x-2] = ""

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
    elif key == 10: # test ENTERa
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


def generate_random_things_on_map(board, item, max_items_in_row = 4, max_items_in_column = 2):


    board_width = len(board[0])
    board_height = len(board)

    if isinstance(item, list):
        item_height = len(item)
        item_width = len(max(item))
        for i in range(item_height):
            if len(item[i]) < item_width:
                difference = item_width - len(item[i])
                item[i] = item[i] + (" " * difference)

        itemsY = random.sample(range(1,board_height - item_height), max_items_in_column)
        itemsY = sorted(itemsY)
        itemsX = random.sample(range(1,board_width - (item_width * max_items_in_row)), max_items_in_row)

        #print(itemsX, itemsY)
        #input()
        for i in range(0, min([len(itemsX), len(itemsY)])):
            for h in range(item_height):
                for w in range(item_width):
                    if item[h][w] != " ":
                        board[itemsY[i]+h][itemsX[i]+w] =  item[h][w]
                
    elif isinstance(item, str):
        item_width = len(item)
    
        for i in range(1, len(board)-1):
            itemsX = random.sample(range(1,board_width - item_width), max_items_in_row)
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


def monster_kill(player):
    stats.monsters_kill += 1
    stats.player_score += 10
    player["experience"] += 20


def fight_with_monsters(player):
    print("Player Hp :  " + str(player["HP"]) + "/" + str(player["max_hp"]))
    print("Choose option: " "\n" "1.Attack" "\n" "2. Inventory" "\n"
          "3.Try to escape")
    key = key_pressed()
    clear_screen()
    if key in KEY_BINDINGS_FIGHT["Fight"]:
        print("1. Attack with weapon =", player["attack"], "dmg", "\n"
              "2. Cast Fire ball =", 1 + player["intelligence"], "dmg", "\n"
              "3. Back"
              )
        key = key_pressed()
        clear_screen()
        if key == "1":
            chance_to_hit = ["hit", "hit", "hit", "miss"]
            if random.choice(chance_to_hit) == "hit":
                print("Succeeded!")
                stats.monster_hp -= player["attack"]      # Add monster hp
                if stats.monster_hp <= 0:
                    print("You killed monster")
                    monster_kill(player)
                    pass
                else:
                    stats.taking_dmg(player)
                    fight_with_monsters
                input("Press enter")
                clear_screen()
            else:
                print("Missed")
                stats.taking_dmg(player)
                input("Press enter")
        elif key == "2":
            chance_to_hit = ["hit", "hit", "hit", "miss"]
            if random.choice(chance_to_hit) == "hit":
                print("Succeeded!")
                stats.monster_hp -= 1 + player["intelligence"]
                if stats.monster_hp <= 0:
                    print("You killed monster")
                    monster_kill(player)
                else:
                    stats.taking_dmg(player)
                    fight_with_monsters
                input("Press enter")
            else:
                print("Missed")
                stats.taking_dmg(player)
                input("Press enter")
        elif key == "3":
            fight_with_monsters(player)
    elif key in KEY_BINDINGS_FIGHT["Use inventory"]:
        ui.display_inv()
        print("1.Heal", "2.Regen", "3.Back")
        key = key_pressed()
        if key == "1":
            if "HP Potion" in ui.inv:
                player["HP"] += 1 + player["intelligence"]
                # If current HP >= maxHP currentHP=MaxHP
                if player["HP"] >= player["max_hp"]:
                    player["HP"] = player["max_hp"]
                ui.inv.remove("HP Potion")
            else:
                print("No potions")
                pass
        if key == "2":
            if "Mana Potion" in ui.inv:
                player["MP"] += 10 + player["intelligence"]
                ui.inv.remove("Mana Potion")
            else:
                  print("No potions")
        fight_with_monsters(player)
        if key == "3":
            fight_with_monsters(player)
    elif key in KEY_BINDINGS_FIGHT["Try to escape"]:
        chance_to_escape = ["fail", "fail", "fail", "fail", "fail", "fail",
                            "successed"]
        if random.choice(chance_to_escape) == "successed":
            print("You escaped")
            input("Press enter")
        elif random.choice(chance_to_escape) == "fail":
            print("Failed")
            stats.taking_dmg(player)
            fight_with_monsters(player)
    if key not in KEY_BINDINGS_FIGHT:
        fight_with_monsters(player)
