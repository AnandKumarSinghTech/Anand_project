def database():
    global amount
    global pin
    amount=6000
    pin=2715

def start():
    password=int(input("enter your pin"))
    if pin==password:
        choice=int(input("Press 1 for checkbalance \n"
        "Press 2 for changepassword \n"
        "Press 3 for withdraw \n"
        "Press 4 for credit_amt \n"
        "Press 5 to exit"))
        if choice==1:
            checkbalance()
        elif choice==2:
            changepassword()
        elif choice==3:
            withdrawl()
        elif choice==4:
            credit()
        else:
            print("Thank You Visit again")
    else:
        print("Wrong Password")

def checkbalance():
    print("Your current balance is",amount)
    start()
def changepassword():
    global pin
    password=int(input("Enter Your Old pin"))
    if password==pin:
        newpin=int(input("Set your new pin"))
        pin=newpin
        start()
    else:
        print("old pin is incorrect")
    changepassword()
def credit():
    global amount
    credit_amt=int(input("Enter the amount you want to credit"))
    amount+=credit_amt
    checkbalance()
def withdrawl():
    withdrawal_amt=int(input("Enter the amount you want to withdraw"))
    global amount
    if withdrawal_amt>amount:
        print("inffulicent balance")
    else:
        amount-=withdrawal_amt
        checkbalance()
database()
start()
