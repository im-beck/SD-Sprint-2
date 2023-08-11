"""
f = open("Defaults.dat", "r")
NEXT_TRANS_NUM = f.readline()
DRIVER_NUM = int(f.readline())
MON_STAND_FEE = float(f.readline())
DAILY_RENTAL = float(f.readline())
WEEKLY_RENTAL = float(f.readline())
HST_RATE = float(f.readline())
f.close()

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
"""
import datetime
CurrDate = datetime.datetime.now()
Date = CurrDate.strftime("%Y-%m-%d")
Driver = "XXXXXXXXXXXXXXXXXXX"
DriverNum = "####"
Rating = "#/#" # rating is out of 5
Review = "xxxxxxx..."
# this is the driver rating table that will make it possible to track how employees are performing
# for an exception report there would an if statement that if the drivers ratings are >= 3 then
# they might need to be spoken to.
print()
print("HAB TAXI SERVICES")
print(f"Driver Ratings as of: {Date}")
print("-"*60)
print("    DRIVER           DRIVER         RATING         REVIEW")
print("     NAME            NUMBER          (1-5)")
print("-"*60)
print(f"{Driver}   {DriverNum}            {Rating}         {Review}")
print(f"{Driver}   {DriverNum}            {Rating}         {Review}")
print(f"{Driver}   {DriverNum}            {Rating}         {Review}")
print(f"{Driver}   {DriverNum}            {Rating}         {Review}")
print(f"{Driver}   {DriverNum}            {Rating}         {Review}")
print(f"{Driver}   {DriverNum}            {Rating}         {Review}")
print(f"{Driver}   {DriverNum}            {Rating}         {Review}")
print(f"{Driver}   {DriverNum}            {Rating}         {Review}")
print("-"*60)

# this is the report for customer reviews, these would be inputted by drivers in order to keep track of
# customers who may be a problem and refused service later on depending on their behaviour

CustName = "XXXXXXXXXXXXXXXXX"
CustRating = "#/#"
CustReview = "xxxxxx..."
CustPhone = "123-123-1234"

print()
print("HAB TAXI SERVICES")
print(f"Customer Ratings As Of: {Date}") # Formatter here lol
print("-"*61)
print("   CUSTOMER         CUSTOMER        CUSTOMER        PHONE")
print("    NAME             RATING          REVIEW         NUMBER")
print("-"*61)
print(f"{CustName}     {CustRating}           {CustReview}    {CustPhone}")
print(f"{CustName}     {CustRating}           {CustReview}    {CustPhone}")
print(f"{CustName}     {CustRating}           {CustReview}    {CustPhone}")
print(f"{CustName}     {CustRating}           {CustReview}    {CustPhone}")
print(f"{CustName}     {CustRating}           {CustReview}    {CustPhone}")
print(f"{CustName}     {CustRating}           {CustReview}    {CustPhone}")
print(f"{CustName}     {CustRating}           {CustReview}    {CustPhone}")
print(f"{CustName}     {CustRating}           {CustReview}    {CustPhone}")
print("-"*61)
