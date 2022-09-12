from mains import *
from mains.game import *





print(money)


def prestiage_choice():
    p_choice = int(input("\n1 = p1\n2 = p2\n3 = p3\n4 = p4\n5 = p5\n6 = p6\n"))
    if p_choice == 1:
        multiplier.pstats.p1 = True
    if p_choice == 2:
        multiplier.pstats.p2 = True
    if p_choice == 3:
        multiplier.pstats.p3 = True
    if p_choice == 4:
        multiplier.pstats.p4 = True
    if p_choice == 5:
        multiplier.pstats.p5 = True
    if p_choice == 6:
        multiplier.pstats.p6 = True
    



def fight():
    f_choice = int(input("\n1 = slime\n"))
    if f_choice == 1:
        slime()



    
while O_F:
    level()
    choice = input("\n1 = prestaige\n2 = Fight\n3 = Inv\n4 = shop\nAnything else = Quit\n")
    if choice == "1":
        prestiage_choice()
    if choice == "2":
        fight()
    if choice == "3":
        inva()
    if choice == "4":
        choice = input("\n1 = Sell\n2 = Buy\nAnything else = back")
        if choice == "1":
            sell()
        if choice == "2":
            buy()
    else:
        O_F = False
        os.system('pause')

    sleep(0.01)















