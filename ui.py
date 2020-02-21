import time
import shutil
import math
import random
import const
import asciiart
from helpers import clear_screen, key_pressed
from termcolor import colored

color_variants = [{
        '█': "blue",
        '░': "red",
        '▒': "green",
        '▓': "green",
        'ˇ': "green",
        'Ψ': "green"
        },
        {
        '█': "cyan",
        '░': "red",
        '▒': "green",
        '▓': "green",
        'ˇ': "yellow",
        'Ψ': "yellow",},
        ]

color_key = {
        '˯': "green",
        'ˬ': "green",
        '‡': "yellow",
        '║': "yellow",
        '▀': "magenta",
        '▄': "blue",
        "●": "yellow",
        "▌": "magenta",
        "▐": "magenta",
        const.ENEMIES["big"]["icon"]: "red",
        const.ENEMIES["small"]["icon"]: "red"
        }

color_key.update(color_variants[0])
#color_key.update(color_variants[1])

def display_board(board, player):
    '''
    Displays complete game board on the screen
    Returns:
    Nothing
    '''
    height = len(board)
    width = len(board[0])

    lines = []
    for i in range(height):
        lines.append("")
        for e in range(width):
            lines[i] += board[i][e]

    lines[1] += " CONTROLS"
    lines[2] += " Movement: WSAD or numerical keyboard"
    lines[3] += " I - inventory"
    lines[4] += " K - character customization"
    lines[5] += " L - display logo"
    lines[6] += " P - show story"
    lines[7] += " O - show test overlay"
    lines[8] += " V - verbal attack"
    lines[9] += " G - generate new level"
    

    # display HP points properly, if there are more than 10 (max in a row)
    if int(player["max_hp"]) > 10:
        extra_lines = player["max_hp"] // 10
        HPs = player["HP"]
        MAXHPs = player["max_hp"]
        lines[-11 - extra_lines -1] += " HP:   "

        for s in range(extra_lines+1,0,-1):

            if MAXHPs > 10:
                if HPs >= 10:
                    lines[-11 - s] += "       " + "❤️ " * 10
                    HPs -= 10
                elif HPs > 0:
                    lines[-11 - s] += "       " + "❤️ " * HPs
                    lines[-11 - s] += "🖤" * (10 - HPs)
                elif MAXHPs >= 10:
                    lines[-11 - s] += "       " + "🖤" * 10
            elif MAXHPs > 0:
                lines[-11 - s] += "       " + "❤️ " * HPs
                lines[-11 - s] += "🖤" * (10 - HPs)

            MAXHPs -= 10
        #lines[-11] += "       " + "❤️ " * (player["HP"] - extra_lines*10)
        
    else:
        lines[-11] += " HP:   " + "❤️ " * player["HP"]
        lines[-11] += "🖤" * (player["max_hp"] - player["HP"])

    lines[-10] += " MANA: " + "💧" * player["MP"]
    #lines[-9] += str(player["HP"]) + " " + str(player["max_hp"])
    lines[-8] += " 🥇 LVL: \t\t" + str(player["lvl"])
    lines[-7] += " 🎰 EXPERIENCE: \t" + str(player["experience"]) + "/" + str(player["max_experience"])
    lines[-5] += " 💪 STRENGTH: \t" + str(player["strength"])
    lines[-4] += " 🧠 INTELLIGENCE: \t" + str(player["intelligence"])
    lines[-3] += " 🤲 ENDURANCE: \t" + str(player["endurance"])
    lines[-2] += " 👄 CHARISMA: \t" + str(player["charisma"])

    #text = "\n".join(lines)
    #print(text)

    for line in lines:
        print (''.join(colored(element, color_key.get(element, 'white'))
           for element in line))

    experience_label = " XP: "
    experience_bar_max = width - len(experience_label)
    experience_bar_points = math.floor(player["experience"] / player["max_experience"] * experience_bar_max)
    experience_bar = experience_label + colored("▀" * experience_bar_points, "yellow") + colored("▀" * (experience_bar_max - experience_bar_points), "grey")
    print(experience_bar)


inv = {"HP Potion", "Mana Potion", "Beginner Sword"}
inv_weight = 0

def display_inv():
    print(inv)


def weight(inv_weight):     # Items checking weight
    for i in inv:
        inv_weight += 1


def show_hall_of_fame():
    with open('Score.csv') as file:
        print(file)
        input("Press enter")
        

