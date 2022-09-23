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

ian = ['Ian Smith', 'ian@test.com']
penny = ['Penny Morgan', 'penny@test.com']
customers = []
gameRentals = []
try:
    f = open("gameRentals.txt", "r")
    gameRentals = eval(f.readline())
    f.close()
except:
    pass
try:
    customer_f = open("customers.txt", "r")
    customers = eval(customer_f.readline())
    f.close()
except:
    pass

def addRental():
  customer = input("Customer: ")
  item = input("Game: ")
  price = float(input("Price per night: "))
  nights = int(input("Nights: "))
  total = round(price*nights,2)
  row = ["Customer Name:",customer, "Game:",item,"Cost:",price,"Nights Rented:",nights,"Total Cost:",total]
  gameRentals.append(row)
  returned = False

  #You'll probably want to start here
  print("Added successfully")
  time.sleep(1)

def viewRentals():
  global gameRentals
  print("RENTAL HISTORY")
  for row in gameRentals:
    print("")
    for item in row:
      print(item, end=" ")
      print("")
    print()
  f = open("gameRentals.txt", "w")
  f.write(str(gameRentals))
  f.close()
  print("Press enter to return to the main menu")
  input(">: ")

def newCustomer():
    os.system('cls')
    print("New Customer")
    name = input("Please enter the customer's name: ")
    email = input("Please enter the customer's email address: ")
    row = [name, email]
    customers.append(row)


def existingCustomers():
    os.system('cls')
    print("Existing Customers")
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

while(True):
  print("🎮 GAME RENTALS 🎮")
  print("   ===========")
  print("Press 1 to add new Rental")
  print("Press 2 to view Rentals")
  print("Press 3 to add new customer")
  print("Press 4 to view existing customers")
  menuChoice = input("> ")

  if(menuChoice=="1"):
    addRental()
  elif(menuChoice=="2"):
    viewRentals()
  elif(menuChoice=="3"):
    newCustomer()
  elif(menuChoice=="4"):
    existingCustomers()
  else:
    print("ERROR: Unknown Option")
    time.sleep(1)
  
  time.sleep(1)
  os.system('cls')