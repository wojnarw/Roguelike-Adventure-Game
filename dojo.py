import os

map = []
width = 64
height = 16
playerX, playerY = 3, 3

for i in range(height):
    map.append([])
    for e in range(width):
        map[i].append("")

def main(moveDir = ""):

    global playerX, playerY
    
    if moveDir == 'w':
        playerY -= 1
    elif moveDir == 's':
        playerY += 1
    elif moveDir == 'a':
        playerX -= 1
    elif moveDir == 'd':
        playerX += 1
    elif moveDir == 'x':
        return

    for i in range(height):
        for e in range(width):
            if i == 0 or e == 0 or i == height-1 or e == width-1:
                map[i][e] = "#"
            elif i == playerY and e == playerX:
                map[i][e] = "@"
            else:
                map[i][e] = "."

    display()


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def display():
    os.system('clear')
    text = ""
    for i in range(height):
        for e in range(width):
            text += map[i][e]
        text += "\n"
    print(text)

    moveDir = getch()
    main(moveDir)

main()
