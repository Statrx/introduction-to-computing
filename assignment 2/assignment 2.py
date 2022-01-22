# Question 1
print("Question 1") 

#giving value to input string

a='Python is a case sensitive language'

# (a) Length of string
print("\nPart a")
print(len(a))

# (b) Reversing a string
print("\nPart b")
print(a[len(a)::-1])

# (c) slicing
print("\nPart c")
b=a[10:26]
print(b)

# (d) replacing
print("\nPart d")
print(a.replace("a case sensitive", "object oriented"))

# (e) index of substring "a"
print("\nPart e")
print(a.index('a'))

# (f) removing white spaces
print("\nPart f")
print(a.replace(" ", ""))

#################################

#Question 2
print('\nQuestion 2')
Name=str(input("Enter your name: "))
SID=int(input("Enter your SID: "))
Department=str(input("Enter your Department: "))
CGPA=float(input("Enter your CGPA: "))
print('''Hey, %s here!
My SID is %d
I am from %s department and my CGPA is %f'''%(Name,SID,Department,CGPA))

#################################

#Question 3
print("\nQuestion 3")

a = 56
b = 10

print(" a&b : ", a & b) #And operator
print(" a|b : ", a | b) #Or operator
print(" a^b : ", a ^ b) #Xor operator

# Left shift both a and b with 2 bits.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)
# Right shift a with 2 bits and b with 4 bits.
print("a>>2 : ", a >> 2, "\tb>>2 :", b >> 4)

####################################

#Question 4
print("\nQuestion 4")
x=float(input("Enter first number: "))
y=float(input("Enter second number: "))
z=float(input("Enter third number: "))
if (x>y and y>z):
    print("The greatest number is:",x)
elif(y>z):
    print("The greatest number is:",y)
else:
    print("The greatest number is:",z)

#####################################

#Question 5
print("\nQuestion 5")
sen = str(input("Write a sentence: "))
if ('name' in sen):
    print("Yes")
else:
    print("No")

######################################

#Question 6
print("\nQuestion 6")
s1= int(input("Enter the length of first side of triangle: "))
s2= int(input("Enter the length of second side of triangle: "))
s3= int(input("Enter the length of third side of triangle: "))
if (s1+s2>s3 and s2+s3>s1 and s3+s1>s2):
    print("Yes")
else:
    print("No") 

