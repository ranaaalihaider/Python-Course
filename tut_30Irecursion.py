number=5
def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number * factorial(number-1)
result=factorial(number)
print(result)
