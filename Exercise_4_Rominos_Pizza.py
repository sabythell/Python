import os
import time

pizzacount = 0
subtotal = 0.00
pizzalist = []
checkout_decision = False


def banner(x):
    special_offer = "SPECIAL OFFER - Buy 4 or more pizzas for a 33 % discount at checkout"
    print("W E L C O M E  T O  R O M I N O ' S  P I Z Z A")
    print(x.upper())
    print(special_offer)
    print("")

def order():
    global pizzacount
    global subtotal
    os.system('cls')
    banner('Order')
    print("Subtotal: ", str(subtotal))
    print("")
    print("Type '1' plus enter to add new pizza.")
    print("Type '2' plus enter to checkout.")
    print("Type '3' plus enter to clear your order.")
    print("Type '5' plus enter to return to the previous screen.")
    choice = input(">: ")
    if choice == "1":
        newpizza()
    if choice == "2":
        checkout()
    if choice == "3":
        subtotal = 0.00
        pizzacount = 0
        order()
    if choice == "5":
        menuScreen()
def final():
    global pizzacount
    global subtotal
    global checkout_decision
    total = 0.00
    if pizzacount > 3:
        total = subtotal * 0.67

    else:
        total = subtotal
    
    os.system('cls')
    banner('Checkout')
    print("Pizza Count:", str(pizzacount))
    print("Subtotal: £", str(round(subtotal, 2)))
    print("Total: £", str(round(total, 2)))
    quit()

def checkout():
    global pizzacount
    global subtotal
    global checkout_decision
    os.system('cls')
    banner('Checkout')
    print("Pizza Count:", str(pizzacount))
    print("Subtotal: ", str(subtotal))

    rush = input("Would you like your order as standard or rush? Please type '1' for standard and '2' for rush and press enter: ")
    if rush == '1':
        delivery = input("Would you like your order to be delivered or collected? Please type '1' for delivery or '2' for collection and press enter: ")
        if delivery == '1':
            subtotal += 0.99
            final()
        if delivery == '2':
            subtotal += 0
            final()
        else:
            print("Input not recognised please try again.")
            time.sleep(2)
            os.system('cls')
            final()
    if rush == '2':
        delivery = input("Would you like your order to be delivered or collected? Please type '1' for delivery or '2' for collection and press enter: ")
        if delivery == '1':
            subtotal += 3.99
            final()
        if delivery == '2':
            subtotal += 1.99
            final()
        else:
            print("Input not recognised please try again.")
            time.sleep(2)
            os.system('cls')
            checkout()



def newpizza():
    global pizzacount
    pizzacount = pizzacount
    global subtotal
    os.system('cls')
    banner('New pizza')
    print("Type '5' plus enter to return to the previous screen.")
    print("")
    print("Subtotal: ", str(subtotal))
    print("")
    choice = input("What type of pizza would you like? Thin, Italian or Pan?: ")
    
    if choice.lower() == "thin":
        size = input("What size pizza would you like? Small, Medium or Large?: ")
        if size.lower() == "small":
            cost = 4.99
            subtotal += cost
            pizzacount += 1
            order()
        if size.lower() == "medium":
            cost = 7.99
            subtotal += cost
            pizzacount += 1
            order()
        if size.lower() == "large":
            cost = 10.99
            subtotal += cost
            pizzacount += 1
            order()

    if choice.lower() == "italian":
        size = input("What size pizza would you like? Small, Medium or Large?: ")
        if size.lower() == "small":
            cost = 5.49
            subtotal += cost
            pizzacount += 1
            order()
        if size.lower() == "medium":
            cost = 8.99
            subtotal += cost
            pizzacount += 1
            order()
        if size.lower() == "large":
            cost = 12.49
            subtotal += cost
            pizzacount += 1
            order()

    if choice.lower() == "pan":
        size = input("What size pizza would you like? Small, Medium or Large?: ")
        if size.lower() == "small":
            cost = 5.99
            subtotal += cost
            pizzacount += 1
            order()
        if size.lower() == "medium":
            cost = 9.99
            subtotal += cost
            pizzacount += 1
            order()
        if size.lower() == "large":
            cost = 13.99
            subtotal += cost
            pizzacount += 1
            order()

    if choice == "5":
        order()

    else:
        print("Input not recognised please try again")
        time.sleep(2)
        os.system('cls')
        newpizza()

def prices():
    os.system('cls')
    banner('Prices')
    print('''
    	Small	Medium	Large
Thin	4.99	7.99	10.99
Italian	5.49	8.99	12.49
Pan	5.99	9.99	13.99
    ''')

    print('''
    	        Rush	Standard
Delivery	3.99	0.99
Collection	1.99	0
    ''')
    print("")
    print("SPECIAL OFFER: Order 4 or more pizzas and receive a 33 percent discount at checkout. ")
    print("Press '5' and enter to return to the main menu: ")
    choice = input(">: ")
    if choice == "5":
        menuScreen()

    else:
        print("Input not recognised, please try again.")
        time.sleep(2)
        prices()

def menuScreen():
    os.system('cls')
    banner('menu screen')
    print("Type '1' plus enter to go to our ordering screen.")
    print("Type '2' plus enter to see our prices.")
    print("Type '5' plus enter to quit.")
    choice = input(">: ")
    if choice == "1":
        order()
    if choice == "2":
        prices()
    if choice == "5":
        os.system('cls')
        banner('Thank you for visiting us today, please come back soon!')
        time.sleep(2)
        quit()

    else:
        print("Input not recognised, please try again.")
        time.sleep(2)
        menuScreen()

menuScreen()
