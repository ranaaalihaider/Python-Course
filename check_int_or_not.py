n1= input('enter number 1: ')
while(n1.isnumeric()==False):
    n1 = input('enter the number again: ')
n1 = int(n1)

n2 = input('enter the second number: ')
while(n2.isnumeric()==False):
    n2 = input('enter the number again: ')
n2 = int(n2)

print(f'the sum is : {n1+n2}')