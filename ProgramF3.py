#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.

# create a function 

def YourMoney():
    fee = input("How much money do you have? ")
    return fee 

def ApplePrice():
    price = input("Enter the price of the apple: ")
    return price 

def QApple():
    TotalApples = int(money/apple)
    return TotalApples

def GetAmount():
    amount = int(money%apple)
    return amount

def Display(affordableQ, changeQ):
    print(f"You can buy {affordable} apples and your is {changeF} pesos.")

# call all the functions

money = YourMoney()
apple = ApplePrice()
affordable = QApple()
changeF = GetAmount()
Display(affordable, changeF)
