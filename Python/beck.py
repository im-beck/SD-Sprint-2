import datetime
import textwrap
CurrDate = datetime.datetime.now()
Date = CurrDate.strftime("%Y-%m-%d")
# this is the report for customer reviews, these would be inputted by drivers in order to keep track of
# customers who may be a problem and refused service later on depending on their behaviour
print()
print("HAB TAXI SERVICES")
print(f"Customer Ratings As Of: {Date}") # Formatter here lol
print("-"*61)
print("   CUSTOMER         CUSTOMER        CUSTOMER        PHONE")
print("    NAME             RATING          REVIEW         NUMBER")
print("-"*61)

f = open("Customer.dat", "r")
for CustomerLine in f:

    CustLine = CustomerLine.split(",")

    CustName = CustLine[0].strip()
    CustRating = CustLine[1].strip()
    CustReview = textwrap.shorten(CustLine[2].strip(), width=20)
    CustPhone = CustLine[3]

    print(f"{CustName}     {CustRating}           {CustReview}    {CustPhone}")

f.close()

print("-"*61)