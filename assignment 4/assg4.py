
# Question 1
print("\nQuestion 1\n")


def tower_of_hanoi(n, source="A", destination="B", temporary="C"):
    global counter
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}");
        counter = counter + 1
        return
    tower_of_hanoi(n - 1, source, temporary, destination)
    print(f"Move disk {n} from {source} to {temporary}");
    counter = counter + 1
    tower_of_hanoi(n - 1, temporary, source, destination)


inp = int(input("Please enter total number of disks- "))
counter = 0
tower_of_hanoi(inp, "A", "B", "C")
print(f"Total number of steps to be followed is {counter}")
#########################################################################################

# Question 2
print('\nQuestion 2\n')
n = int(input("Enter the number of rows for Pascal's Triangle: "))
# creating the pascal function and using recursion
print("Using recursions to create pascal's triangle: ")


def pascal(n, initial_n=n):
    if n == 0:
        return

    pascal(n-1, initial_n)
    print('  '*(initial_n-n), end='')
    a = 1
    for i in range(1, n+1):
        print(a, end='   ')
        a = a * (n - i) // i
    print()


pascal(n)

# Using loops to create pascal's triangle
print("Using loops to create pascal's triangle:")
for line in range(1, n+1):
    print('  '*(n - line), end='')
    b = 1
    for i in range(1, line+1):
        print(b, end='   ')
        b = b * (line - i) // i
    print()
##########################################################################################

# Question 3
print("\nQuestion 3\n")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# ensuring that denominator is not zero
while b == 0:
    b = int(input("Denominator cannot be zero. Please enter a non zero number : "))

Q, R = divmod(a, b)
m = [Q, R]


def division():
    Q, R = divmod(a, b)
    print(f"Quotient:{Q}\nRemainder:{R}")


division()

print('a)')
print(callable(division))

print('b)')
if all(divmod(a, b)):
    print('All the values are non zero')
else:
    print('All the values are not non zero')

print('c)')
m.extend([4, 5, 6])
print("After adding 4,5,6 : ", m)
filtered = filter(lambda n: n > 4, m)
print("Values greater than 4 are : ", list(filtered))

print('d)')
s = set(m)
print(s)

print('e)')
f_s = frozenset(s)
print("Immutable set : ", f_s)

print('f)')
m = max(f_s)
print(hash(str(m)))
####################################################################################################

# Question 4
print("\nQuestion 4\n")


class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid

    def __del__(self):
        print("Object destroyed")


# assigning values
student1 = Student("Sajjal Rana", 21105090)
print("Object is created")

# printing the assigned values
print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

# deleting object
del student1
####################################################################################################

#Question 5
print("\nQuestion-5\n")

class factory():                        # Creating a class names factory.

    def __init__(self,name,salary):     # Storing data of employees
        self.name = name
        self.salary = salary
        print(f"Object created named {self.name}.")

    def show_info(self):                # Data of employees
        print("\tShowing info of the employee.")
        print(f"Name of the employee working in this factory is {self.name}")
        print(f"Salary of {self.name} is {self.salary}.")

    def update_salary(self,new_salary): # Update the salary of employee
        self.salary = new_salary
        print(f"Updated salary of the employee {self.name} is {self.salary}\n")

    def __del__(self):                  # Deleting data of employee
        print(f"Record of the employee {self.name} is deleted.")
    
# Employees
Mehak = factory('Mehak', 40000)
Ashok = factory("Ashok", 50000)
Viren = factory('Viren', 60000)
print()

# DATA of employees
Mehak.show_info()
print()
Ashok.show_info()
print()
Viren.show_info()
print()

# Updating salary of employee
print("Updating mehak's salary.")
Mehak.update_salary(70000)

# Removing data of employee
print("Calling destructor to delete viren's record.")
del Viren

##########################################################################################################

# Question 6
print("\nQuestion 6\n")

def friendship(word1, word2):

    word1 = word1.lower()
    word2 = word2.lower()

    # checking whether all the letters are same in both words
    if sorted(word1) == sorted(word2):
        print("Your friendship is real")
    else:
        print("Your friendship is fake")

w1 = input("Friend 1, please enter your word : ")
w2 = input("Friend 2, please enter your word : ")


#verifying new word's meaningfulness from shopkeeper
a=input("Is the new word meaningful?(Y/N) : ")

if a.upper()=="N":
    print("Your friendship is fake.")
elif a.upper()=="Y":
    friendship(w1, w2)
else:
    ("Error!")
####################################################################################
