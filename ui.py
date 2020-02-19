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
