method=" "
n1=""
n2=''
def clc (method,n1,n2):
        method=str(input("Enter what you want to do +,-,/,* : "))
        
        if((method=="+") or (method=="-" ) or (method=="*" ) or (method=="/")):
                n1=int(input("Enter Number 1: "))
                n2=int(input("Enter Number 2: "))
                if(method =="+" ):
                        print(n1+n2)
                if(method =="-" ):
                        print(n1-n2)
                if(method =="/" ):
                        print(n1/n2)
                if(method =="*" ):
                        print(n1*n2)                         
        else:
                print("Wrong command")                
        



clc(method,n1,n2)

