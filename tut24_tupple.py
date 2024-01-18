#following two are examples of tuple 
tup= (1,4,6)
print(type(tup), tup)
cup= (2,7,9)
print(type(cup), cup)
#following type will show as int if we want it as tupple we will have to add a ","
tup= (6)
print(type(tup), tup)
cup= (9)
print(type(cup), cup)
#following will represent a tuple these are just like the int category but python dedected it as a tuple
#beacuse of addition of "," in the end 
tup= (6,)
print(type(tup), tup)
cup= (9,)
print(type(cup), cup)
''' difference in list and tupple is that the values given in a list can ve changed by use of finctions
but values giiven in a tuple can not be changed by use of any function
following i will change values in a list 
'''
print("This is s list on following")
liex=[12,34,65,78,998]
print(type(liex),liex)
print("Now we will change first value of list by use of function that can not be done in a tuple")
liex[0]=550
print(type(liex),liex)
#back to tuple
print("Now we are back to tuple \n i am going to print each valuee of tuple seprately just like list")
tuptx=(12,764,3432,5735,"Rana",True)
print(tuptx[0])
print(tuptx[1])
print(tuptx[2])
print(tuptx[3])
print(tuptx[4])
print(tuptx[5])
print(len(tuptx))
print(tuptx[-2])
#we can also we if else condition in tuple
if 5735 in tuptx:
    print("Yes 5735 is found in tuple uptx")
else:
    print("No 5735 is not present in tuple tuptx")
if 5755 in tuptx:
    print("Yes 5755 is found in tuple uptx")
else:
    print("No 5755 is not present in tuple tuptx")
print("We can also do slicing in tuple by following method ")
print("Tuple[start : end : jumpindex ]")
tup1=(12,23,43,54,56,76,87)
print(tup1)
print("Following it will print index number 2 and 4 by use of slicing")
tup2=tup1[2:4]
print(tup2)
tuple_text=(12,23,43,54,65,2,1,23,32,1,32)
print(tuple_text)
print(type(tuple_text))
list_tuple=list(tuple_text)
print(list_tuple)
tuple3=tuple(list_tuple)
print(tuple3)