print("Check Your Bmi Here")

weight=float(input("Enter your weight in kg : "))
print("Select Height Unit to Enter Press 1 for Feet Press 2 For Meters")
unit=float(input())
if(unit==1):
    height_feet=float(input("Enter your Height In Feet : "))
elif(unit==2):
    height_meter=float(input("Enter your Height In Meters : "))
else:
    print("Wrong Command Restart Programme")
    exit()
if(unit==1):
    final_height=((height_feet)/(3.28084))
elif(unit==2):
    final_height=height_meter


bmi=weight/(final_height*final_height)
print("Your BMI is %.2f"%(bmi))
if(bmi<18.5):
    print("You are underweight")
elif(bmi>=18.5 and bmi<24.9):
    print("Normal Weight")
elif(bmi>24.9 and bmi<29.99):
    print("You are Over Weight")
elif(bmi>29.99):
    print("You are obese")
