#Create a program that will ask for name, age and address. 
#Display those details in the following format.
#Hi, my name is _____. I am ____ years old and I live in _____ .

# use a function

def YourName():
    Fname = input("Enter Your Name: ")
    return Fname

def YourAge():
    Fage = int(input("Enter Your Age: "))
    return Fage

def YourAdress():
    Fadd = input("Enter Your Name: ")
    return Fadd

def OutputF(name1, age1, add1):
    print(f"Hi, my name is {name1}. I am {age1} years old and I live in {add1}.")

# call all the functions
name = YourName()
age = YourAge()
address = YourAdress()

OutputF(name, age, address)