x=0

while(x<10):
    print("Types exit anytime to end programme \n")
    a=str(input("Enter Theoretical Value : "))
    if(a==("exit")):
        break
    while a.replace(".","").isdigit() == False:
        print("Wrong Command")
        a=str(input("Enter Theoretical Value : "))
    b=str(input("Enter Actual Value Value : "))
    if( b==("exit")):
        break
    while b.replace(".","").isdigit()== False :
        print("Wrong Command ")
        b=str(input("Enter Actual Value Value : "))
    c=float(a)
    d=float(b)
    r= (((d-c)/c)*100)
    print("Percentage Error is : ",r ,"\n")
    
'''x = 0

while x < 10:
    a = str(input("Enter Theoretical Value (or 'exit' to quit): "))
    if a == "exit":
        break  # Exit the loop if 'exit' is entered
    b = str(input("Enter Actual Value Value (or 'exit' to quit): "))
    if b == "exit":
        break  # Exit the loop if 'exit' is entered

    # Convert the input values to floats
    c = float(a)
    d = float(b)

    # Calculate and print the percentage error
    r = (((d - c) / c) * 100)
    print("Percentage Error is:", r)'''
