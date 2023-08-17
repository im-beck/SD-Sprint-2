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
        Data = {}
        with open('Employees.dat') as f:
                for i in f:
                    line = i.split(", ")
                    EmpIDs.append(line[0])
                    for x, v in enumerate(line):
                        error, val = V.number(v)
                        if not error:
                            line[x] = val
                    Data[str(line[0])] = line[1:]
        EmpID = V(V.string, "Enter Driver Number: ", EmpIDs).V
        rentId = V(V.number, "What is the rental ID?: ").UP
        startRental = V(V.date, "Enter the start date of the rental (YYYY-MM-DD): ", "%Y-%m-%d", "string").V
        carNum = V(V.number, "Enter the Car Number (1-4): ", "int", "1-4").V
        rentTime = V(V.string, "Is the Rental for a day or a week? (D/W): ", "D,W").V
        if rentTime == "W":
                Week = 7
        elif rentTime == "D":
                dailyTime = Curr_Date.replace(hour=12, minute=0, second=0, microsecond=0)
                FormattedTime = dailyTime.strftime("%Y-%m-%d %H:%M")
        else:
                print("Error: Invalid entry, must provide D or W.")
        
        
        

            # Calculations

        Defaults = {}
        with open("Defaults.dat") as f:
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

        Data[EmpID][8] += totalCost
        FormattedTime = ""
        comp = ""
        for i in Data:
                if comp == "":
                    comp = i
                else:
                    comp = f"{comp}{i}"
                for x in Data[i]:
                    comp = f"{comp}, {x}"
                comp = f"{comp}\n"
                
        with open("Employees.dat", "w") as f:
                f.write(comp)



        # Add files for future reference.
                
        with open('Rentals.dat', 'a') as f:
                f.write(f"Rental ID:{rentId}, ")
                f.write(f"Employee ID: {EmpID}, ")
                f.write(f"Rental Start: {FormattedTime}, ")
                f.write(f"Car Number:{carNum}, ")
                f.write(f"Rent Duration:{rentTime}, ")
                f.write(f"Rental Cost:{f'${totalCost}'}, ")
                f.write(f"Taxes:{f'${taxes}'}, ")
                f.write(f"Total:{f'${totalCost}'}\n")

        Continue = input("Would you like to enter more rentals? (Y/N):").upper()

        if Continue == "Y":
                continue
        else:
                break


        