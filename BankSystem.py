# This work done by group 11:
# Faris Alghamdi, 201920230, (50%)
# Khalid Alahmari, 201857680, (50%)


# We need to import a method from time library to make the program sleep for few seconds:
import time
# We also need to import a method from "IPython.display" library to clear the output (optional):
from IPython.display import clear_output
# We also need to read the date and time, for this purpose, we will use datatime module:
import datetime


def create():
    # This function create a bank account for a new user.

    # We first clear the output:
    clear_output()

    outFile = open("cardNumber.txt", "w")
    # We should open a file for writing the user's account information.

    cardNumber = input("Enter your card number (4 digits): ")

    # Now we have to check the validity of this card number.
    # We will use "sets" to check if the digits are unique or not.
    setOfDigits = set(number for number in cardNumber)
    while not cardNumber.isdigit() or len(setOfDigits) != 4:
        print("Card number must contain 4 unique digits.")
        cardNumber = input("Enter a card number (4 digits): ")
        setOfDigits = set(number for number in cardNumber)
    # After this point, we are sure that the card number is valid.

    outFile.write(cardNumber+"\n")
    # We put "\n" so that each line contain only one piece of information.

    pin = input("Enter a PIN code (4 digits): ")

    # Now we have to check the validity of this PIN number, same method applied as in card number.
    setOfDigits = set(number for number in pin)
    while not pin.isdigit() or len(setOfDigits) != 4:
        print("PIN code must contain 4 unique digits.")
        pin = input("Enter a PIN code (4 digits): ")
        setOfDigits = set(number for number in pin)
    # After this point, we are sure that the PIN number is valid.

    outFile.write(pin+"\n")

    email = input("Enter your KFUPM Email: ")
    # Now we have to check the validity of this Email. g201920230@kfupm.edu.sa

    # Lets put some varibles:
    long = len(email)
    ifStart = email.startswith("g20")
    ifEnd = email.endswith("@kfupm.edu.sa")

    # We also need to make sure that all X in "g20XXXXXXX" are digits:
    ifNumber = False
    if long == 23:
        # We put this condition to avoid "Out Of Range" error.

        for X in range(3, 10):
            if not email[X].isdigit():
                ifNumber = False
                break
            else:
                ifNumber = True

    # This is the test proccesing:
    while long != 23 or not ifStart or not ifEnd or not ifNumber:
        print("Invalid Email, try again.")
        email = input("Enter your KFUPM Email: ")
        long = len(email)
        ifStart = email.startswith("g20")
        ifEnd = email.endswith("@kfupm.edu.sa")
        ifNumber = False
        if long == 23:
            for X in range(3, 10):
                if not email[X].isdigit():
                    ifNumber = False
                    break
                else:
                    ifNumber = True
    # After this point, we are sure that the Email is valid.

    outFile.write(email+"\n")

    extra = input(
        "add at least one service for the new account (separated by commas): ")
    outFile.write(extra+"\n")

    # Initializing an amount for the account:
    outFile.write("0"+"\n")

    outFile.close()
    # We have to close the file to save the account's information.

    # Now lets make the program sleep for few seconds, showing a massage after clearing the output:
    clear_output()
    print("Please wait..")
    time.sleep(4)

    # After we finished sign up process, we move into login gate:
    clear_output()
    login()


def login():
    # This function asks the user for his saved information to access his account.

    # We first clear the output:
    clear_output()

    inFile = open("cardNumber.txt", "r")
    # First we should open the file that contain his information to check if the input is correct or not.

    cardNumber = input("Enter your card number: ")
    line1 = inFile.readline().rstrip()
    # We used "rstrip()" method to remove the "\n" character from the card number.

    while cardNumber != line1:
        print("Wrong card number, try again.")
        cardNumber = input("Enter your card number: ")
    # After this point, we are sure that the card number is correct.

    # Same process for PIN number:
    pin = input("Enter your PIN code: ")
    line2 = inFile.readline().rstrip()
    while pin != line2:
        print("Wrong PIN code, try again.")
        pin = input("Enter your PIN code: ")

    inFile.close()

    showMenu()


def showMenu():
    # This fuction just show the 7 features in a menu:
    clear_output()

    print("Bank Account Program")
    print("="*30)
    print("1. ", "Show account information")
    print("2. ", "Change PIN number")
    print("3. ", "Withdraw amount of money")
    print("4. ", "Deposit amount of money")
    print("5. ", "Pay bills")
    print("6. ", "View the last transactions")
    print("7. ", "Terminate a program")
    print("="*30)


