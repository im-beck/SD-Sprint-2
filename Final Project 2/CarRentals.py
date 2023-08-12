# Written by: SD 9 Robot Group 1 A.K.A Python Punishers
# Written on: 2023/08/012
# Description: Collects information about Car Rentals.

Allowed_Characters = "0123456789"
# Import Libraries

import Modules.Stylizer as S
from Modules.Validizer import Validate as V
import datetime as DT

# Constants
Curr_Date = DT.datetime.now()

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


# Calculations

# Output

