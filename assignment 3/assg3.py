#Question 1

print("Question 1\n")
#taking input from user
sen = input("Please give an input- ")
sen=sen.lower().strip()
i=0
#defining empty dictionary to use later to store element, counter pairs and eliminating common letters and words
dict={}

#checking if the string input is a word or a sentence
if " " not in sen:
     #searching for common elements
     while i<len(sen):
          counter=0
          k=0
          while k<len(sen):
               if sen[i]==sen[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
          #storing the values in dictionary
          dict[f"{sen[i]}"]=counter
          i=i+1

else:
     #making a list of words using split method
     list = str.split(sen)
     #searching for common words
     while i<len(list):
          counter=0
          k=0
          while k<len(list):
               if list[i]==list[k]:
                    counter=counter+1
                    k=k+1
               else:
                    k=k+1
                    #storing the pairs in dictionary
          dict[f"{list[i]}"]=counter
          i=i+1
#Printing the final result
print("Total occurances")
for key,value in dict.items():
    print(f"{key}-{value}")

###################################################################################################

#Question 2

print("\nQuestion 2\n")
#Taking input from user
day=int(input('Please enter Day- '))
month=int(input('Please enter Month- '))
year=int(input('Please enter Year- '))


#Removing all the invalid cases
if day>30 and month in {2,4,6,9,11}:
    condition=False
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition=False
elif (day==29 or day==30) and month==2 and year%4!=0:
    condition=False
elif day==30 and month==2 and year%4==0:
    condition=False
else:
    condition=True
if month>12:
    condition=False


#After checking the condition, following if-else statement is executed
if condition:
    #checking and changing for new year
    if day==31 and month==12:
        n_year=year+1
    else:
        n_year=year
    if month==12 and day==31:
        n_month=1
    else:
        n_month=month

#changing dates
    #checking for months with 31 days
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            next_day=1
            if month!=12:
                n_month=month+1
            else:
                n_month=1
        else:
            next_day=day+1
    #checking for the month of february
    elif month==2:
        if year%4==0:
            if day==29:
                next_day=1
                n_month=3
            else:
                next_day=day+1
        else:
            if day==28:
                next_day=1
                n_month=3
            else:
                next_day=day+1

    #covering all the remaining cases
    else:
        if day==30:
            next_day=1
            n_month=month+1
        else:
            next_day=day+1
    #printing the calculations
    print(f"Next Date is: {next_day}/{n_month}/{n_year}\n")

else:
    #gives a warning and ends the program
    print("That's not a valid date")

###################################################################################################

#Question 3
print("Question 3\n")
list1 = eval(input("Enter the list of integers: "))
list2 = []
#(i, i**2) is the tuple which is added in the list, i.e. list_out is list of tuples
for i in list1:
    list2.append((i, i**2))                                                                              
print("Output:", list2)
################################################################################################

#Question 4

print("Question 4\n")
gpa=int(input('Enter Grade Points- '))

dict={10:{'grade':'A+','remarks':'Outstanding'},
           9:{'grade':'A','remarks':'Excellent'},
           8:{'grade':'B+','remarks':'Very Good'},
           7:{'grade':'B','remarks':'Good'},
           6:{'grade':'C+','remarks':'Average'},
           5:{'grade':'C','remarks':'Below Average'},
           4:{'grade':'D','remarks':'Poor'}}
if 3<gpa<11:
    for key in dict.keys():
        if key==gpa:
            value=dict[key]
            print(f"Your Grade is {value['grade']} and {value['remarks']} performance ")
        else:
            continue
else:
    print('Error!')
###################################################################################################

#Question 5
print("Question 5\n")
string = "ABCDEFGHIJK"
j = 0
while len(string) - j*2 >= 1:
    print(" "*j + string[0 : len(string) - j*2])
    j += 1
 
####################################################################################################

#Question 6

print("Question 6\n")
condition=True

#Defining dictionary to store the values
Dictionary={}
msg="y"
while condition:
    if msg.lower()=="y":
        SID=int(input("Please Enter SID of the Student- "))
        name=input("Please enter the name of the Student- ")
        Dictionary[SID]=name
        msg= input("If you want to enter more details press Y/N- ")
        condition = True

    else:
        condition = False

print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

print("Part b")
Val_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

print("Part c")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

print("Part D")
SID2=int(input("Please enter the student's SID whose detail you need- "))
if SID2 in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID2]}")
else:
    print("The SID is not present in the given Data")
print("")

#######################################################################################################

#Question 7

print("Question 7\n")
num=int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))

#using the formula of the sum of previous two terms is equal to the present term.
an1=1
an2=0
n=0
#initializing sum with first two terms
sum=an1+an2

#printing the initial two terms as the recursion is not valid on them
print(f"Fibonnaci sequence with {num} terms")
print(an2)
print(an1)

#Printing the remaining fibonnaci terms
while n<num-2:
    an=an2+an1
    an2=an1
    an1=an
    print(an)
    n=n+1
    sum+=an
average=sum/num
#printing the program end prompt
print(f"Average of total {num} terms of sequence is {average}")
print("END")

################################################################################################

#Question 8
print("Question 8\n")
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print("a. Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)
print("b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)
print("d. Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)
print("e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)
##########################################################################################################

