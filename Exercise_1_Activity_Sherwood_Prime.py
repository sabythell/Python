import time, os, site
from turtle import clear

print("    Welcome to")
print("")
print("     SHERWOOD")
print("      Prime")
print(" One stop Shopping")


def Books():
    print("Our books section is coming soon, you might need to go into an actual store until then. Sorry.")
    print("")
    time.sleep(2)
    pass
def Movies():
    print("Yeah, sorry. It's Netflix or your local multiplex until our developer sorts themselves out. Sorry.")
    print("")
    time.sleep(2)
    pass

def My_Account():
    pass

time.sleep(2)
os.system('cls')

while(True):

    print("          S H E R W O O D   P R I M E          ")
    print("- - Enter the number to make your selection - -")
    print("")
    print("1.  Books")
    print("2.  Movies")
    print("3.  My Account")
    print("4.  Exit")

    menuSelection = input("> ")

    if menuSelection == "1":
        Books()
    elif menuSelection == "2":
        Movies()
    elif menuSelection == "3":
        My_Account()
    elif menuSelection == "4":
        exit()



