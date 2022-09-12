from mains.imports import *






with open("files/money.txt", "r+") as f:
    m = int(f.read(1))


O_F = True

class economy():
    money = 1000

class stats():
    class player():
        health = 10
        dmg = 6
        level = 0
        defense = 2
        cd = 3
    
    class slime():
        health = 5
        dmg = 0.5
        level = 0
        defense = 0
        cd = 2

class all():
    player_stats = stats.player.health + stats.player.dmg + stats.player.level + stats.player.defense
    slime_stats = stats.slime.health + stats.slime.dmg + stats.slime.level + stats.slime.defense



class multiplier():
    class pstats():
        p0 = False
        p1 = False
        p2 = False
        p3 = False
        p4 = False
        p5 = False
        p6 = False
        pstats = all.player_stats
        p0 = 1 * pstats
        p1 = 1.5 * pstats + p0
        p2 = 2 * pstats + p1
        p3 = 3.5 * pstats + p2
        p4 = 5 * pstats + p3
        p5 = 6.5 * pstats + p4
        p6 = 8 * pstats + p5

        default = p0
        p1_s = p1
        p2_s = p2
        p3_s = p3
        p4_s = p4
        p5_s = p5
        p6_s = p6

        if default == True:
            p0
            print(p0)
        if p1_s == True:
            p1
            print(p1)
        if p2_s == True:
            p2
            print(p2)
        if p3_s == True:
            p3
            print(p3)
        if p4_s == True:
            p4
            print(p4)
        if p5_s == True:
            p5
            print(p5)
        if p6_s == True:
            p6
            print(p6)



score = 0
money = economy.money
level_player = stats.player.level



