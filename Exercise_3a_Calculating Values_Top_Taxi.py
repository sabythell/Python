#Top Taxi Ltd. Is a taxi firm operating out of Central London. Build a command line program that allows them to do the following:
#a. A member of admin staff should be able to add all journeys for a particular taxi driver for an entire day, they should be expected to enter pick up location, 
#destinations and distance (miles).

#b. Calculate the subtotal of each journey charged at £0.50 per mile

#c. If the drive has completed more than 15 miles in one journey it is classified as 'long distance' and therefore is reduced in price by 30%

#d. After each of the taxi drivers journeys has been entered both the subtotal and the overall daily total should be displayed, to 2DP.

import os
from turtle import clear
price_per_mile = 0.5
total = 0
day_done = False
total_journey = 0
journey_list = []

print("               T O P  T A X I  L T D                    ")
print("Special offer: Journeys over 15 miles are reduced by 30%")
print("")

driver = input("Please enter the driver's name: ")

while day_done == False:
    pickup = input("Enter pick-up location: ")
    destination = input("Enter destination: ")
    journey_list.append(pickup + " to " + destination)
    distance = float(input("Enter miles travelled: "))
    subtotal = round((distance*price_per_mile), 2)
    if distance > 15:
        subtotal = round((subtotal * 0.7), 2)
    else:
        subtotal = round((distance*price_per_mile), 2)
    total += round(subtotal, 2)
    total_journey += 1
    day_over_check = False
    while day_over_check == False:
        day_over = input("Have you finished for the day? Please type 'y' for yes and 'n' for no: ")
        if day_over.lower() == "y":
            day_done = True
            day_over_check = True
            os.system('cls')
            print(driver)
            print("Journeys made: " + str(total_journey))
            print("Subtotal: £" + str(subtotal))
            print("Total: £" + str(total))
            print("Journeys: ")
            for journey in journey_list:
                print(journey)
        elif day_over.lower() == "n":
            day_done = False
            day_over_check = True
            print("Journeys made: " + str(total_journey))
            print("Subtotal: £" + str(subtotal))
            print("Total: £" + str(total))
        else:
            print("Input not recognised, please try again.")
            day_over_check = False

