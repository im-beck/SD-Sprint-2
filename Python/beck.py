f = open("Defaults.dat", "r")
NEXT_TRANS_NUM = f.readline()
DRIVER_NUM = int(f.readline())
MON_STAND_FEE = float(f.readline())
DAILY_RENTAL = float(f.readline())
WEEKLY_RENTAL = float(f.readline())
HST_RATE = float(f.readline())

DriverNum = DRIVER_NUM

DriverNum += 1

DriverName = input("Enter the employee's name: ")

DriverAdd = input("Enter the employee's address: ")

PhoneNum = input("Enter the employee's phone number: ")

LicenseNum = input("Enter the employee's license number: ")

LicenseExp = input("Enter the license's expiry date: ")

InsPolComp = input("Enter the employee's insurance policy company: ")

InsPolNum = input("Enter the employee's insurance policy number: ")

OwnCar = input("Does the employee have their own car (Y/N): ").upper()

if OwnCar == "Y":
    BalDue = MON_STAND_FEE + (MON_STAND_FEE * HST_RATE)
else:
    BalDue = (DAILY_RENTAL + WEEKLY_RENTAL) + (DAILY_RENTAL + WEEKLY_RENTAL * HST_RATE)

print("Driver number:", DriverNum)
print("Driver Name:", DriverName)
print("Driver's address:", DriverAdd)
print("License number:", LicenseNum)
print("License expiry date:", LicenseExp)
print("Employee's insurance policy company:", InsPolComp)
print("Employee's insurance policy number:", InsPolNum)
print("Using own car:", OwnCar)
print("Balance due:", BalDue)
