import stats
import main
import engine
import random
from helpers import key_pressed, clear_screen
from const import *


def fight_with_monsters_small(player):
    while stats.small_monster_hp > 0:
        print("Player Hp :  " +
              str(player["HP"]) + "/" + str(player["max_hp"]))
        print("Choose option: " "\n" "1.Attack" "\n" "2. Inventory" "\n"
              "3.Try to escape")
        key = key_pressed()
        clear_screen()
        if key in KEY_BINDINGS_FIGHT["Fight"]:
            print("1. Attack with weapon =", player["attack"], "dmg", "\n"
                  "2. Cast Fire ball =", 1 +
                  player["intelligence"], "dmg", "\n"
                  "3. Back"
                  )
            key = key_pressed()
            clear_screen()
            if key == "1":
                chance_to_hit = ["hit", "hit", "hit", "miss"]
                if random.choice(chance_to_hit) == "hit":
                    print("Succeeded!")
                    # Add monster hp
                    stats.small_monster_hp -= player["attack"]
                    if stats.small_monster_hp <= 0:
                        print("You killed monster")
                        small_monster_kill(player)
                        continue
                    else:
                        stats.small_taking_dmg(player)
                        fight_with_monsters_small(player)
                    input("Press enter")
                    clear_screen()
                else:
                    print("Missed")
                    stats.small_taking_dmg(player)
                    input("Press enter")
            elif key == "2":
                chance_to_hit = ["hit", "hit", "hit", "miss"]
                if random.choice(chance_to_hit) == "hit":
                    print("Succeeded!")
                    stats.small_monster_hp -= 1 + player["intelligence"]
                    if stats.small_monster_hp <= 0:
                        print("You killed monster")
                        small_monster_kill(player)
                        pass
                    else:
                        stats.small_taking_dmg(player)
                        fight_with_monsters_small(player)
                    input("Press enter")
                else:
                    print("Missed")
                    stats.small_taking_dmg(player)
                    input("Press enter")
            elif key == "3":
                fight_with_monsters_small(player)
        elif key in KEY_BINDINGS_FIGHT["Use inventory"]:
            ui.display_inv()
            print("1.Heal", "2.Regen", "3.Back")
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
                    pass                                           # Sprawdź
            if key == "2":
                if "Mana Potion" in ui.inv:
                    player["MP"] += 10 + player["intelligence"]
                    ui.inv.remove("Mana Potion")
                else:
                    print("No potions")
            fight_with_monsters_small(player)
            if key == "3":
                fight_with_monsters_small(player)
        elif key in KEY_BINDINGS_FIGHT["Try to escape"]:
            chance_to_escape = ["fail", "fail", "fail", "fail", "fail", "fail",
                                "successed"]
            if random.choice(chance_to_escape) == "successed":
                print("You escaped")
                input("Press enter")
            elif random.choice(chance_to_escape) == "fail":
                print("Failed")
                stats.small_taking_dmg(player)
                fight_with_monsters_small(player)
        if key not in KEY_BINDINGS_FIGHT:
            fight_with_monsters_small(player)