def show_overlay(board, table=["sword","ring","lala"], show_indexes = True):

    BOARD_WIDTH = len(board[0])
    BOARD_HEIGHT = len(board)
    max_width = 40
    max_height = 30

    overlay_height = min(BOARD_HEIGHT*1//2,max_height)
    overlay_width = min(BOARD_WIDTH*1//2,max_width)

    overlay_y = (BOARD_HEIGHT - overlay_height) // 2
    overlay_x = (BOARD_WIDTH - overlay_width) // 2

    for y in range(overlay_y, overlay_y + overlay_height):
        for x in range(overlay_x, overlay_x + overlay_width):
            if y == overlay_y or x == overlay_x or y - overlay_height == overlay_y -1 or x - overlay_width == overlay_x-1:
                board[y][x] = "▒"
            else:
                board[y][x] = " "
    margin = 2

    for i in range(len(table)):
        if show_indexes:
            board[overlay_y + i + margin][overlay_x + 0 + margin] = str(i+1)
            board[overlay_y + i + margin][overlay_x + 1 + margin] = "."
            board[overlay_y + i + margin][overlay_x + 2 + margin] = " "
        
        for e in range (margin, len(table[i]) + margin):
            board[overlay_y + i + margin][overlay_x + e + margin] = table[i][e-margin]

    return board


def show_story():

    time.sleep(1)

    text_movement_delay = 3
    animation_delay = 0.3

    story = []
    story.append("The night was cold, I wrapped myself in thick blanket and tried to sleep. ") 
    story.append("Then I heard a thunder. The Baba Yaga has came. ")
    story.append("She took my lynx, she killed my parents. ")
    story.append("I hid under bed and saw as she rode away on my lynx.")
    story.append("I will get you back Rysio. I will get revenge.")
    text = []

    for i in range(len(story)):
        clear_screen()
        empty_space = (20-i) * "\n"
        text.append(story[i])
        print(empty_space)
        for e in range(len(text)):
            print(text[e].center(shutil.get_terminal_size().columns))

        time.sleep(text_movement_delay)

    for i in range(1,15):
        print(empty_space)
        for e in range(len(text)):
            print(text[e].center(shutil.get_terminal_size().columns))
        print(asciiart.FACE2[i % 2])
        time.sleep(animation_delay)
        
    print("Press any key".center(shutil.get_terminal_size().columns))
    key_pressed()


def verbal_attack(board_with_player, board, player, used):

    texts = ["Nie sąd cię skaże wiedźmi sługo",
             "Widziałem cię w Żabce na kasie",
             "Pchasz się w gips, kolego",
             "Masz niedobór żelaza pod żebrami?",
             "HA TFU!",
             "Czarci pomiot!",
             "Chrrrr HA TFU!"
             ]
    # make random not repeat last choice
    choose = random.randint(0, len(texts)-1)

    while choose == used:
        choose = random.randint(0, len(texts)-1)
        print(choose)

    player_say(board_with_player, player, texts[choose])

    if board[player["y"]+2][player["x"]] in const.ENEMIES["icons"]:
        board[player["y"]+3][player["x"]] = board[player["y"]+2][player["x"]]
        board[player["y"]+2][player["x"]] = " "

    return choose, board


def player_say(board_with_player, player, sentence):

    # bubble speech relative position
    speech_Y = player["y"] - 2
    if len(sentence) + player["x"] < len(board_with_player[0]):
        speech_X = player["x"] + 3
    else:
        speech_X = player["x"] - len(sentence)

    for i in range(len(sentence)):
        board_with_player[speech_Y][speech_X + i] = sentence[i]

    clear_screen()
    display_board(board_with_player, player)

def show_logo_animation(logo, forward = "True"):

    # time delay in seconds
    animation_delay = 0.2
    full_logo_delay = 1.5

    time.sleep(full_logo_delay)

    if forward:
        for i in range(3,-1,-1):
            clear_screen()
            print("\n\n")
            print(colored(logo[i], 'yellow', attrs=[]))
            time.sleep(animation_delay)

        time.sleep(full_logo_delay)
    else:
        for i in range(4):
            clear_screen()
            print("\n\n")
            print(colored(logo[i], 'yellow', attrs=[]))
            time.sleep(animation_delay)
    
    #clear_screen()
    time.sleep(animation_delay)

"""def show_logo_animation(logo):

    # time delay in seconds
    animation_delay = 0.2
    full_logo_delay = 1.5

    clear_screen()
    time.sleep(full_logo_delay)

    characters = ["░", "▓", "█", "█"]
    fade_in(logo, "yellow", animation_delay, characters)
    characters.reverse()
    fade_out(logo, "yellow", animation_delay, characters)

    time.sleep(full_logo_delay)

    clear_screen()
    time.sleep(animation_delay)

def fade_out(string_to_fade, color, animation_delay, characters):
    clear_screen()
    print(colored(string_to_fade, color, attrs=[]))
    time.sleep(animation_delay)
    for i in range(3):
        clear_screen()
        string_to_fade = string_to_fade.replace(characters[i], characters[i+1])
        print(colored(string_to_fade, color, attrs=[]))
        time.sleep(animation_delay)
    

def fade_in(string_to_fade, color, animation_delay, characters):
    clear_screen()
    print(colored(string_to_fade, color, attrs=[]))
    time.sleep(animation_delay)
    for i in range(3):
        clear_screen()
        string_to_fade = string_to_fade.replace(characters[i], characters[i+1])
        print(colored(string_to_fade, color, attrs=[]))
        time.sleep(animation_delay)
"""
