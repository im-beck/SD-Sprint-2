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

        EmpIDs = []
        with open('Employees.dat', 'r') as f:
                for data in f:
                    dataLine = data.split(",")
                    EmpIDs.append(dataLine[0].strip())
        while True:
                EmpID = input("Enter Driver Number: ")
                if EmpID not in EmpIDs:
                    print("Driver number does not match our records. Please try again.")
                else:
                    break
                
        rentId = input("What is the rental ID?: ")
        if rentId == "":
            print("Error: ID is Invalid.")
            continue
        elif not all(char in Allowed_Characters for char in rentId):
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
         



# Calculations

        Defaults = {}
        with open('Defaults.dat', 'r') as f:
               for i in f.read().split(", "):
                v = i.split(":")
                Defaults[v[0]] = V.number(v[1])[1]
             
                Daily = Defaults["DailyRentalFee"]
                Weekly = Defaults["WeeklyRentalFee"]
                taxes = Defaults["HST"]

                if rentTime == "W":
                      subTotal = (Weekly * taxes)
                      totalCost = subTotal + Weekly
                elif rentTime == "D":
                      subTotal = (Daily * taxes)
                      totalCost = subTotal + Daily  


        Data = {}
        with open('Employees.dat') as f:
            for i in f.read().split("\n"):
                line = i.split(", ")
                for x, v in enumerate(line):
                    error, val = V.number(v)
                    if not error:
                        line[x] = val
                Data[line[0]] = line[1:]
        for i in Data:
                Data[i][len(Data[i])-1] += totalCost
        comp = ""
        for i in Data:
            if comp == "":
                comp = i
            else:
                comp = f"{comp}{i}"
            for x in Data[i]:
                comp = f"{comp}, {x}"
            comp = f"{comp}\n"
   # Add files for future reference.
        with open('Rentals.dat', 'a') as r:
                f.write(f"{rentId}, ")
                f.write(f"{EmpID}, ")
                f.write(f"{startRentalFormat}, ")
                f.write(f"{carNum}, ")
                f.write(f"{rentTime}, ")
                f.write(f"{taxes},")
                f.write(f"{subTotal}, ")
                f.write(f"{totalCost}\n")
