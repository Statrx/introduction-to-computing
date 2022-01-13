#Question no-1:Average of 3 numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
print("The average of the three numbers is",(a+b+c)/3)

#Question 2:Income tax calculation
gross_income=float(input("Enter your total income:"))
dependent_members=int(input("Enter your non-earning family members:"))

taxable_income=float(gross_income-10000-dependent_members*3000)

income_tax=taxable_income/5

if income_tax<=0:
    print("You don't have to pay income tax.")

else:    
   print("Income tax to be paid is ", income_tax)


#Question 3:Storing different data
SID=int(input("Enter your SID-"))
name=input("Enter your name-")
gender=input("Enter your Gender-(M,F,U) -  ")
course=input("Enter the course name-")
CGPA=float(input("Enter the CGPA-"))

Student=[SID,name,gender,course,CGPA]

print(Student)

#Question 4: Sorting marks of students
SM1=float(input("Enter your marks(Student 1): "))
SM2=float(input("Enter your marks(Student 2): "))
SM3=float(input("Enter your marks(Student 3): "))
SM4=float(input("Enter your marks(Student 4): "))
SM5=float(input("Enter your marks(Student 5): "))

Marks=[SM1,SM2,SM3,SM4,SM5]
Marks.sort()
print(Marks)

#Question 5-1: Removing 4th element colour from list
colour=['Red','Green','White','Black','Pink','Yellow']
colour.remove('Black')
print(colour)

#Question 5-2: Replacing element in list
colour=['Red','Green','White','Black','Pink','Yellow']
colour[3:5]=["Purple"]
print(colour)
