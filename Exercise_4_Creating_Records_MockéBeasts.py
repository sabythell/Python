#MockéBeasts is a video game where a lone child stalks the wilderness to capture tiny monsters in small plastic orbs, it sounds very familiar. The developer of MockéBeasts wants to build a MockéDex to store the information about them in an easily accessible manner.

#Build a command line tool to take in the following information in a loop:

#Beast Name
#Beast Type (Must be Earth, Fire, Air, Water or Spirit)
#Special Move
#Starting HP (A value between 1 and 999)
#Starting MP (A value between 1 and 999)
#Add functionality to be able to add each beast to a 2D data structure

#Add a pretty print function that prints out the list of beasts nicely after each one has been added

#Extension
#Update your pretty print function so that the output includes the index value of the record in the 2D list, this should be amended so that the first beast is number 1, the second is number 2, etc.

total_beasts = 2 #modify to change the total amount of inputs into the mokédex
beast_count = 0 #beast count set to 0 for the empty mokédex
mockeDex = [] #empty list for mokédex
beast_type = "" #empty string for beast type
beast_name = "" #empty string for beast name
special_move = "" #empty string for special move
hp = 0 #hp set to 0
mp = 0 #mp set to 0
typelist = ["earth","fire","air","water","spirit"] #type list available for beasts

def specialMove():
    global special_move
    special_move = input("Special Move: ").upper()
    if special_move == "":
        print("ERROR: Input cannot be left blank, please try again")
        specialMove()
    else:
        pass
def beastName():
    global beast_name
    beast_name = input("Beast Name: ").upper()
    if beast_name == "":
        print("ERROR: Input cannot be left blank, please try again")
        beastName()
    else:
        pass
def beastType():
    global beast_type
    beast_type = input("Beast Type: ").upper()
    if beast_type.lower() not in typelist:
        print("ERROR: Input not recognised, please enter from the following list: Earth, Fire, Air, Water or Spirit")
        beastType()

    else:
        pass
def HP():
    global hp
    hp = input("Starting HP: ")

    if str(hp) == "":
        print("ERROR: Input cannot be left blank, please try again.")
        HP()

    if (int(hp)<1 or (int(hp)>999)):
        print("ERROR: HP must be between 1 and 999")
        HP()

    else:
        pass
def MP():
    global mp
    mp = input("Starting MP: ")

    if str(mp) == "":
        print("ERROR: Input cannot be left blank, please try again.")
        MP()

    if (int(mp)<1 or (int(mp)>999)):
        print("ERROR: MP must be between 1 and 999")
        MP()

    else:
        pass

print("Please enter below the " + str(total_beasts) + " Mockébeasts from the region")

while(beast_count < total_beasts):
    beastName()
    beastType()
    specialMove()
    HP()
    MP()
    beast_count += 1
    beast_entry = ["MockéNo.",beast_count,"NAME:",beast_name.title(),"SPECIAL MOVE:",special_move.title(),"HP:",hp,"MP:",mp]
    mockeDex.append(beast_entry)
print("")    
print("------------------------------MokéDex------------------------------")

for beast in mockeDex:
    if beast_entry[1] != 1:
        print("")

    else:
        pass
    for stat in beast:
        print(stat, end=" ")

