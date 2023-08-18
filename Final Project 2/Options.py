# Written by: SD 9 Robot Group 1 A.K.A Python Punishers
# Written on: 2023/08/06-
# Description: Has all the options for HAB taxi services.

# Imports
import Modules.Stylizer as S
from Modules.Validizer import Validate as V
from datetime import datetime
from tqdm import tqdm
from time import sleep

ES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-,.'1234567890 "
# Extended set, for addresses and such. If a string is passed through as an additional argument on Validate.name
# it's converted to a set, if a set is passed through nothing happens.


def loading_bar(name):
    for i in tqdm(range(0, 100), desc=name):
        sleep(.01)
# Does loading bar with name since we may need it multiple times.


# Options:
def choose(num, d):
    pc = True
    for i in range(0, 20):
        print()
    if num == 1:
        # Inputs and validations:
        data = [d['DriverNum']]
        driver_name = V(V.name, "Enter the employee's name: ").V
        data.append(driver_name)
        # ^ adds to data list for saving later.
        driver_address = V(V.name, "Enter the employee's address: ", ES).V
        data.append(driver_address)
        driver_phone = V(V.phone_number, "Enter the employee's phone number: ").V
        data.append(driver_phone)
        licence_num = V(V.licence_plate, "Enter the employee's license number: ", "X999999999").V
        # Licence plate validation can also format any kind of string of numbers and letters.
        data.append(licence_num)
        licence_exp = V(V.date, "Enter the license's expiry date: ", "%y/%m", "string").V
        data.append(licence_exp)
        insurance_company = V(V.name, "Enter the employee's insurance policy company: ", ES).V
        data.append(insurance_company)
        insurance_num = V(V.number, "Enter the employee's insurance policy number: ").UP
        # .UP for Unprocessed since an insurance number may start with a 0. ^
        data.append(insurance_num)
        own_car = V(V.string, "Does the employee have their own car (Y/N): ", "Y,N").V
        data.append(own_car)

        # Calculations:
        d["DriverNum"] += 1
        if own_car == "Y":
            balance_due = d["MonthlyStandFee"] + (d["MonthlyStandFee"] * d["HST"])
        else:
            balance_due = (d["DailyRentalFee"] + d["WeeklyRentalFee"]) + \
                          (d["DailyRentalFee"] + d["WeeklyRentalFee"] * d["HST"])
        data.append(balance_due)

        # Output:
        S.Constraint = 60
        S.blank(20)
        S.line()
        # 0 is left, 1 is right.
        S.align("0:Employee: ", f"1:{data[0]}-{driver_name}")
        S.align("0:Address:", f"1:{driver_address}")
        S.align("0:Phone number:", f"1:{driver_phone}")
        S.line()
        S.align("0:Licence: ", f"1:Number: {licence_num} Expiry: {licence_exp}")
        S.align("0:Insurance: ", f"1:{insurance_company}-{insurance_num}")
        S.align(f"0:Using own car: {own_car}", f"1:Balance due: {balance_due}")
        S.line()
        print(S.display())
        # Above displays the entered information into an easy to read block so that the user
        # can double check the input fields.

        # Saving:
        print()
        with open("Employees.dat", "a") as f:
            comp = ""
            for i in data:
                comp = f"{comp}, {i}"
            f.write(f'\n{comp[2:]}')
        # Saves employee data to file ^
        loading_bar("Saving employee data...")
        # Redundant loading bar ^ so the user knows something happened.
    elif num == 4:
        while True:
            EmpIDs = []
            Data = {}
            Defaults = {}
            with open("Defaults.dat") as f:
                for i in f.read().split(", "):
                    v = i.split(":")
                    Defaults[v[0]] = V.number(v[1])[1]
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
            startRental = V(V.date, "Enter the start date of the rental (YYYY-MM-DD): ", "%Y/%m/%d", "string").V
            carNum = V(V.number, "Enter the Car Number (1-4): ", "int", "1-4").V
            rentTime = V(V.string, "Is the Rental for a day or a week? (D/W): ", "D,W").V

            # Calculations
            totalCost, Subtotal, HST = 0, 0, 0
            if rentTime == "W":
                Subtotal = Defaults["WeeklyRentalFee"]
                HST = (Defaults["WeeklyRentalFee"] * Defaults["HST"])
                totalCost = Defaults["WeeklyRentalFee"] + HST
            elif rentTime == "D":
                Subtotal = Defaults["DailyRentalFee"]
                HST = (Defaults["DailyRentalFee"] * Defaults["HST"])
                totalCost = Defaults["DailyRentalFee"] + HST

            Data[EmpID][8] += totalCost
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
                f.write(f"Employee ID:{EmpID}, ")
                f.write(f"Rental Start:{startRental}, ")
                f.write(f"Car Number:{carNum}, ")
                f.write(f"Rent Duration:{rentTime}, ")
                f.write(f"Rental Cost:{Subtotal}, ")
                f.write(f"Taxes:{HST}, ")
                f.write(f"Total:{totalCost}\n")
            S.Constraint = 35
            S.blank(20)
            S.Border = True
            S.align("C:HAB Taxi Services")
            S.line()
            S.align("0:Employee ID:", f"1:{EmpID}")
            S.align("0:Rental ID:", f"1:{rentId}")
            S.line()
            S.align("0:Rental Start:", f"1:{startRental}")
            S.align("0:Rental Duration:", f"1:{rentTime}")
            S.align("0:Car Number:", f"1:{carNum}")
            S.line()
            S.align("0:Subtotal:", f"1:${Subtotal:.2f}")
            S.align("0:HST:", f"1:${HST:.2f}")
            S.align("0:Total:", f"1:${totalCost:.2f}")
            print(S.display())
            S.Border = False
            loading_bar("Saving rental...")
            if V(V.string, "Would you like to enter more rentals? (Y/N): ", "Y,N").V == "N":
                pc = False
                break
    elif num == 5:
        while True:
            # Inputs:
            with open("Payments.dat", "r") as f:
                PayID = 1
                for i in f.read().split("\n"):
                    if ", " in i:
                        v = V.number(i.split(", ")[0])
                        if not v[0]:
                            PayID = v[1] + 1
            EmpIDs = []
            with open("Employees.dat", "r") as f:
                for data in f:
                    dataLine = data.split(",")
                    EmpIDs.append(dataLine[0].strip())
            EmpID = V(V.string, "Enter employee number: ", EmpIDs).V
            PayDate = V(V.date, "Enter the payment date (YYYY-MM-DD): ", "%Y-%m-%d", "string").V
            PayAmt = V(V.number, "Enter the payment amount: ", "$").UP
            PayReason = input("Please input reason for payment: ")
            if PayReason.replace(" ", "") == "":
                PayReason = "No reason given"
            PayMethod = V(V.string, "Enter the payment method: ", ["Visa", "Debit", "Cash"]).V

            # Output:
            S.Constraint = 75
            S.blank(30)
            S.line()
            S.align(f"0:Payment ID: ", f"1:{PayID}")
            S.align(f"0:Employee Number: ", f"1:{EmpID}")
            S.align(f"0:Payment Date: ", f"1:{PayDate}")
            S.align(f"0:Payment Amount: ", f"1:${PayAmt}")
            S.align(f"0:Payment Reason: ", f"1:{PayReason}")
            S.align(f"0:Payment Method: ", f"1:{PayMethod}")
            S.line()
            print(S.display())

            # Saving:
            with open("Payments.dat", "a") as f:
                f.write(f"{PayID}, ")
                f.write(f"{EmpID}, ")
                f.write(f"{PayDate}, ")
                f.write(f"{PayAmt}, ")
                f.write(f"{PayReason}, ")
                f.write(f"{PayMethod}\n")
            loading_bar("Saving Payment Record...")
            if V(V.string, "Would you like to enter another record? (Y/N): ", "Y,N").V == "N":
                pc = False
                break
    elif num == 6:
        while True:
            startDate = V(V.date, "Please enter the start date (YYYY-MM-DD): ", "%Y-%m-%d", "string").V
            endDate = V(V.date, "Please enter the end date (YYYY-MM-DD): ", "%Y-%m-%d", "string").V
            revTotal = 0
            expTotal = 0
            S.Constraint = 65
            S.blank(20)
            S.align("R:HAB Taxi Services")
            S.align(f"R:Profit listing between {startDate} and {endDate}")
            S.line("=")
            S.align("R:Revenues: ")
            S.blank()
            S.align(".1:TRANSACTION", ".45:DRIVER", ".65:TRANSACTION", ".9:TOTAL")
            S.align(".1:NUMBER", ".45:NUMBER", ".65:DATE", ".9:REVENUE")
            with open("Revenue.dat", "r") as f:
                for lines in f:
                    data = lines.split(", ")
                    revDate = datetime.strptime(data[1], "%Y-%m-%d")
                    if datetime.strptime(startDate, "%Y-%m-%d") <= revDate <= datetime.strptime(endDate, "%Y-%m-%d"):
                        revTotal += float(data[6].strip())
                        S.align(f".1:{data[0]}", f".45:{data[3]}", f".65:{data[1]}",
                                f".9:${float(data[6]):.2f}")
            S.line("=")
            S.align(f"r3#:GRAND TOTAL:", f".9:${revTotal:.2f}")
            S.line("=")
            S.blank()
            S.line("=")
            S.align("R:Expenses:")
            S.blank()
            S.align(".1:INVOICE", ".45:DRIVER", ".65:INVOICE", ".9:TOTAL")
            S.align(".1:NUMBER", ".45:NUMBER", ".65:DATE", ".9:EXPENSE")
            with open("Expenses.dat", "r") as f:
                for lines in f:
                    data = lines.split(", ")
                    expDate = datetime.strptime(data[1], "%Y-%m-%d")
                    if datetime.strptime(startDate, "%Y-%m-%d") <= expDate <= datetime.strptime(endDate, "%Y-%m-%d"):
                        expTotal += float(data[7])
                        S.align(f".1:{data[0]}", f".45:{data[2]}", f".65:{data[1]}",
                                f".9:${float(data[7]):.2f}")
            S.line("=")
            S.align("r3#:GRAND TOTAL:", f".9:${expTotal:.2f}")
            S.line("=")
            profit = revTotal - expTotal
            S.align("r3#:PROFIT:", f".9:${profit:.2f}")
            S.line("=")
            S.blank()
            print(S.display())

            if V(V.string, "Would you like to print another profit listing? (Y/N): ", "Y,N").V == "N":
                pc = False
                break
    elif num == 8:
        current_date = datetime.now().strftime("%Y-%m-%d")
        # This is the report for customer reviews, these would be inputted by drivers in order to keep track of
        # customers who may be a problem and refused service later on depending on their behaviour.
        S.blank()
        S.align("0:HAB TAXI SERVICES")
        S.align(f"0:Customer Ratings As Of: {current_date}")  # Formatter here lol
        S.line()
        S.align(".1:CUSTOMER", ".45:CUSTOMER", ".65:CUSTOMER", ".9:PHONE")
        S.align(".1:NAME", ".45:RATING", ".65:REVIEW", ".9:NUMBER")
        S.line()
        customers = ["End"]
        with open("Customer.dat") as f:
            for i in f.read().split("\n"):
                i = i.split(", ")
                customers.append(f"{i[0]}-{i[1]}")
                S.align(f".1:{i[0]}", f".45:{i[1]}", f".65:{i[2][:15]}...", f".9:{i[3]}")
        S.line()
        print(S.display())
        print()
        input_string = S.align("R:Type a name to get full review (type 'End' to exit):", fill=False, qd=True)
        while True:
            S.Constraint = 90
            search = V(V.string, input_string, customers, True).V
            if search == "End":
                pc = False
                break
            else:
                S.line()
                with open("Customer.dat") as f:
                    for i in f.read().split("\n"):
                        i = i.split(", ")
                        if i[0] == search.split("-")[0] and i[1] == search.split("-")[1]:
                            S.align(f"0.5:{i[0]}-{i[1]}: {i[2]}")
                S.line()
                print(S.display())
                S.blank()
    else:
        print(num, "is not implemented.")
    return d, pc


