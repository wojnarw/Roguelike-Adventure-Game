def display_board(board):
    '''
    Displays complete game board on the screen
    Returns:
    Nothing
    '''
    lines = []
    for i in range(len(board)):
        lines.append("")
        for e in range(len(board[i])):
            lines[i] += board[i][e]

    lines[1] += " CONTROLS"
    lines[2] += " Movement: WSAD or numerical keyboard"
    lines[3] += " I - inventory"
    lines[4] += " K - character customization"

    #lines[-5] = 

    text = "\n".join(lines)
    print(text)


inv = {"HP Potion", "Mana Potion", "Beginner Sword"}


def display_inv():
    print(inv)
    max_player_carry = 10
    listed_items = 0
    for i in inv:
        listed_items += 1
        if listed_items >= max_player_carry:
            print("you can't carry more items")
