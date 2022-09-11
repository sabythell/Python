#You have been asked to create a command-line program that uses validation to update your student contact information for your school. When the program is run it needs to ask for the following pieces of data:

#First name (Cannot be blank)
#Surname (Cannot be blank)
#Mobile Phone number (Must be 11 digits long)
#Year group: (Must be between 7 and 11)
#Gender (Options: Male, Female, Other) Feel free to list other genders rather than just using 'Other' but do think about the time this would take you to make a comprehensive list if this were in an NEA and therefore time sensitive
#Email (Cannot be blank, must contain an @ and a . )
#You need to ensure that you use appropriate error messages to communicate to the user any mistakes they are making.

#Extension
#Date of Birth (Must be in standard British format DD/MM/YYY, year must be less than the current year)
#Add a splash screen and menu to the program so that it becomes easier to use##

import time, os, site

first_name = input("First Name: ")
while(first_name==""):
    print("ERROR: First Name entry cannot be left blank, please try again!")
    first_name = input("First Name: ")
    if first_name.isalpha() == False:
        print("ERROR: Your input contains more than just letters, please try again.")
        first_name = input("First Name: ")

surname = input("Surname: ")
while(surname==""):
    print("ERROR: Surname entry cannot be left blank, please try again!")
    surname = input("Surname: ")
    if surname.isalpha() == False:
        print("ERROR: Your input contains more than just letters, please try again.")
        surname = input("Surname: ")

mobile = input("Mobile Number: ")
while(mobile==""):
    print("ERROR: Mobile Number entry cannot be left blank, please try again!")
    mobile = input("Mobile Number: ")
    if mobile.isnumeric() == False:
        print("ERROR: Your input contains more than just numbers, please try again.")
        mobile = input("Mobile Number: ")
    if int(len(mobile)) != 11:
        print("ERROR: You have not entered the correct amount of numbers for a UK mobile phone number, please try again.")
        mobile = input("Mobile Number: ")

year_group = int(input("Year Group: "))
while(year_group<7 or year_group>11):
    print("ERROR: Incorrect year group entered, please enter a year group from Year 7 to Year 11.")
    year_group = int(input("Year Group: "))

gender_list = ["male", "female", "other"]
gender = input("Please enter your Gender: ")

while (gender.lower() not in gender_list):
    print("ERROR: Gender not recognised, please select from Male, Female or Other.")
    gender = input("Please enter your Gender: ")

correct_email = False
doublecheck = False
stopcheck = False
atcheck = False

email = input("Please enter your email address: ")

while email == "":
    print("Email entry cannot be left blank, please try again")
    email = input("Please enter your email address: ")

while doublecheck == False:
    if "@" in email:
        atcheck = True
    if "." in email:
        stopcheck = True
    if atcheck == True and stopcheck == True:
        doublecheck == True
        print("Thank you for updating your details on our system, have a good day!")
        time.sleep(2)
        quit()
    else:
        print("Incorrect email address entered, please ensure it contains both '.' and '@'")
        stopcheck = False
        atcheck = False 
        email = input("Please enter your email address: ")