def show(file):
    # This function show the account details:

    # We have to open the file:
    inFile = open(file, "r")

    # We will read each line and print it:
    line1 = inFile.readline().rstrip()
    print("%-20s %s" % ("Card number:", line1))
    line2 = inFile.readline().rstrip()
    print("%-20s %s" % ("PIN code:", line2))
    line3 = inFile.readline().rstrip()
    print("%-20s %s" % ("Email:", line3))
    line4 = inFile.readline().rstrip()
    print("%-20s %s" % ("Extra services:", line4))
    line5 = inFile.readline().rstrip()
    print("%-20s %s" % ("The balance:", line5))
    inFile.close()

    time.sleep(12)
    # this list will appear for 12 seconds

    showMenu()


def changePINFun(file):
    # This function changes the PIN code and replaces it by new one:

    # First we open the file to read and copy the information:
    inFile = open(file, "r")

    lines = inFile.readlines()
    # Decomposing the file to lines, every line is an element in list

    # Now we will first make like a login before changing the PIN code:
    cardNumber = input("Enter your card number: ")
    while cardNumber != lines[0].rstrip():
        print("Wrong card number, try again.")
        cardNumber = input("Enter your card number: ")
    # After this point, we are sure that the user entered his card number correctly.

    currentPIN = input("Enter your current PIN code: ")
    while currentPIN != lines[1].rstrip():
        print("Wrong PIN code, try again.")
        currentPIN = input("Enter your current PIN code: ")
    # After this point, we are sure that the user entered his current PIN code correctly.

    # No need to read the file, we will close it:
    inFile.close()

    # Now we will read user new PIN code and check if it is valid:
    newPin = input("Enter your new PIN code (4 digits): ")
    setOfDigits = set(number for number in newPin)
    while not newPin.isdigit() or len(setOfDigits) != 4:
        print("PIN code must contain 4 unique digits.")
        newPin = input("Enter your new PIN code (4 digits): ")
        setOfDigits = []
        for number in newPin:
            setOfDigits.append(number)
        setOfDigits = set(setOfDigits)
    # After this point, we are sure that the new PIN number is valid.

    # Now let's change the PIN code:
    lines[1] = newPin

    # Now we have to update his information:
    outFile = open(file, "w")
    for line in lines:
        outFile.write(line.rstrip()+"\n")
        # We put .rstrip()+"\n" to ensure that each line has 1 "\n" chracter
    outFile.close()

    # Now the program will sleep for few seconds:
    clear_output()
    print("Changed successfully. returning to menu..")
    time.sleep(4)

    showMenu()


def withdrawFun(file):
    # This fuction allows the user to withdraw some money from his account:

    # We open the file to copy his information:
    inFile = open(file, "r")
    lines = inFile.readlines()
    inFile.close()
    # We closed it because we just need a copy to use it when we update user account details

    # We first obtain user current balance:
    balance = float(lines[4].rstrip())
    # We put .rstrip() to avoid value error

    # Now we have to check the validity of the amount entered (float number and bigger than zero and less than balance):
    isNumber = False
    isBigger = False
    isWithdrawable = False
    while not isWithdrawable:
        try:
            # We first check if it is a number, then we check if it is bigger than zero, then if it is less than balance:
            amount = float(
                input("Please Enter the amount of money to withdraw: "))
            # If it is not a number, the program will not continue here
            isNumber = True
            if amount >= 0:
                isBigger = True
                if amount <= balance:
                    isWithdrawable = True
                else:
                    print(
                        "Sorry, you do not have enough money to Withdraw this amount.")
            else:
                print("the amount must be bigger than zero.")
        except ValueError:
            print("Wrong input.Try again")
    # After this point, we are sure that the amount is valid.

    # Doing the Discount:
    balance = balance - amount

    # Saving his new balance:
    lines[4] = str(balance)

    # Now we have to update his information:
    outFile = open(file, "w")
    for line in lines:
        outFile.write(line.rstrip()+"\n")

    # Now we will write the transaction details:
    outFile.write("\nwithdraw: %.1f\n" % amount)
    # we put \n in the beginning so that each transaction separated by an empty line.

    # Calling the date and time methods:
    now = datetime.datetime.now()
    outFile.write(now.strftime("Date: 20%y/%m/%d \nTime: %H:%M:%S\n"))

    outFile.close()

    # Now the program will sleep for few seconds:
    clear_output()
    print("changed successfully. returning to menu..")
    time.sleep(4)

    showMenu()


