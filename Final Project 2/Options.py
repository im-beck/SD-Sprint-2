# Written by: SD 9 Robot Group 1 A.K.A Python Punishers
# Written on: 2023/08/06-
# Description: Has all the options for HAB taxi services.

# Imports
import Modules.Stylizer as S
from Modules.Validizer import Validate as V
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
    else:
        print(num, "is not implemented.")
    return d
