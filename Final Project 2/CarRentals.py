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

        startRental = input("Enter the start date of the rental (YYYY-MM-DD): ")
        startRentalFormat = DT.datetime.strptime(startRental, "%Y-%m-%d")
        
        
        carNum = (input("Enter the Car Number (1,2,3,4): "))
        if carNum not in carLST:
                print("Error: Invalid entry, must provide car number 134-4.")
                continue
            
        rentTime = input("Is the Rental for a day or a week? (D/W): ").upper()
        if rentTime == "":
                print("Error: Must input D for Day, W for a week.")
                continue
        elif rentTime == "W":
                Week = 7
        elif rentTime == "D":
                dailyTime = Curr_Date.replace(hour=12, minute=0, second=0, microsecond=0)
                FormattedTime = dailyTime.strftime("%Y-%m-%d %H:%M")
        else:
               print("Error: Invalid entry, must provide D or W.")

        
        rentCost = (input("Enter the rental cost: "))
        if rentCost == "":
                print("Error: Please enter the rental cost.")                    
        elif all(char.isdigit() or char in ('.', '-') for char in rentCost):
                rentCost = float(rentCost)
        else:
                print("Error: Please enter the rental cost")
                continue

        
        taxCost = (input("Enter the tax cost: "))
        if taxCost == "":
                    print("Error: Must enter a tax cost.")                    
        elif all(char.isdigit() or char in ('.', '-') for char in taxCost):
                    taxCost = float(taxCost)                    
        else:
                print("Error: Must enter a tax cost.")  
                continue
        
        
        totalCost = (input("Enter the total cost: "))
        if totalCost == "":
                    print("Error: Must enter a total cost.")
        elif all(char.isdigit() or char in ('.', '-') for char in totalCost):
                    totalCost = float(totalCost)
        else: 
            print("Error: Must enter a total cost.")
            continue 
        
        f = open('Rentals.dat', 'a')
        with open("Rentals.dat", "a") as f:
            f.write(f"Rental ID: {rentId}, ")
            f.write(f"Driver Num: {driverNum}, ")
            f.write(f"Start Date: {startRentalFormat}, ")
            f.write(f"Car Number: {carNum}, ")
            f.write(f"Time Rented: {FormattedTime}, ")
            f.write(f"Rent Cost: ${rentCost}, ")
            f.write(f"Tax Cost: ${taxCost}, ")
            f.write(f"Total Cost: ${totalCost}\n")
            f.close()



# Calculations

# Output
