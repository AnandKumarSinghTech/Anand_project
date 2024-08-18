# String are immutable.
a = "Anand!!! kumar!!! Singh!!"
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("@")) # It will strip(remove) the given character.\
# It will not strip the aplphabet that is written before.
print(a.replace("!", "#"))
print(a.split(" "))
print(a.capitalize()) # It will do capital to the First character in upper case.
d = " introduction tO introduction caPatiLiZe"
print(d.capitalize())
print(len(d))
print(len(d.center(50)))
print(d.count("introduction")) # It vwill count no of "introduction" (string which we will write in print counted
print(a.endswith("!!")) 
print(a.startswith("Anand"))
print(a.endswith("!!!", 0, 8)) 
stt = "He's name is Ankit. He is a good boy."
print(stt.find("is"))
print(stt.find("iss")) #It's output will be -1 means not occur in this string.
print(stt.index("is")) 
str1 = "WelcomeTOTheConsole" # It will give you an output true if it is written only eith alphabet(a-z) and numeric(0-9) without space.
print(str1.isalnum())
dd = "Welcome00"
print(dd.isalnum()) 
#He has said that it will give you false but it is giving true.
print(d.islower())
# If it will be in lower case then it will give you true otherwise it will give you false.
sd0 = "HAPPY DIWALI"
print(sd0.upper())
sd = "Happy Diwali and Chhath"
print(sd.isprintable())
sd1 = "Happy Diwali and\n Chhath"
print(sd1)
print(sd1.isprintable())
# It will give you false because "/n" is doing is work but it is not printable.
print(sd1.isspace())
sd2 = "Happy              Diwali and   Chhath"
print(sd2.isspace())
# He has said that while using tabs or space from spacebar it will give you true but it is giving false.
sd3  ="Lovely Professional University"
print(sd3.istitle())
# It will give true if all the word's first letter is capital, and give false even one of the first's letter is in lower case. 
sd4 = "Lovely professional university"
print(sd4.istitle())
sd5 = "Lovely professional University"
print(sd5.istitle())
print(sd0.swapcase()) # It will change the cases like upper to lower and lower to upper.
sd6 = "Happy"
print(sd6.swapcase())
print(sd4.title())