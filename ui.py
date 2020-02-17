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

