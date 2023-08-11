# Written by: SD 9 Robot Group 1 A.K.A Python Punishers
# Written on: 2023/08/07
# Description: Main menu for HAB Taxi Services.

# Imports:
import Modules.Stylizer as S
from Modules.Validizer import Validate as V
from Modules.Validizer import strip
from Options import choose

# Loads file to dictionary:
Defaults = {}
with open("Defaults.dat") as f:
    for i in f.read().split(", "):
        v = i.split(":")
        Defaults[v[0]] = V.number(v[1])[1]
print(S.rgb(204, 153, 255))

# Main loop:
while True:
    S.blank(20)
    S.Constraint = 58
    S.Padding = 4
    S.align("r13#:HAB Taxi Services")
    S.align("r13#:Company Services System")
    S.align("l:1.  Enter a New Employee (driver). ")
    S.align("l:2.  Enter Company Revenues. ")
    S.align("l:3.  Enter Company Expenses.")
    S.align("l:4.  Track Car Rentals. ")
    S.align("l:5.  Record Employee Payment. ")
    S.align("l:6.  Print Company Profit Listing. ")
    S.align("l:7.  Print Driver Financial Listing. ")
    S.align("l:8.  Your report –add description here ")
    S.align("l:9.  Quit Program.")
    print(S.display())
    Choice = V(V.number, S.align("r13#:Enter choice (1-9): ", fill=False, qd=True), "int", "0-9").V
    if Choice == 9:
        print("Quitting...")
        break
    if Choice != 0:
        d = choose(Choice, Defaults)
        Defaults = d.copy()
        comp = ""
        for i in Defaults:
            comp = f"{comp}, {i}:{Defaults[i]}"
        with open("Defaults.dat", "w") as f:
            f.write(comp[2:])
        input("Press enter to continue...")
    else:
        S.blank(20)
        S.Constraint = 60
        S.align("C:Looks like you found the super secret option ZeRo ;)")
        S.line()
        print(S.display())

        Color = V(V.rgb, S.align("R:Enter an rgb color (999,999,999): ", fill=False, qd=True)).V
        print(Color)
        print(S.rgb(*Color))
