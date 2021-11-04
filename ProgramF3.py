#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.

# create a function 

from ProgramF2 import OutPutF


def YourMoney():
    fee = input("How much money do you have? ")
    return fee 

def ApplePrice():
    price = input("Enter the price of the apple: ")
    return price 

def GetTotal():
    result = int(money // apple)
    return result

def GetAmount():
    amount = int(money % apple)
    return amount

def OutputF():
    print(f"You can buy {affordable} apples and your is {change}")

money = YourMoney()
apple = ApplePrice()
affordable = GetTotal()
change = GetAmount()
OutPutF()

