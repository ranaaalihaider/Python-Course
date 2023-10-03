print("Following is list")
marks = [2, 4, 6,"item 4" , "item 5", 6.21]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print(marks[-3])
print(len(marks))
print(marks[6-3])
#now to check that following thing is present in list or not
if 6.21 in marks:
    print("YES")
else:
    print("No")
if 7 in marks:
    print("Yes")
else:
    print("No")
#we can do same thing for string 
stringexmple= "rana","ali","haider"
print(stringexmple)
if "ali" in stringexmple:
    print("Yes")
else:
    print("No")
print("Now we will print list items according to our desire")
print(marks[:])
print(marks[1:])
print(marks[2:4])
print(marks[4:])
print("FOLLOWING IS NEW LIST")
liexmp=[1,2,3,4,5,6,7,8,9,10]
print(liexmp)
print("Now we will use jump index to jump values")
print(liexmp[0:11:2])
print("As we can see it is printing to values on jump 2 after skiping 1 value")
print("Now we will make list by another method")
list2=[i for i in range (5)]
print(list2)
list2=[i*i for i in range (10)]
print(list2)
print("Now we will add condition in list")
list3=[i*i for i in range (10) if i%2==0]
print(list3)