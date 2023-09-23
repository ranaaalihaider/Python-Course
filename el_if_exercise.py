apple=int(input("Enter Apple Price : "))
budget=int(input("Enter Your Budget : "))


balance = (budget-apple)
budget_limit = budget * (50/100)
if(balance >= budget_limit):
    print("You have enough money for other things")
elif(balance >1):
    print("you have little bit money more")
elif(balance==0):
    print("You have no more money")
else:
    print("you dont have enough money")

    