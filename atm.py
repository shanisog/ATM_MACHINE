from datetime import datetime
actual_pin = None
inserted = False
Balance = 10000
attempt = 0
blocked = False
transactions = []
print("Welcome to SBI")

while True:
    if inserted == False:
        print("INSERT YOUR ATM CARD")
        ins = int(input("1 - for yes 2 - for no : "))
        if ins == 1:
            inserted = True
        else:
            continue
    if blocked == True:
        print("Your Card has been blocked, contact your Branch Manager to unblock")
        inserted = False
    if actual_pin == None:
        actual_pin = int(input("Set your 4 digit PIN : ")) # "1234" -> 1234
    if blocked == False:
        enter_pin = input("Enter Your PIN : ") # "1234"
    if len(enter_pin) == 4:
        if int(enter_pin) == actual_pin: #1234 == 1234
            # print("Select one of the options below ")
            print(""" 
                1. Deposit
                2. Withdrawal
                3. Check Balance / Account's Mini Statement
                4. Change PIN

    """)
        else:
            attempt += 1
            print("Invalid PIN, Try")
            if attempt>=2:
                blocked = True
            continue

    x = int(input("Select one of the options above : "))

    if x == 1:
        amount = int(input("Enter the amount : "))

        if amount % 100 == 0:
            print("Cash has been accepted")
            Balance = Balance + amount
            transactions.append(amount)
            print("Balance = ", Balance)
        else:
            print("Invalid Cash or feed multiples of 100")
            print("Balance = ", Balance)

    elif x == 2:
        amount = int(input("Enter the amount : "))

        if amount % 100 == 0:
            if amount < Balance:
                print("Take the Cash ")
                Balance = Balance - amount
                transactions.append(-amount)
                print("Balance = ", Balance)
            else:
                print("Insufficient Balance, \n Try again later")
        else:
            print("Invalid Cash or enter multiples of 100")
            print("Balance = ", Balance)

    if x == 3:

        datim = datetime.now()

        date = datim.strftime("%d-%m-%Y")

        time = datim.strftime("%H:%M")
        print(

            f"""
                            State Bank of India

            Time : {time}                               Date {date}

            Last Transactions """)

        for t in transactions:
            print(f"""                            {t}""")


        print(f"""

            Balance {Balance}
            
            
            """
        )

    if x == 4:
        actual_pin = int(input("Set New PIN"))

    cont = int(input("Do you want to continue 1- for yes and 2 for no : "))
    if cont == 1 :
        continue
    elif cont == 2:
        inserted = False        




