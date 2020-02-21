import main
import asciiart
from const import *
from helpers import clear_screen
player_score = 0
monsters_kill = 0
small_monster_hp = ENEMIES["small"]["HP"]
small_monster_dmg = ENEMIES["small"]["DMG"]
large_monster_hp = ENEMIES["big"]["HP"]
large_monster_dmg = ENEMIES["big"]["DMG"]
boss_monster_hp = ENEMIES["boss"]["HP"]
boss_monster_dmg = ENEMIES["boss"]["DMG"]


def create_player(PLAYER_START_X, PLAYER_START_Y, PLAYER_ICON):
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        "x": PLAYER_START_X,
        "y": PLAYER_START_Y,
        "icon": PLAYER_ICON,
        "height": 3,
        "width": 5,  # body + 2 arms, emojis are wider than single character
        "HP": 9,
        "MP": 10,
        "lvl": 1,
        "experience": 0,
        "max_experience": 100,    # Exp needed to lvl up
        "intelligence": 1,   # Stat making spells and potions deal/heal more
        "strength": 1,      # Stat increasing attack dmg
        "endurance": 1,     # Stat increasing max carry and max hp
        "charisma": 1,      # Make it possible to get bonuses from events
        "max_hp": 10,
        "max_player_carry": 10,    # Maximum carrying size
        "attack": 5   # Dmg Player deal to enemies
    }
    return player


# OBSELETE FUNCTION


def display_basic_stats(player):
    print("\tHP =", player["HP"], "/", player["max_hp"], "| MP =", player["MP"],
          "|", "Experience =", player["experience"], "/", player["max_experience"], "|",
          "Level =", player["lvl"])


def display_advenced_stats(player):
    print("intelligence =", player["intelligence"], "Strength =", player["strength"],
          "Endurance =", player["endurance"], "Charisma =", player["charisma"],
          "Max inventory size =", player["max_player_carry"],
          "Attack Damage =", player["attack"],)
    input("Press enter")


def level_up(player):
    global player_score
    if player["experience"] >= player["max_experience"]:
        # If more then needed experience to lvl up experience converted to
        # another lvl progress:
        experience_remainder = player["experience"] - player["max_experience"]
        player["max_experience"] += 25
        player["experience"] = 0 + experience_remainder
        player["lvl"] += 1
        player["intelligence"] += 2
        player["strength"] += 2
        player["endurance"] += 2
        player["charisma"] += 2
        player["max_hp"] += player["endurance"]
        player["max_player_carry"] += player["endurance"]
        player["attack"] = player["strength"]
        player_score += 200


def small_taking_dmg(player):  # Dmg small monster deal to Player
    player["HP"] -= small_monster_dmg
    print("Player took dmg -" + str(small_monster_dmg) + "HP")
    if player["HP"] <= 0:
        clear_screen()
        game_over()
        input()
        raise SystemExit


def large_taking_dmg(player):  # Dmg large monster deal to Player
    player["HP"] -= large_monster_dmg
    print("Player took dmg -" + str(large_monster_dmg) + "HP")
    if player["HP"] <= 0:
        clear_screen()
        game_over()
        input()
        raise SystemExit


def boss_taking_dmg(player):  # Dmg Boss deal to Player
    player["HP"] -= boss_monster_dmg
    print("Player took dmg -" + str(boss_monster_dmg) + "HP")
    if player["HP"] <= 0:
        game_over()
        raise SystemExit


def game_over():
    # print(colored(asciiart.game_over, 'red', attrs=[]))
    empty_space = 5 * "\n"

    os.system('clear')
    print(empty_space)
    for pictureLine in asciiart.game_over.splitlines():
        print(colored(pictureLine.center(shutil.get_terminal_size().columns),'red', attrs=[]))
    play_again()