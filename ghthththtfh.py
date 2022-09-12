chestplate = []
gloves =     []
leggings =   []
helmet =     []
projectial = []
male =       []
armour =     [chestplate, gloves, leggings, helmet]
magic =      []
weapons =    []
inv =        [weapons, magic, armour]

chestplate.append("Bronze Chestplate")
chestplate.append("Iron Chestplate")
chestplate.append("Diamond Chestplate")
chestplate.append("Mithiral Chestplate")
chestplate.append("Adamnite Chestplate")
chestplate.append("Ruiniate Chestplate")
chestplate.append("Stygiate Chestplate")
chestplate.append("Netherite Chestplate")



def inva():
    choice = int(input("\n1 = Weapons\n2 = magic\n3 = Armour\n\n"))
    if choice == 1:
        w_choice = int(input("\n1 = Projectial\n2 = Male"))
        if w_choice == 1:
            for i in range(len(projectial)):
                print(f"{projectial[1]}")
        if w_choice == 2:
            for i in range(len(male)):
                print(f"{male[1]}")
    if choice == 2:
        pass
    if choice == 3:
        a_choice = int(input("\n1 = chestplate\n2 = gloves\n3 = leggings\n4 = helmet\n"))
        if a_choice == 1:
            for i in range(len(chestplate)):
                print(f"{chestplate[i]}")
        if a_choice == 2:
            for i in range(len(gloves)):
                print(f"{gloves[1]}")
        if a_choice == 3:
            for i in range(len(leggings)):
                print(f"{leggings}")
        if a_choice == 4:
            for i in range(len(helmet)):
                print(f"{helmet[1]}")
inva()