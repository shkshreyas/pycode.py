yr=int(input("Enter year: "))
if (yr%400==0) or (yr%100!=0 and yr%4==0):
    print(f"{yr} is a leap year")
else:
    print(f"{yr} is not a leap year")