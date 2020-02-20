import main
from const import *
player_score = 0
monsters_kill = 0
monster_hp = ENEMIES["small"]["HP"]
monster_dmg = ENEMIES["small"]["DMG"]


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
        "HP": 5,
        "MP": 10,
        "lvl": 1,
        "experience": 20,
        "max_experience": 100,    # Exp needed to lvl up
        "intelligence": 1,   # Stat making spells and potions deal/heal more
        "strength": 1,      # Stat increasing attack dmg
        "endurance": 1,     # Stat increasing max carry and max hp
        "charisma": 1,      # Make it possible to get bonuses from events
        "max_hp": 10,
        "max_player_carry": 10,    # Maximum carrying size
        "attack": 1   # Dmg Player deal to enemies
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


def taking_dmg(player):
    player["HP"] -= monster_dmg
    print("HP -" + str(monster_dmg))
    if player["HP"] <= 0:
        print("Przegrana")
        raise SystemExit


'''def drinking_potions(player):
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
                  print("No potions")'''
