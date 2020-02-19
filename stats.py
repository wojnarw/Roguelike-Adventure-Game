HP = 5              # Health Player starts with
MP = 10             # Mana Player starts with
lvl = 1
experience = 0
max_experience = 5
Inteligence = 1     # Stat making spells and potions deal/heal more
strength = 1        # Stat increasing attack dmg
endurance = 1       # Stat increasing max carry and max hp
charisma = 1        # Make it possible to get bonuses from events
max_hp = 10 + endurance
max_player_carry = 10 + endurance    # Maximum carrying size
attack = 1 + strength   # Dmg Player deal to enemies


def display_basic_stats():
    print("HP =", HP, "/", max_hp, "| MP =", MP, "|",
          "Experience =", experience, "/", max_experience, "|",
          "Level =", lvl)


def display_advenced_stats():
    print("Inteligence =", Inteligence, "Strength =", strength,
          "Endurance =", endurance, "Charisma =", charisma,
          "Max inventory size =", max_player_carry,
          "Attack Damage =", attack,)
    input("Press enter")
