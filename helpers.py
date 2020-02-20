import os

def key_pressed():
    
    import sys

    try:
        import tty, termios
    except ImportError:
    # Probably Windows.
        try:
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            # Just give up here.
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen(n =500):
    
    #if os.name == "nt":
    #    os.system('cls')
    #else:
    #    os.system('clear')
    
    os.system('clear')
    #if n == 0:
    #    os.system('clear')
    #else:
    #    print('\b'*n)