# *** we should make functions for all options ***
# *** we have always to deal with unexpected user input ***

import pandas as pd
import matplotlib.pyplot as plt



user_name = "admin"
password = "admin123"
ongoing = True

while ongoing:
    print("\n*** Wecome to --- ***\n")
    print("LongIn to Start")
    print("1. LongIn\n2. Exite:\n")
    answer = input("\n Please Choose a Number: ")
    # long in ask for user_name and password if correct go to next if not continue again
    if answer == "1":
        while ongoing:
            user_name_answer = input("Enter the UserName: ").lower()
            password_answer = input("Enter the password: ").casefold()
            # if both true long in and bring the service options
            if user_name_answer == user_name and password_answer == password:
                print("\n*** Our Services ***")
                print("1. Enter Your Ticket Details\n2. View TicKet Details\n3. Search by Ticket ID\n4. Produce Reports\n5. Return to HomePage\n6. Exite")
                answer = input("\n Please Choose a Number: ")
                # Let user to inter a Ticket info (ID should be unique, Event Name, Customer Name, Date, Ticket Price, Quantity)
                # and the programm should culculate the total cost
                # finally we have to save the all the infos in csv file
                if answer == "1":
                    pass
                # this choice should display all the info form the csv file in clean and bueatiful way
                elif answer == "2":
                    pass
                # Search a Ticket by id and disply all it's infos if it avalible but if it not in csv print a massge said that 
                elif answer == "3":
                    pass
                # display all reports

                # 1. all sales by Event for example: 
                # football 23
                # basketball 42 and so on for the csv info

                # 2. bar chart for (1)

                # 3. salse over time, for example:
                # 2023-10-10  3
                # 2024-05-19  42

                # 4. Line chart for (3)

                # 5. Discriptive Statisticas (focuse on quantity):
                #    1. Avrage sales, like# Average Sales: 5 Tickets/day
                #    2. max sales, like# Maximum Sales: 10 Tickets  (on 2025-02-16)
                #    3. min sales like# Minimum Sales: 2 Tickets  (on 2023-11-06)

                elif answer == "4":
                    pass
                elif answer == "5":
                    break
                elif answer == "6":
                    ongoing = False
                    break
                    # to deal with unexpected user input
                else:
                    print("** Please Enter a Number, From 1 to 5! **")

            # if it dont match display a notification and continue again
            else:
                print("\n** Wrong Password or UserName **")
                print("1. Try again\n2. Return to HomePage\n")
                answer = input("\n Please Choose a Number: ")
                # to try again
                if answer == "1":
                    continue
                # to retunt to homePage
                elif answer == "2":
                    break
                # to deal with unexpected user input
                else:
                    print("** Please Enter a Number, Ehither 1 or 2! **")

    # exite option to close the loop
    elif answer == "2":
        break
    # to deal with unexpected user input
    else:
        print("** Please Enter a Number, Ehither 1 or 2! **")