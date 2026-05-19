# *** we should make functions for all options ***
# *** we have always to deal with unexpected user input ***

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import pandas as pd

def addTicket(ticketID, eventName, customerName, eventDate, price, quantity ):
    """this function let the user to enter a ticket by providing it's detelis"""
    if not ticketID or not eventName or not customerName or not eventDate or not price or not quantity:
        return "All are requierd, Fail to continue"
    else:
        try:
            ticketID = int(ticketID)
            price = int(price)
            quantity = int(quantity)
        except:
            return "\nTicket ID, Price, And quantity all should be numbers"
        try:
            datetime.strptime(eventDate, "%Y-%m-%d")
        except:
            return "\nEvent Date should be in this format: YYYY-MM-DD for example: 2024-03-23"
    with open("tickets.csv", 'r', newline="") as file:
        content = csv.reader(file)
        for row in content:
            if row[0] == "Ticket_ID":
                continue
            if int(row[0]) == ticketID:
                return  "\nThis Ticket ID Is Already Taken"

    totalCost = price * quantity

    with open("tickets.csv", 'a', newline="") as file:
        pen = csv.writer(file)
        pen.writerow([ticketID,eventName,customerName,eventDate,price,quantity,totalCost])
    return "\nAdd Successfully"

def displayAll():
    """this function display all tickets with detelis in clean and nice way"""
    allTickets = ""
    with open("tickets.csv", "r", newline="") as file:
        read = csv.reader(file)
        for row in read:
                allTickets +=  f"\n\nTicket ID: {row[0]}\nEvent Name: {row[1]}\nCustomer Name: {row[2]}\nEvent Date: {row[3]}\nTicket Price: {row[4]}\nTickets Quantity: {row[5]}\nTotal Cost: {row[6]}\n\n"
        return allTickets

def search(ticketID):
    """this function enable the user to search on a ticket by it's id """
    with open("tickets.csv", "r", newline="") as file:
        read = csv.reader(file)
        for row in read:
            if ticketID == row[0]:
                return f"\n\nTicket ID: {row[0]}\nEvent Name: {row[1]}\nCustomer Name: {row[2]}\nEvent Date: {row[3]}\nTicket Price: {row[4]}\nTickets Quantity: {row[5]}\nTotal Cost: {row[6]}\n\n"
            # else:
            #     return "\nThere Are No Ticket With Same ID\n"
        return "\nThere Are No Ticket With Same ID\n"

def reaports():
    df = pd.read_csv("tickets.csv")
    plt.figure(figsize=(11, 5))
    plt.suptitle("Sales by Enent and Date")
    eventSalesTable = df.groupby("Event")[["Cost"]].sum()
    eventSalesTable.columns = ["Sum of Sales by Event"]
    
    dateSalesTable = df.groupby("Date")[["Cost"]].sum()
    dateSalesTable.columns = ["Sum of Sales by Date"]

    plt.subplot(1, 2, 1)
    eventSalesChart = plt.bar(eventSalesTable.index, eventSalesTable["Sum of Sales by Event"], color="skyblue", edgecolor="black", width=0.6)
    plt.title("Events Sales", loc="left")
    plt.xlabel("Events")
    plt.ylabel("Sales")

    plt.subplot(1, 2, 2)
    dateSalesChart = plt.plot(dateSalesTable.index, dateSalesTable["Sum of Sales by Date"], color="darkred", marker='o', markerfacecolor="g", markeredgecolor="g", markersize=8)
    plt.title("Sales Over Time", loc="left")
    plt.xlabel("Date")
    plt.ylabel("Sales")

    plt.show()

    salesMean = df["Cost"].mean()
    salesMax = df["Cost"].max()
    salesMin = df["Cost"].min()
    maxDate =  df[df["Cost"] == salesMax]["Date"]
    minDate =  df[df["Cost"] == salesMin]["Date"]
    Discriptive_Statisticas = f"\nAverage Sales: {round(salesMean, 2)} Tickets\nMaximum Sales: {salesMax} Tickets  (on {maxDate.to_string(index=False)})\nMinimum Sales: {salesMin} Tickets  (on {minDate.to_string(index=False)})\n"


    print("\n",eventSalesTable)
    print("\n",dateSalesTable)
    print("\n",Discriptive_Statisticas)

user_name = "admin"
password = "admin123"
ongoing = True
longin =  True
services = True

while ongoing:
    print("\n*** Welcome to Ticket Sales Management System ***\n")
    print("LongIn to Start")
    print("1. LongIn\n2. Exite:\n")
    answer = input("\n Please Choose a Number: ")
    # long in ask for user_name and password if correct go to next if not continue again
    if answer == "1":
        longin = True
        while longin:
            user_name_answer = input("Enter the UserName: ").lower()
            password_answer = input("Enter the password: ").casefold()
            # if both true long in and bring the service options
            if user_name_answer == user_name and password_answer == password:
                while services:
                    print("\n*** Our Services ***")
                    print("1. Enter Your Ticket Details\n2. View TicKet Details\n3. Search by Ticket ID\n4. Produce Reports\n5. Return to HomePage\n6. Exite")
                    answer = input("\n Please Choose a Number: ")
                    # Let user to inter a Ticket info (ID should be unique, Event Name, Customer Name, Date, Ticket Price, Quantity)
                    # and the programm should culculate the total cost
                    # finally we have to save the all infos in csv file
                    if answer == "1":
                        ticketID = input("Please Enter Ticket ID (Numbers only): ")
                        eventName = input("Please Enter Event Name: ").lower()
                        customerName = input("Please Enter Your Name: ").lower()
                        eventDate = input("Please Enter Event Date in this format (YYYY-MM-DD): ")
                        price = input("Please Enter Ticket Price (Number only): ")
                        quantity = input("Please Enter Tickets Quantity (Number only): ")
                        print(addTicket(ticketID,eventName,customerName, eventDate,price,quantity))
                    # this choice should display all the info form the csv file in clean and bueatiful way
                    elif answer == "2":
                        print(displayAll())
                    # Search a Ticket by id and disply all it's infos if it avalible but if it not in csv print a massge said that 
                    elif answer == "3":
                        ticketID = input("\nPlease Enter The ID Of the  (Numbers only): ")
                        print(search(ticketID))
                        
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
                        reaports()
                    elif answer == "5":
                        longin = False
                        break
                    elif answer == "6":
                        ongoing = False
                        longin = False
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
                    longin =False
                # to deal with unexpected user input
                else:
                    print("** Please Enter a Number, Ehither 1 or 2! **")
                    break

    # exite option to close the loop
    elif answer == "2":
        break
    # to deal with unexpected user input
    else:
        print("** Please Enter a Number, Ehither 1 or 2! **")
        continue