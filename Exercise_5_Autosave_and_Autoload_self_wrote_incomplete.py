#instructions:
    #You have been given a basic version of a video game rentals program (It's like I've been looking back through the old code or something!), 
    # extend this program so that it:
    #Uses a 2D list to store the data
    #Uses autosave to store the data in a file called gameRentals.txt
    #Use autoload to load the 2D list from the gameRentals.txt file on each load
    #You'll see that the program also contains a list of customers in a file called customers.txt, write some autoload code to create a list called customers that loads this data
    #Extend the program to be able to create customers
    #Write an autosave function to be able to save the customers list back to customers.txt, you should not delete any existing customers whilst doing this
    #Extension
    #Go back through any of your other exercise files that used 2D lists and add in code to use autosave and autoload, making sure that the file names 
    #you are using to store you data in are sensible

    #example customers.txt [['Ian Smith', 'ian@test.com'], ['Penny Morgan', 'penny@test.com']]

import time, os
name = ""
email = ""
row = ""
customers = []
try:
    file = open("customers.txt", "r")
    customers = eval(file.readline())
    file.close()
except:
    pass

def banner(x):
    print("VIDEO GAME RENTALS INC")
    print(x)
    print("")


def newCustomer():
    global name
    global email
    global row
    global customers
    os.system('cls')
    banner('New Customer')
    name = input("Please enter the customer's name: ")
    email = input("Please enter the customer's email address: ")
    row = [name.upper(), email.upper()]
    customers.append(row)

def existingCustomers():
    global name
    global email
    global row
    global customers
    os.system('cls')
    banner('Existing Customers')
    for customer in customers:
        print("")
        for data in customer:
            print(data, end=" ")
            print("")
    file = open("customers.txt", "w")
    file.write(str(customers))
    file.close()
    print("")
    print("Press enter to return to the main menu.")
    input(">: ")
    menu()

def menu():
    os.system('cls')
    banner('Main Menu')
    print("Press 1 to add new customer")
    print("Press 2 to view existing customers")
    print("Press 3 to close the application")
    choice = input(">: ")

    if choice == "1":
        newCustomer()
    if choice == "2":
        existingCustomers()
    if choice == "3":
        os.system('cls')
        time.sleep(1)
        quit()
    else:
        menu()
menu()



