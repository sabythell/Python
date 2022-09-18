#Phones4Us is an independent mobile phone retailer in Cardiff. You need to build a command line tool to do the following:
#a. Allow a sales assistant to enter the Customer name, Name of phone, size of phone and Contract length (months)

#b. Calculate the cost of the phone using the table below

#                  Mini	              Regular	           Max
#iPhone 12	      799.99	            999.99	            X
#iPhone 12 Pro   	X	                1099.00	         1190.00
#c. Work out the monthly cost, which £10 per month plus the cost of the phone divided by the length of the contact. 
# E.g. iPhone 12 Pro over 36 months. Cost of phone = £1099, monthly cost = 1099/36 = 30.53, plus monthly cost 30.53 + 10 = 40.53

import time

cost = 0
monthly_cost = 10
contract_length = ""
phone_check = False

print("     PHONES")
print("       4")
print("      U S")

customer_name = input("Please enter the customer's Name: ")

while phone_check == False:
    phone = input("Please enter the name of the phone: ")
    size = input("Please enter the size of the phone: ")
    if phone.lower() == "iphone12":
        if size.lower() == "mini":
            cost = 799.99
            phone_check = True
        elif size.lower() == "regular":
            cost = 999.99
            phone_check = True
        elif size.lower() == "max":
            print(phone.upper() + " not available in this size")
        else:
            print("Size or Phone input not recognised, please try again.")
    if phone.lower() == "iphone12pro":
        if size.lower() == "mini":
            print(phone.upper() + " not available in this size")
        elif size.lower() == "regular":
            cost = 1099.00
            phone_check = True
        elif size.lower() == "max":
            cost = 1190.00
            phone_check = True
        else:
            print("Size or Phone input not recognised, please try again.")

while contract_length == "":    
    contract_length = input("Please enter the contract length: ")
    if contract_length == "":
        print("Contract length cannot be left blank, please try again")
    if contract_length.isnumeric() == False:
        print("Input not recognised as a number, please try again.")
        contract_length = ""

contract_monthly_cost = int(monthly_cost) + (int(cost) / int(contract_length))
print("-")
print("-")
print("-")
time.sleep(2)
print("CONTRACT FOR " + customer_name.upper())
print(phone.upper() + " " + size.upper() + " OVER " + str(contract_length) + " MONTHS.")
print("MONTHLY COST: £" + str(round(contract_monthly_cost, 2)))
