'''Now we will study continue and break'''
for i in range(16):
    if (i==10):
        continue
    print(i)
    '''It will skip 10'''
for i in range(16):
    if (i==10):
        break
    print(i)
    '''it will end before 10'''
'''Printing table by use of '''
t=int(input("Enter Number To Get Table : "))
for s in range(12):
    if(s==0):
        continue
    
    print(t,"*",s,"=",(t*s))
    s=s+1
    if(s==11):
        break
k=0
while True:
    print(k)
    k=k+1
    if(k==101):
        break


