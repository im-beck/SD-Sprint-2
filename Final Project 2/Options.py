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
    for i in range(0, 20):
        print()
    if num == 1:
        data = [d['DriverNum']]
        # Inputs and validations:
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

        # Outputs:
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
        print()
        with open("Employees.dat", "a") as f:
            comp = ""
            for i in data:
                comp = f"{comp}, {i}"
            f.write(f'\n{comp[2:]}')
        # Saves employee data to file ^
        loading_bar("Saving employee data...")
        # Redundant loading bar ^ so the user knows something happened.
    elif num == 6:
        while True:
            with open("Payments.dat", "r") as f:
                noLine = f.readline()
                if noLine == "":
                    PayID = 1
                else:
                    f.seek(0)
                    lines = f.readlines()
                    lastLine = lines[-1]
                    PayID = int(lastLine.split(",")[0]) + 1
            EmpIDs = []
            with open("Employees.dat", "r") as f:
                for data in f:
                    dataLine = data.split(",")
                    EmpIDs.append(dataLine[0].strip())
            while True:
                EmpID = input("Enter employee Number: ")
                if EmpID not in EmpIDs:
                    print("Employee number does not match our records. Please try again.")
                else:
                    break
            PayDate = V(V.date, "Enter the payment date (YYYY-MM-DD): ", "%Y-%m-%d", "string").V
            PayAmt = V(V.number, "Enter the payment amount: ", "$").UP
            PayReason = input("Please input reason for payment: ")
            PayMethod = V(V.string, "Enter the payment method: ", ["Visa", "Debit", "Cash"]).V

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
            with open("Payments.dat", "a") as f:
                f.write(f"{PayID}, ")
                f.write(f"{EmpID}, ")
                f.write(f"{PayDate}, ")
                f.write(f"{PayAmt}, ")
                f.write(f"{PayReason}, ")
                f.write(f"{PayMethod}\n")
            loading_bar("Saving Payment Record...")
            choice = input("Would you like to enter another record? (Y/N): ").upper()
            if choice == "Y":
                continue
            else:
                break
    
    elif num == 8:
        current_date = datetime.now().strftime("%Y-%m-%d")
        driver = "XXXXXXXXXXXXXXXXXXX"
        driver_num = "####"
        rating = "#/#"  # rating is out of 5
        review = "xxxxxxx..."
        # This is the driver rating table that will make it possible to track how employees are performing
        # for an exception report there would an if statement that if the drivers ratings are >= 3 then
        # they might need to be spoken to.
        S.Constraint = 65
        S.align("R:HAB TAXI SERVICES")
        S.align(f"R:Driver Ratings as of: {current_date}")
        S.line()
        S.align(".1:DRIVER", ".45:DRIVER", ".65:RATING", ".9:REVIEW")
        S.align(".1:NAME", ".45:NUMBER", ".65:(1-5)")
        S.line()
        for i in range(0, 8):
            S.align(f".1:{driver}", f".45:{driver_num}", f".65:{rating}", f".9:{review}")
        S.line()
        print(S.display())

        # This is the report for customer reviews, these would be inputted by drivers in order to keep track of
        # customers who may be a problem and refused service later on depending on their behaviour.

        cust_name = "XXXXXXXXXXXXXXXXX"
        cust_rating = "#/#"
        cust_review = "xxxxxx..."
        cust_phone = "123-123-1234"

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
    return d
