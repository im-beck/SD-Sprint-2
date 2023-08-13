# Written by: SD 9 Robot Group 1 A.K.A Python Punishers
# Written on: 2023/08/012
# Description: Collects information about Car Rentals.


# Import Libraries

import Modules.Stylizer as S
from Modules.Validizer import Validate as V
import datetime as DT
from datetime import timedelta

# Constants
Curr_Date = DT.datetime.now()
Allowed_Characters = "0123456789"
carLST = ['1','2','3','4']

# Inputs
while True:
        rentId = input("What is the rental ID?: ")
        if rentId == "":
            print("Error: ID is Invalid.")
            continue
        elif not all(char in Allowed_Characters for char in rentId):
            print("Error: Invalid entry, must provide integers only.")
            continue
    
        while True:

            driverNum = (input("Enter the driver number (111111): "))

            if driverNum == "":
                print("Error: Driver number is Invalid. Please enter a valid driver number.")
                continue
            elif len(driverNum) != 6:
                print("Error: Driver number must be 6 characters.")
                continue
            elif not all(char in Allowed_Characters for char in driverNum):
                print("Error: Invalid entry, must provide integers only.")
                continue

            startRental = V(V.date, "Enter the start date of the rental (YYYY-MM-DD): ")
            
            while True:
                carNum = (input("Enter the Car Number (1,2,3,4): "))
                if carNum not in carLST:
                    print("Error: Invalid entry, must provide car number 1-4.")
                    continue
                
                rentTime = input("Is the Rental for a day or a week? (D/W): ").upper()
                if rentTime == "":
                    print("Error: Must input D for Day, W for a week.")
                    continue
                elif rentTime == "W":
                    Week = 7
                    print(Week)
                elif rentTime == "D":
                    dailyTime = Curr_Date.replace(hour=12, minute=0, second=0, microsecond=0)
                    FormattedTime = dailyTime.strftime("%Y-%m-%d %H:%M")
                    print(FormattedTime)
                    break

            while True:
                rentCost = float(input("Enter the rental cost: "))
                if rentCost == "":
                    print("Error: Please enter the rental cost.")
                    continue
                elif not all (char in Allowed_Characters for char in rentCost):
                    print("Error: Must only use integers.")
                    continue
                
                taxCost = float(input("Enter the tax cost: "))
                if taxCost == "":
                    print("Error: Must enter a tax cost.")
                    continue
                elif not all (char in Allowed_Characters for char in taxCost):
                    print("Error must only use integers.")
                    continue
                
                totalCost = float(input("Enter the total cost: "))
                if totalCost == "":
                    print("Error: Must enter a total cost.")
                    continue
                elif not all (char in Allowed_Characters for char in totalCost):
                    print("Error must only use integers.")
                    continue
                
                
# Calculations

# Output
