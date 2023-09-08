year=int(input("Enter Year To Check Leap Year or Not : "))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("This is a leap year")
else:
    print("This is not a leap year")
'''This programme will check year is divided by 4 and reminder is zero and year is divided by 100 and reminder is not zero then
year is leap year
or it will check if year is divided by 400 than year will be leap year'''