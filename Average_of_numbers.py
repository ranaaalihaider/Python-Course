
def average (*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    #print("Average is :", sum/len(numbers))
    return sum/len(numbers)
'''So by adding return return will take this value and will end this loop or function whatever is'''
'''Return function is used to return value to calling function'''
average(5,6,7)
c= average(12,4,12,55,1)
print(c)
'''Sonnit is taking numbers as a tuple class'''
'''So in this code *numbers is a tuple it will use all the numbers and will sum them by sum function 
and will divide them by lenth of number function and will give value to return functio that will be stored in calling
function which is c in this case and it will print values of average wehn we will print c'''
