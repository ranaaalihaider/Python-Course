a=int(input("Enter Number 1 : "))
b=int(input("Enter Number 2 : "))
def sumfunction (a,b):
    print(a+b)
sumfunction(a,b)
""" AS IN ( ) next to sumfuntion we provided a and b but if we will provide default value it will ignore variables of
function and will use our given value Like fillowing"""
sumfunction(5,10)
'''So in output you will see that 15 will be printed that will take 5 and 10 to put in sumfunction'''
c=int(input("Enter Number to Divide: "))
d=int(input("Enter Number to Divide WIth: "))
def dividefunction (c,d):
    print(c/d)

dividefunction(c,d)