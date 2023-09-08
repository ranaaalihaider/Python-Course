print("Hello world")
'''Switch case verify differ options and match with commands'''
x=int(input("Enter Your Number More than 5 lower than 100 : "))
match x:
    case 0 :
        print("Your number is zero")
    case _ if x<5 :
        print("X is smaller than 5")
    case _ if x>100:
        print("Your Number is greater than 100")
    case _ :
        print(x)
'''We can also use if statement in case and default case'''
