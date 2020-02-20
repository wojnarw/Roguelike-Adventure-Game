#import main
player_score = 0
monsters_kill = 0

# OBSELETE FUNCTION
def display_basic_stats(player):
    print("\tHP =", player["HP"], "/", player["max_hp"], "| MP =", player["MP"],
          "|", "Experience =", player["experience"], "/", player["max_experience"], "|",
          "Level =", player["lvl"])


def display_advenced_stats(player):
    print("Inteligence =", player["intelligence"], "Strength =", player["strength"],
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
        player["max_experience"] += 5
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