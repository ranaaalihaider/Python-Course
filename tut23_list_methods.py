list1=[1,82,45,6,55]
print(list1)
list1.append(7)
#it will add 7 in end of list
print(list1)
print("7 is added in end of list by use of a method called append")
#sort method will arrange list elements in an order 
#automatically it will show in assending order but if we reverse it will show in descending order
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
print("Following is list no 2 example")
#reverse will change order of list in reverse type
lis=[2,54,543,32,12,12,12,90,43,12]
print(lis)
lis.reverse()
print(lis)
lis.append(69)
print(lis)
#now we will count an element in list 
print(lis.count(12))
print("4 Number presents number of 4 in upper list is is done by count method")
#we can copy list in new list or variable by using .copy method
list4=[33,44,55,66,77,88,99]
print(list4)
#print("Now we will print list4 by use of copy function ")
m = list4.copy()
m[0]=0
print(m)
print("Now we will learn how to add something on speccific position in list")
li2=[0,3,5,7,9,12]
print(li2)
print("Now in the same list above we will add 899 on index position 3")
li2.insert(3,899)
#in insert function first value represents the number of index and 2nd represents the value to be replaced at that position
print(li2)
#we cna combine two lists by using extent method like following
ex1=[22,44,66,88,99]
print(ex1)
ex2=[333,444,555,666,777,888]
print(ex2)
ex1.extend(ex2)
print(ex1)
