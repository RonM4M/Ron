#To associate pin to user details,using {}
def load_data():  
    bankd ={}
    with open("bank.txt","r") as f:
        for line in f:
            pin,name,balance=line.strip().split(",")
            bankd[int(pin)]={"name":name,"balance":float(balance)}
    return bankd
#To write latest data into txt from {}
def add_data(bankd):
    with open("bank.txt","w") as f:
        for pin,data in bankd.items():
            f.write(f"{pin},{data['name']},{data['balance']}\n")


while(True):
    bankd=load_data()
    print("\t1.Create an account\n\t2.Check Balance\n\t3.Deposit Money\n\t4.Withdraw money\n\t5.Exit")
    choice = int(input("Enter your choice(1/2/3/4/5): "))
    if choice ==  1:
        name = input("Enter name: ")
        pin1 = int(input("Enter 4 digit pin: "))
        dep = float(input("Enter deposit amount: "))
        bankd[pin1] = {"name":name,"balance":dep}
        add_data(bankd)
        print("Account created")
    elif choice == 2:
        name = input("Enter name(first letter capital): ")
        for key in bankd:
            if bankd[key]["name"].lower() == name.lower():
                print("Account found")
                pin = int(input("Enter pin: "))
                if(key == pin):
                    print("Balance: ",bankd[key]["balance"])
                    add_data(bankd)
                else:
                    print("Incorrect")
            else:
                pass
       
    elif choice == 3:
        name = input("Enter name(first letter capital): ")
        for key in bankd:
            if bankd[key]["name"].lower() == name.lower():
                print("Account found")
                pin = int(input("Enter pin: "))
                if(pin == key):
                    dep=float(input("Enter amount to deposit: "))
                    bankd[key]["balance"]+=dep
                    print("Successfully deposited.")
                    add_data(bankd)
                else:
                    break
            else:
                pass

    elif choice == 4:
        name = input("Enter name: ")
        for key in bankd:
            if name == bankd[key]["name"]:
                print("Account found")
                pin = int(input("Enter pin: "))
                if(pin == key):
                    print("Current balance: ",bankd[key]["balance"])
                    withdep=int(input("Enter amount to withdraw: "))
                    if bankd[key]["balance"] < withdep:
                        print("Insufficient balance")
                    else:
                        bankd[key]["balance"]-=withdep
                        add_data(bankd)
                        print("Withdrawn. Remaining balance: ",bankd[key]["balance"])
                else:
                    print("Incorrect")
            else:
                pass
    elif choice == 5:
        break
    else:
        print("Invalid option")
print("\n **Thank you for banking with us**")
                
