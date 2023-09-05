'''Strings can not be changed these are immutable'''
a="Harry"
print(a)
print(len(a))
'''we can convert string but it will not change existing string it will make a new string like below i am making upper case and lower case'''
print(a.upper())
print(a.lower())
'''So by this method string is converted but new string is made to do that is actual original string is immutable'''
'''We can also remove additional characters from string by using rstrip'''
b="!! Ranaaa!!!!!"
print(b)
print("Now i will remove these !! from name by using rstrip method")
print("for this i have to specity letter to remove in small brackets of rstrip in code")
print("but it will only remove letter or symbol after name not before name")
print(b.rstrip("!"))
print("Now we will replace content of one string with other content")
d='DATA OF "d" TO BE REPLACED'
f="Python"
print(d)
print('Now following is replaced data of "d"')
print(d.replace("DATA","Replace Done"))
print(d.replace(d,f))
''''So in upper case point is d.replace is doing function to replace from d in next bracket
1st word or variable is that which is to be resplaced and 2nd is that with which it is to be replace it can be word or variabble
if it is word in 1st it will replace all matching word with wors in 2nd'''
print("Now we will study split")
print("This split method will split strings into a list after specific word or space that will be specified like below")
h="Now i will split this string in list after space every word below"
print(h.split(" "))
print("Now every word after i will be converted into list")
print(h.split("i"))
i="Testing 1"
k="Testing 2"
l=(i.replace(i,k))
m=(k.replace(k,i))
print(i)
print(k)
print(l)
print(m)