def fight_with_monsters_large(player):
    while stats.large_monster_hp > 0:
        print("Player Hp :  " +
              str(player["HP"]) + "/" + str(player["max_hp"]))
        print("Choose option: " "\n" "1.Attack" "\n" "2. Inventory" "\n"
              "3.Try to escape")
        key = key_pressed()
        clear_screen()
        if key in KEY_BINDINGS_FIGHT["Fight"]:
            print("1. Attack with weapon =", player["attack"], "dmg", "\n"
                  "2. Cast Fire ball =", 1 +
                  player["intelligence"], "dmg", "\n"
                  "3. Back"
                  )
            key = key_pressed()
            clear_screen()
            if key == "1":
                chance_to_hit = ["hit", "hit", "hit", "miss"]
                if random.choice(chance_to_hit) == "hit":
                    print("Succeeded!")
                    # Add monster hp
                    stats.large_monster_hp -= player["attack"]
                    if stats.large_monster_hp <= 0:
                        print("You killed monster")
                        large_monster_kill(player)
                        continue
                    else:
                        stats.large_taking_dmg(player)
                        fight_with_monsters_large(player)
                    input("Press enter")
                    clear_screen()
                else:
                    print("Missed")
                    stats.large_taking_dmg(player)
                    input("Press enter")
            elif key == "2":
                chance_to_hit = ["hit", "hit", "hit", "miss"]
                if random.choice(chance_to_hit) == "hit":
                    print("Succeeded!")
                    stats.large_monster_hp -= 1 + player["intelligence"]
                    if stats.large_monster_hp <= 0:
                        print("You killed monster")
                        large_monster_kill(player)
                        pass
                    else:
                        stats.large_taking_dmg(player)
                        fight_with_monsters_large(player)
                    input("Press enter")
                else:
                    print("Missed")
                    stats.large_taking_dmg(player)
                    input("Press enter")
            elif key == "3":
                fight_with_monsters_large(player)
        elif key in KEY_BINDINGS_FIGHT["Use inventory"]:
            ui.display_inv()
            print("1.Heal", "2.Regen", "3.Back")
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
                    print("No potions")
            fight_with_monsters_large(player)
            if key == "3":
                fight_with_monsters_large(player)
        elif key in KEY_BINDINGS_FIGHT["Try to escape"]:
            chance_to_escape = ["fail", "fail", "fail", "fail", "fail", "fail",
                                "successed"]
            if random.choice(chance_to_escape) == "successed":
                print("You escaped")
                input("Press enter")
            elif random.choice(chance_to_escape) == "fail":
                print("Failed")
                stats.large_taking_dmg(player)
                fight_with_monsters_large(player)
        if key not in KEY_BINDINGS_FIGHT:
            fight_with_monsters_large(player)


def fight_with_monsters_boss(player):
    while stats.boss_monster_hp > 0:
        print("Player Hp :  " +
              str(player["HP"]) + "/" + str(player["max_hp"]))
        print("Choose option: " "\n" "1.Attack" "\n" "2. Inventory" "\n"
              "3.Try to escape")
        key = key_pressed()
        clear_screen()
        if key in KEY_BINDINGS_FIGHT["Fight"]:
            print("1. Attack with weapon =", player["attack"], "dmg", "\n"
                  "2. Cast Fire ball =", 1 +
                  player["intelligence"], "dmg", "\n"
                  "3. Back"
                  )
            key = key_pressed()
            clear_screen()
            if key == "1":
                chance_to_hit = ["hit", "hit", "hit", "miss"]
                if random.choice(chance_to_hit) == "hit":
                    print("Succeeded!")
                    # Add monster hp
                    stats.boss_monster_hp -= player["attack"]
                    if stats.boss_monster_hp <= 0:
                        print("You killed monster")
                        engine.boss_monster_kill(player)
                        continue
                    else:
                        stats.boss_taking_dmg(player)
                        fight_with_monsters_boss(player)
                    input("Press enter")
                    clear_screen()
                else:
                    print("Missed")
                    stats.boss_taking_dmg(player)
                    input("Press enter")
            elif key == "2":
                chance_to_hit = ["hit", "hit", "hit", "miss"]
                if random.choice(chance_to_hit) == "hit":
                    print("Succeeded!")
                    stats.boss_monster_hp -= 1 + player["intelligence"]
                    if stats.boss_monster_hp <= 0:
                        print("You killed monster")
                        engine.boss_monster_kill(player)
                        pass
                    else:
                        stats.boss_taking_dmg(player)
                        fight_with_monsters_boss(player)
                    input("Press enter")
                else:
                    print("Missed")
                    stats.boss_taking_dmg(player)
                    input("Press enter")
            elif key == "3":
                fight_with_monsters_boss(player)
        elif key in KEY_BINDINGS_FIGHT["Use inventory"]:
            ui.display_inv()
            print("1.Heal", "2.Regen", "3.Back")
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
                    print("No potions")
            fight_with_monsters_boss(player)
            if key == "3":
                fight_with_monsters_boss(player)
        elif key in KEY_BINDINGS_FIGHT["Try to escape"]:
            chance_to_escape = ["fail", "fail", "fail", "fail", "fail", "fail",
                                "successed"]
            if random.choice(chance_to_escape) == "successed":
                print("You escaped")
                input("Press enter")
                return
            elif random.choice(chance_to_escape) == "fail":
                print("Failed")
                stats.boss_taking_dmg(player)
                fight_with_monsters_boss(player)
        if key not in KEY_BINDINGS_FIGHT:
            fight_with_monsters_boss(player)
