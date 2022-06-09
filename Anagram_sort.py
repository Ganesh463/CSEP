string1=input("Enter the string1: ")
string2=input("Enter the string2: ")
str1=string1.lower()
str2=string2.lower()
if(len(str1)==len(str2)):
	if(sorted(str1)==sorted(str2)):
		print(string1 +" and " + string2 +" are anagrams")
	else:
		print(string1 +" and " + string2 +" are not anagrams")
else:
	print(string1 +" and " + string2 +" are not anagrams")
