'''t=10
while(t>0):
    name=str(input(("Enter Student Name: ")))
    phy=(input(("Enter Physics Number : ")))
    while(phy.count(".")>1):
        print("You have wrong entry")
        phy=(input(("Enter Physics Number : ")))
    while(phy.replace(".","").isdecimal()== False):
        print("Wrong command")
        phy=(input(("Enter Physics Number : ")))
    chem=(input(("Enter Chemistry Number : ")))
    while(chem.replace(".","").isdecimal()==False):
        print("Wrong command")
        chem=(input(("Enter Chemistry Number : ")))
    bio=(input(("Enter Biology Number : ")))
    while(bio.replace(".","").isdecimal()==False):
        print("Wrong command")
        bio=(input(("Enter Biology Number : ")))
    eng=(input(("Enter English Number : ")))
    while(eng.replace(".","").isdecimal()==False):
        print("Wrong command")
        eng=(input(("Enter English Number : ")))
    urdu=(input(("Enter Urdu Number : ")))
    while(urdu.replace(".","").isdecimal()==False):
        print("Wrong command")
        urdu=(input(("Enter Urdu Number : ")))
    math=(input(("Enter Math Number : ")))
    while(math.replace(".","").isdecimal()==False):
        print("Wrong command")
        math=(input(("Enter Math Number : ")))
    phy1=float(phy)
    chem1=float(chem)
    bio1=float(bio)
    eng1=float(eng)
    urdu1=float(urdu)
    math1=float(math)
    Total=phy1+chem1+bio1+eng1+urdu1+math1
    print(name, "Secured ", Total ,"Numbers in Total \nAs passing Percentage is above 60%")
    percentage=(Total/(600))*(100)
    grade=""
    if(percentage>=90):
        grade="With A Grade"
    elif(percentage>=80):
        grade="With B Grade"
    elif(percentage>=70):
        grade="With C Grade"
    elif(percentage<=60):
        grade="He is Fail"
    print("He Secured ", percentage, grade)
    '''
t=10
while(t>0):
    def erf (phy):
        if(phy=="exit"):
            exit()
        while(phy.count(".")>1 or phy.replace(".","").isdecimal()==False):
            print("Wrong command")
            phy=input("Enter Number Again : ")
        phy=float(phy)
        while(phy>100):
            print("Scores can not be greater than 100")
            phy=input("Enter Number Again : ")
            phy=float(phy)

    name=input("Enter Name Student Name: ")
    phy=input("Enter Physics Numbers: ")
    erf(phy)
    bio=input("Enter Biology Numbers: ")
    erf(bio)
    chem=input("Enter Chemistry Numbers: ")
    erf(chem)
    eng=input("Enter English Numbers: ")
    erf(eng)
    urdu=input("Enter Urdu Numbers: ")
    erf(urdu)
    phy=float(phy)
    bio=float(bio)
    chem=float(chem)
    eng=float(eng)
    urdu=float(urdu)

    total=float(phy+bio+chem+eng+urdu)
    percent=(total/500)*100
    grade=""
    if(total>=450):
        grade="A Grade"
    elif(total>=400):
        grade="B Grade"
    elif(total>=350):
        grade="C Grade"
    elif(total>=300):
        grade="D Grade"
    elif(total<300):
        grade="He is Fail"
    print(name,"Scored ",total ,"out of 600 with ",percent, "Percentage and ",grade )