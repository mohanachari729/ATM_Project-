balance = 500
def display_menu():
    print("\ATM MENU:")
    print("1.CREDIT")
    print("2.DEBIT")
    print("3.balance")
    print("4.EXIT")
def get_choice():
    return input("enter your option(1-4):")
def CREDIT():
    global balance
    amount = float(input("enter your amount:"))
    if amount <= 0 :
        print("enter the positive amount")
    else :
        balance += amount
        print(f"${amount}credited in your account")
        print(f"you total balance is ${balance}")
def DEBIT():
    global balance
    amount = float(input("enter your amount:"))
    if amount > balance :
        print("your account have a not sufficient balance")
    else :
        balance -= amount
        print(f"the ${amount} has been debited in your account")
        print(f"your total balance is ${balance}")
def show_balance():
    print(f"your total balance is ${balance}")
def main():
    while True :
        display_menu()
        choice=get_choice()
        if choice == "1":
            CREDIT()
        elif choice == "2":
            DEBIT()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            print("thank for using ATM have a nice day")
            break
        else :
            print("please enter the valid choice")
main()






    

    