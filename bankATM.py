import random

print("                                                                      Welcome To Natinol Bank")
print("Please Fill The All Inputs")
name=input("Your Bank User Name ? ")
acno=int(input("Enter Your Bank Account Number: "))
openBal=random.randint(0,100000)
currBal=openBal

def printMenu():
    print("Welcome,",name)
    print("")
    print("I'll be helping you through the whole experience of using ATM.")
    print("")
    print(name,"These are the commands to operate this ATM ,'B'(B To Checkout Balance),'D'(D For Deposit), 'W'(W for Withdrawl Money),'Q'(Q to quit the operation)")

def getTransaction():
    transaction=str(input("What would you like to do? "))
    return transaction

def withdraw(bal,amt):
    global b
    b=bal-amt
    if b<0:
        b=b-10

def formatCurrency(amt):
    return "$%.2f" %amt

printMenu()
command=str(getTransaction())

while command!="Q":
    if (command=="B"):
        print(name,"Your current balance is",formatCurrency(currBal))
        printMenu()
        command=str(getTransaction())
    elif (command=="D"):
        amount=float(input("Amount to deposit?: "))
        currBal=currBal+amount
        print("Current Balance After Depositing: ",currBal)
        printMenu()
        command=str(getTransaction())
    elif (command=="W"):
        amount=float(input("Amount to withdraw? "))
        if currBal>=amount: 
            currBal-=amount 
            print("\n You Withdraw:", amount)
            print("\n Your Currnent Balance:", currBal) 
        else: 
            print("\n Insufficient balance  ") 
  
        
        printMenu()
        command=str(getTransaction())
    else:
        print("Incorrect Command.")
        printMenu()
        command=str(getTransaction())

print(name,"Thank you For Coming")