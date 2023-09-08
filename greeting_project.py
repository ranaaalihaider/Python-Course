
print("Chart \n5am to 10am Good Morning \n11am to 3pm Good Noon \n4pm to 8pm Good Evening \n9pm to 4am Good Night")
#will Dsiplay chart
am_or_pm=int(input("Select 1 for AM and 2 for PM : "))
#getting value for am or pm from user 
if(am_or_pm<1 or am_or_pm>2):
    print("wrong command Restart Programmer")
    exit()
#checking value
t_input=str(input("What is time : "))
str1=t_input[0:2]
t_final=int(str1)
#getting time value and converting into two digits and converting into int from string
if(t_final>12 or t_final<1):
    print("Wrong Entry Restart programme 2")
    exit()
#exit due to wrong command
elif ( am_or_pm==1 ) and (t_final>=5 and t_final <=10 ):
    print("Good Morning")
elif (( am_or_pm==1 ) and (t_final>10)) or((am_or_pm==2) and(t_final>=1 and t_final<=4)):
    print("Good Noon")
elif(am_or_pm==2)and(t_final>=5 and t_final<=8):
    print("Good Evening")
elif(am_or_pm==2) and(t_final>=9 and t_final<=12):
    print("Good Night")
elif(am_or_pm==1) and (t_final>=1 and t_final<=4):
    print("Good Night")
#logics to display output




