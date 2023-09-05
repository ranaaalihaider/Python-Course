#anything closed in "" or '' is convertd to sring automatically

Name = "Ali Haider"
Cast ='\"Ranaa\" '
print("Hello", Cast+Name)
print("Another Method of displaying Doble coats as output is closing string in single coats")
a='He said, "I am Tired"'
print(a)
print("Now we will print multiple lines as string")
spt='''Now we will print Multiple lines in single string
This is line no 1
This is line no 2
Now i will print these 4 lines'''
print(spt)
print("Its mean that we can print multipule string lines in single way by closing them in triple sinle inverted commas '''  string here ''' thats it")
print("By following method we can print letters seprately")
print(Name[0],Name[1])
print(Name[1])
print(Name[2])
print("By following method we can print seprate latters of long string by using for loop ")
for char in Name:
    print(char)
