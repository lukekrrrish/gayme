from mains.imports import *
from mains.vars import *

def slime():
    global score
    global money
    player_hp = stats.player.health
    slime_hp = stats.slime.health
    player_dmg = stats.player.dmg
    slime_dmg = stats.slime.dmg
    outcome = False
    while outcome != True:
        if slime_hp > 0:
            player_hp -= slime_dmg
            print(f"The player has {player_hp} Left")
            sleep(stats.player.cd)
        else:
            score += 50
            money += 500
            print("U have gained 500 coins")
            outcome = True
        if player_hp > 0:
            slime_hp -= player_dmg
            print(f"The slime has {slime_hp} Left")
            sleep(stats.slime.cd)
        else:
            money -= 250
            print("U have lost 250 coins")
            outcome = True
        if outcome == True:
            score += 50
            print("U have grown to level 1")
            choice = input(f"Your new amount of moni is {str(money)}\n Would you like to play again?\n1 = Yes\nOther = home\n")
            if choice == "1":
                slime()
            else:
                break
            