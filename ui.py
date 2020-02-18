def display_board(board):
    '''
    Displays complete game board on the screen
    Returns:
    Nothing
    '''
    text = ""
    for i in range(len(board)):
        for e in range(len(board[i])):
            text += board[i][e]
        text += "\n"
    print(text)


inv = {"HP Potion", "Mana Potion", "Beginner Sword"}


def display_inv():
    print(inv)
    listed_items = 0
    for i in inv:
        listed_items += 1
        if listed_items >= 10:
            print("you can't carry more items")


HP = 5
MP = 10


def display_stats():
    print("HP =", HP, "MP =", MP)
