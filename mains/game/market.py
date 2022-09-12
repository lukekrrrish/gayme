from mains import *
from .items import *










class price():
    class ingot():
        bronze = 25
        iron = 100
        diamond = 300
        mithril = 500
        gold = 1500
        adamantite = 3000
        runite = 9000
        stygian = 12000
        obsidian = 20000
    class sword():
        bronze = 800
        iron = 600
        diamond = 40000
        mithril = 78000
        adamantite = 670_000
        runite = 2_600_000
        stygian = 3_300_000
        obsidian = 6_500_000
    class chestplate():
        bronze = 2000
        iron = 1200
        diamond = 4000
        mithril = 91000
        adamanite = 770_000
        runite = 2_900_000
        stygian = 4_800_000
        obsidian = 6_500_000
    class dagger():
        bronze = 400
        iron = 4000
        diamond = 10000
        mithril = 39000
        adamantite = 384_000
        runite = 1_600_000
        stygian = 2_900_000
        obsidian = 5_100_000
    class magic():
        pass
    class projectial():
        pass
    class pants():
        bronze = 800
        iron = 6000
        diamond = 3000
        mithril = 52000
        adamanite = 480_000
        runite = 2_000_000
        stygian = 3_400_000
        obsidian = 6_800_000
    class helmate():
        bronze = 800
        iron = 4800
        diamond = 20000
        mithiral = 52000
        adamantite = 480_000
        runite = 1_900_000
        stygian = 3_400_000
        obsidian = 6_000_000
    class ring():
        pass
    class wands():
        pass
    class gloves():
        bronze = 100
        iron = 3000
        diamond = 100_000
        mithril = 250_000
        adamantite = 1_500_000
        runite = 7_500_000
        stygian = 30_000_000
        obsidian = 60_000_000
    class boots():
        bronze = 100
        iron = 8000
        diamond = 30000
        mithril = 60000
        adamantite = 480_000
        runite_boot = 1_800_000
        stygian_boot = 2_900_000
        obsidian_boot = 5_700_000
    class sheild():
        bronze = 1200
        iron = 8000
        diamond = 30000
        mithril = 65000
        adamantite = 580_000
        runite = 2_300_000
        stygian = 4_000_000
        obsidian = 8_000_000
    class all():
        pass


def buy(item):
    if money - item > -1:
        print(f"U now have {money} after the purchase")
    else:
        print(f"U need {item - money} more to buy that item")




def sell(item):
    global money
    if item != player.inv:
        print(f"U need to have that item in the inventory")
    else:
        money += item.price
        print(f"Your new mony amount is {money}")



sell(diamon_dagger)



# def shop():
#     choice = int(input("\n1 = Weapons\n2 = magic\n3 = Armour\n4 = all\n"))
#     if choice == 1:
#         w_choice = int(input("\n1 = Projectial\n2 = Male\n"))
#         if w_choice == 1:
#             for i in range(len(projectial)):
#                 print(f"{projectial[i]}")
#         if w_choice == 2:
#             m_choice = int(input("\n1 = Swords\n2 = daggers\n"))
#             if m_choice == 1:
#                 for i in range(len(swords)):
#                     print(f"{swords[i]}")
#             if m_choice == 2:
#                 for i in range(len(daggers)):
#                     print(f"{daggers[i]}")
#     if choice == 2:
#         pass
#     if choice == 3:
#         a_choice = int(input("\n1 = chestplate\n2 = gloves\n3 = leggings\n4 = helmet\n"))
#         if a_choice == 1:
#             for i in range(len(chestplate)):
#                 print(f"{chestplate[i]}")
#         if a_choice == 2:
#             for i in range(len(gloves)):
#                 print(f"{gloves[i]}")
#         if a_choice == 3:
#             for i in range(len(leggings)):
#                 print(f"{leggings[i]}")
#         if a_choice == 4:
#             for i in range(len(helmet)):
#                 print(f"{helmet[i]}")
#     if choice == 4:
#         for i in range(len(helmet)):
#             print(f"{helmet[i]}")
#         for i in range(len(leggings)):
#             print(f"{leggings[i]}")
#         for i in range(len(gloves)):
#             print(f"{gloves[i]}")
#         for i in range(len(chestplate)):
#             print(f"{chestplate[i]}")
#         for i in range(len(swords)):
#             print(f"{swords[i]}")
#         for i in range(len(projectial)):
#             print(f"{projectial[i]}")

