import asciiart
import os
import time
import ui
import helpers
import engine
import main
import const
import shutil
from termcolor import colored
from art import *

def print_menu():

    helpers.clear_screen()
    empty_space = 7 * "\n"
    print(empty_space)
    print(colored(const.LOGO[1], 'yellow', attrs=[]))
    print(empty_space)

    user_input = input("PRESS ENTER TO START".center(shutil.get_terminal_size().columns))

    if user_input == "":
        show_animation(asciiart.swing, asciiart.orphan)
    # elif user_input == "2":
    #     # engine.customize_character(player)
    # elif user_input == "0":
    #     # sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def show_intro(list_with_picture):
    os.system('clear')
    t = 0.5
    empty_space = 5 * "\n"
    
    for picture in list_with_picture:
        print(empty_space)
        for pictureLine in picture.splitlines():
            print(pictureLine.center(shutil.get_terminal_size().columns))
        time.sleep(t)
        os.system('clear')
        

def show_animation(swing, orphan):
    t = 3
    empty_space = 10 * "\n"

    for i in range(3):
        show_intro(swing)
    os.system('clear')
    ui.show_story()
    os.system('clear')

    for picture in orphan:
        os.system('clear')
        print(empty_space)
        for pictureLine in picture.splitlines():
            print(pictureLine.center(shutil.get_terminal_size().columns))
        time.sleep(t)

    main.init()
   

def win():

    t =2
    empty_space = 5 * "\n"

    os.system("clear")
    for picture in lynx:
        print(empty_space)
        for pictureLine in picture.splitlines():
            print(pictureLine.center(shutil.get_terminal_size().columns))
        time.sleep(2)
        os.system('clear')
    print(empty_space)
    for pictureLine in asciiart.heart_lynx.splitlines():
        print(pictureLine.center(shutil.get_terminal_size().columns))
    play_again()

def play_again():
    play_again = input("Do you want to play again(yes/no)? ")

    if play_again == "yes":
        print_menu()
    else:
        raise SystemExit



# def show_intro(picture):
#     board = engine.create_board(80,30)
#     BOARD_HEIGHT = len(board)
#     BOARD_WIDTH = len(board[0])

#     WALL = '█'
#     for i in range(BOARD_HEIGHT):
#         for e in range(BOARD_WIDTH):
#             if i == 0 or e == 0 or i == BOARD_HEIGHT-1 or e == BOARD_WIDTH-1:
#                 board[i][e] = WALL

#     helpers.clear_screen()

#     #picture = asciiart.picture
#     lineList = picture.splitlines()

#     artWidth = len(lineList[1])
#     artHeight = len(lineList)
#     widthShift = int((BOARD_WIDTH - artWidth)/2)
#     heighthShift = int((BOARD_HEIGHT - artHeight)/2)
#     for i in range(len(lineList)):
#         lineLen = len(lineList[i])
#         for j in range(lineLen):
#             board[i+heighthShift][j+widthShift] = lineList[i][j]


    


print_menu()
# print_menu()
