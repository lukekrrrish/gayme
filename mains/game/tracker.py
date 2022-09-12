from mains import *








def money():
    global O_F
    if money > 0:
        print(f"You cant but that item")
        O_F = False


def level():
    global score
    global level_player
    if score == 100:
        level_player += 1
        score += 100 
    while level_player == 1:
        print("Congrats u have reached level 1")
        choice = int(input(f"\n\nChoose which item u want\n\n1 = ?\n2 = ?\n3 = ?\n"))
        if choice == 1:
            print("Congrats u have gotten a wooden sword\n___________________________\n____Stats____\n2 + dmg")
            stats.player.dmg += 0.5
        if choice == 2:
            print("GG'S u have gotten a wodden sheild\n___________________________\n____Stats____\n2 + defense")
            stats.player.defense += 0.5
        if choice == 3:
            print("GG'S u have gotten a wodden wand\n___________________________\n____Stats____\n2 + magic")