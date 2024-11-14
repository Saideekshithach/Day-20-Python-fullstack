#ATM APPLICATION
Account=10000
while True:
    pwd=1234
    card=input("Insert the card")
    if card=='c':
        print("welcome Deekshitha")
        password=int(input("enter the password"))
        if password==pwd:
            option=int(input('''choose the option:
                             1.Balance enquiry
                             2.withdraw'''))
            if option==1:
                print("Acount balance is",Account)
            elif option==2:
                withdraw=int(input("enter the amount:"))
                print(withdraw)
                balance=Account-withdraw
                Account=balance
                print("Remaining account balance is ",balance)
        else:
            print("Incorrect password")
    else:
        print("invalid card")

        
