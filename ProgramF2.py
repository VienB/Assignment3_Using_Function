# Create a program that will ask how many apples and oranges you want to buy.
# Display th.e total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______

# make a function

def GetApple():
    AppleF = int(input("How many apple you want to buy? "))
    return AppleF
    
def GetOrange():
    OrangeF = int(input("How many apple you want to buy? "))
    return OrangeF

def Calculate():
    price = (apples * 20) + (oranges * 25)
    return price

def OutPutF(Fapple, Forange1, Fcal):
    print(f"The total amount is {cal}.")

#call all the functions

apples = GetApple()
oranges = GetOrange()
cal = Calculate()
OutPutF(apples, oranges, cal)

# short conclusion:
# I conclude that it is important to understand the logic of the program because one mistake can affect
# all the lines. But it is okay to make a mistake considering that it will give you a learnings and realization.