def depositFun(file):
    # This fuction allows the user to deposit some money to his account:

    # We open the file to copy his information:
    inFile = open(file, "r")
    lines = inFile.readlines()
    inFile.close()
    # We closed it because we just need a copy

    # Now we have to check the validity of the amount entered (float number and bigger than zero):
    isNumber = False
    isBigger = False
    while not isBigger:
        try:
            # We first check if it is a number, then we check if it is bigger than zero:
            amount = float(
                input("Please Enter the amount of money to deposit: "))
            # Wf it is not a number, the program will not continue here
            isNumber = True
            if amount > 0:
                isBigger = True
            else:
                print("the amount must be bigger than zero.")
        except ValueError:
            print("Wrong input.Try again")
    # After this point, we are sure that the amount is valid.

    # Now we take user current balance and convert it to a float number:
    balance = float(lines[4].rstrip())

    # Now we add the amount entered to user balance:
    lines[4] = str(balance + amount)

    # Now we have to update user information:
    outFile = open(file, "w")
    for line in lines:
        outFile.write(line.rstrip()+"\n")

    # Now we will write the transaction details:
    outFile.write("\ndeposit: %.1f\n" % amount)
    # we put \n in the beginning so that each transaction separated by an empty line.

    # Calling the date and time methods:
    now = datetime.datetime.now()
    outFile.write(now.strftime("Date: 20%y/%m/%d \nTime: %H:%M:%S\n"))

    outFile.close()

    # Now the program will sleep for few seconds:
    clear_output()
    print("deposited successfully. returning to menu..")
    time.sleep(4)

    showMenu()


def payBillFun(file):
    # This fuction allows the user to pay a bill from his account:

    # We open the file to copy his information:
    inFile = open(file, "r")
    lines = inFile.readlines()
    inFile.close()

    billName = input("Enter the name of the bill: ")

    # Checking that the bill name is not empty:
    while billName == "" or billName.isspace():
        print("Please enter at least one character for the name")
        billName = input("Enter the name of the bill: ")

    billNumber = input("Enter the account number of this bill (4 digits): ")

    # Checking that the bill account is containing 4 digits:
    billDigits = []
    for number in billNumber:
        billDigits.append(number)
    billDigits = set(billDigits)
    while not billNumber.isdigit() or len(billDigits) != 4:
        print("Bill number must contain 4 unique digits.")
        billNumber = input("Enter the account number of this bill(4 digits): ")
        billDigits = []
        for number in billNumber:
            billDigits.append(number)
        billDigits = set(billDigits)

    # Here the program will get the balance from the user’s file
    balance = float(lines[4].rstrip())

    # Now we have to check the validity of the amount entered (float number and bigger than zero):
    isNumber = False
    isBigger = False
    while not isBigger:
        try:
            # We first check if it is a number, then we check if it is bigger than zero:
            billValue = float(input("Please enter the value of the bill: "))
            isNumber = True
            if billValue >= 0:
                isBigger = True
            else:
                print("The bill must be bigger than zero.")
        except ValueError:
            print("Wrong input.Try again")
    # At this point, we are sure that billValue is a digit and greater than zero.

    # Now we have to check that billValue less than balance:
    if billValue <= balance:
        # If bill value is less than balance , the old balance will be deducted by billValue:
        balance = balance - billValue

        # Now we will save the new balance:
        lines[4] = str(balance)

        # Now we have to update user information:
        outFile = open(file, "w")
        for line in lines:
            outFile.write(line.rstrip()+"\n")

        # Now we will write the transaction details:
        outFile.write("\nBill name: %s\n" % billName)
        # we put \n in the beginning so that each transaction separated by an empty line.
        outFile.write("Account number: %s\n" % billNumber)
        outFile.write("amount: %.1f\n" % billValue)

        # Calling the date and time methods:
        now = datetime.datetime.now()
        outFile.write(now.strftime("Date: 20%y/%m/%d \nTime: %H:%M:%S\n"))

        outFile.close()

        # Now the program will sleep for few seconds:
        clear_output()
        print("bill has been paid. returning to menu..")
        time.sleep(4)

        showMenu()
    else:
        # If bill value is bigger than balance, the old balance will not change.

        # Now the program will exit and sleep for few seconds:
        clear_output()
        print("Sorry, you do not have enough money to pay the bill. Try to deposit some money frist.")
        time.sleep(5)
        clear_output()
        print("returning to menu..")
        time.sleep(3)

        showMenu()


