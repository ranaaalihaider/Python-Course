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
#to capitalize first letter of any string we can write variable name.capitaliza() this will capitalize the first letter of string
#it will automatically convert all next characters to lower case
blogheadinh="introduction to python"
print(blogheadinh.capitalize())
test="i Will TESt Capitalize FuNCTiOn In FolLowing PrInTs"
print(test)
print(test.capitalize())
cnt="Now we will learn centre method"
print(cnt.center(50))
print(len(cnt))
print(len(cnt.center(50)))
str1="Now i will count word Rana in this line so i am typing Rana two times"
print(str1)
print(str1.count("Rana"))
#By usung variable.endswith we can check either ouer string is ending with specific word or not
print(str1.endswith("times"))
#now we will again check that following string ends with same word or not
str2="Hey this is a python tutorail by youtube"
print(str2)
print(str2.endswith("youtube"))
str4="We can also specify range in a string from where we will start looking word that it irnds with specific word in this range or not"
print(str4)
str5="in the follwing value we will define that upper statement range of word from 20 to 26 ends with word range or not"
print(str5)
print(str4.endswith("range",0,25))
str6="We can also specify range"
str7="Following is the length of specified string in long string"
print(str7)
print(len(str6))
str8=("we can also location position of a word in a sting by use of a find function it will tell number on which the word is present on base of number this number can be used in endswith function also")
str9=("Following is an example of find function we will fiind number of word function in upper string")
print(str8)
print(str9)
print(str8.find("function"))
str10="As the upper responce show that function word is on 68 number now we will test it with endswith function"
print(str10)
print(str8.endswith("function",0,76))
str11="Now in this string word function 2 will be returned as falls due to wrong command in find function"
print(str11)
print(str11.find("asasas"))
str12="As we can see -1 is printed its mean that value is not found according to the command in find"
print(str12)
str13="Now we will study about index index will work like same as find but when value is not found insted of giving -1 value like find it will give error if value not found"
str14="Now we will find wrong word in str9 same like above true and error will be returened in following 2 prints "
print(str13)
print(str14)
print(str9.find("function"))
print(str9.index("function"))
#print(str9.index("functiomn"))
str15="In code section error command is commented"
print(str15)
str16="we use index if we are sure that value will be definately in string or program should exit after giving error"
print(str16)
str17="Now we will study about isalnum() function it will find that all the data in string is a number or alphabet if anything other is it will indicate"
print(str17)
str18="this2is2testing2string2for2isalnum2function9"
print(str18)
print(str18.isalnum())
str19="But point is isalnum function will indetify space as anyother character and it will false value"
print(str19)
str20="next isalpha function will give true value only if all the characters in string are alphabets not number like following"
print(str20)
str21="thisianexampleofisalpha"
print(str21)
print(str21.isalpha())
'''Now we will find out in str21 that all the text are in lowecase or not by use of function islower()'''
print(str21.islower())
''''Recalling concept of lower'''
print(str21.upper())
''''String change to upper case automaticcally'''
''''NOW WE WILL check is string printable or not
by use if function isprintable()
if anything like \n will be used it will return falls value'''
str22="checking printable function \n"
print(str22)
#str22="checking printable function \n"
print(str22.isprintable())
str23='Upper is returning false value because it has "\\n" in it'
print(str23)
str24="We can also check white space in string by use of isspace function like in following space string"
print(str24)
str25="         "
print(str25)
print(str25.isspace())
str26="Is title is used to check if first letter of every word in string in capitalized"
print(str26)
str27="This Is An Example"
print(str27)
print(str27.istitle())
str28="This Is A second Example"
print(str28)
print(str28.istitle())
'''False value is return because S of second is small so it can not be title'''
'''We can also check that our string starts with specific word or not by use of starts with'''
str29="computer science department SOFTWARE engineer"
print(str29.startswith('computer'))
'''Swapcase will change uppercase to lowercase and lowercase to upper case automatically'''
print(str29.swapcase())
'''Title function will convert automatically string to title'''
print(str29.title())
