import main
player_score = 0
monsters_kill = 0


def display_basic_stats(player):
    print("HP =", player["HP"], "/", player["max_hp"], "| MP =", player["MP"],
          "|", "Experience =", player["experience"], "/", player["max_experience"], "|",
          "Level =", player["lvl"])


def display_advenced_stats(player):
    print("Inteligence =", player["Inteligence"], "Strength =", player["strength"],
          "Endurance =", player["endurance"], "Charisma =", player["charisma"],
          "Max inventory size =", player["max_player_carry"],
          "Attack Damage =", player["attack"],)
    input("Press enter")