def viewTransactionsFun(file):
    # This fuction shows the last transactions of the account:

    # We open the file to copy his information:
    inFile = open(file, "r")
    lines = inFile.readlines()
    inFile.close()

    # We have to check if there are transactions or not:
    if len(lines) == 5:  # 5 is the number of lines that contain the account information
        print("no transactions")
    else:
        print("Last transactions:")  # this is a header

        # printing the transactions:
        for number in range(5, len(lines)):
            # from 5: line 6, which is an empty line
            # to len(lines): the last line, which its postion in the list is (len(lines) - 1)
            print(lines[number].rstrip())

    # now the program will sleep for few seconds:
    time.sleep(len(lines)/4 + 5)  # :relevant time
    clear_output()
    print("returning to menu..")
    time.sleep(3)

    showMenu()


def terminateFun(file):
    # this fuction shows the last transactions and terminate the program:

    # We open the file to copy his information:
    inFile = open(file, "r")
    lines = inFile.readlines()
    inFile.close()

    # We have to check if there are transactions or not:
    if len(lines) == 5:
        print("no last transactions")
    else:
        for number in range(5, len(lines)):
            print(lines[number].rstrip())

    # now the program will sleep for few seconds without showing the menu:
    time.sleep(6)
    clear_output()


def main():
    # Program starts here.

    # First, we need to check if the user has an account or not (does the file exist or not):
    file = "cardNumber.txt"
    try:
        infile = open(file, "r")
        # if the file exists, it will continue here, otherwise, it will go directly to except block
        found = True
        infile.close()
    except IOError:
        found = False
    # if found = True: the file exists
    # if found = False: the file does not exist

    # asking the user to login or sign up:
    sOrL = input("Enter S for sign up or L for login: ").upper()

    # making sure that the input is correct:
    while sOrL != "S" and sOrL != "L":  # we can use "or", no difference.
        print("Wrong input. Enter S or L only.")
        sOrL = input("Enter S for sign up or L for login: ").upper()

    # Making the decision:
    if sOrL == "S":
        # the user want to sign up.
        create()
    else:
        # the user want to login.

        # We have to check if the user already has an account or not:
        if found:
            # if there is an account:
            login()

        while not found:
            # if there is no account, we will ask the user to create one:
            print("you do not have an account. Go and create one!.")

            # asking the user again to login or sign up:
            sOrL = input("Enter S for sign up or L for login: ").upper()

            # making sure that the input is correct:
            while sOrL != "S" and sOrL != "L":
                print("Wrong input. Enter S or L only")
                sOrL = input("Enter S for sign up or L for login: ").upper()

            # if he entered "S", the sign up gate will appear and the program will get out from the loop.
            # otherwise, the program will ask the user again to create an account
            if sOrL == "S":
                create()
                break  # or we can write: found = True

    # Now, we ask the user to enter one of the 7 features:
    feature = input("Enter your feature: ")

    # checking if the input is correct and in range:
    while len(feature) != 1 or not feature in "1234567":
        print("Wrong input. Try again")
        feature = input("Enter your feature: ")

    # This is the main part of program:
    while True:
        # We will ask the user continuously to enter a feature until he enter feature number 7 (terminate):

        clear_output()  # every time we clear the output
        if feature == "1":
            show(file)
        if feature == "2":
            changePINFun(file)
        if feature == "3":
            withdrawFun(file)
        if feature == "4":
            depositFun(file)
        if feature == "5":
            payBillFun(file)
        if feature == "6":
            viewTransactionsFun(file)
        if feature == "7":
            terminateFun(file)
            break  # this is the terminate point

        feature = input("Enter your feature: ")

        # checking again if the input is correct and in range:
        while len(feature) != 1 or not feature in "1234567":
            print("Wrong input. Try again")
            feature = input("Enter your feature: ")


main()  # Program starts here. 