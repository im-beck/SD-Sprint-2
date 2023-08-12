# Written by: SD 9 Robot Group 1 A.K.A Python Punishers
# Written on: 2023/08/012
# Description: Collects information about Car Rentals.


# Import Libraries

import Modules.Stylizer as S
from Modules.Validizer import Validate as V
import datetime as DT

# Constants
Curr_Date = DT.datetime.now()
Allowed_Characters = "0123456789"
carLST = ["1","2","3","4"]

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
            
            carNum = (input("Enter the Car Number (1,2,3,4): "))
            if carNum is not carLST():
                 print("Error: Invalid entry, must provide car number 1-4.")
                 continue
            elif carNum != "":
                 print("Error: Invalid entry, must provide car number.")
                 continue
            elif not all (char in Allowed_Characters for char in carNum):
                 print("Error: Invalid entry, must provide number.")
                 continue
                 



# Calculations

# Output
