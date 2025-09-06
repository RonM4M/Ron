#To associate pin to user details,using {}
def load_data():  
    bank ={}
    with open("bank.txt","r") as f:
        for line in f:
            pin,name,balance=line.strip().split(",")
            bank[int(pin)]={"name":name,"balance":balance}
#To write latest data into txt from {}
def add_data(bank):
    with open("bank.txt","w") as f:
        for pin,data in bank.items:
            f.write(f"{pin},{data['name']},{data['balance']}\n")
            
                   
print("Bank")


#To be modified
while(True):
    bank=load_data()
    print("\t1.Create an account\n\t2.Check Balance\n\t3.Deposit Money\n\t4.Withdraw money\n\t5.Exit")
    choice = int(input("Enter your choice(1/2/3/4/5): "))
    if choice ==  1:
        name = input("Enter name: ")
        pin1 = int(input("Enter 4 digit pin: "))
        dep = int(input("Enter deposit amount: "))
        bank[pin1] = {"name":name,"balance":dep}
        print("Account created")
        print(bank)
    elif choice == 2:
        name = input("Enter name(first letter capital): ")
        for key in bank:
            if bank[key]["name"].lower() == name.lower():
                print("Account found")
                pin = int(input("Enter pin: "))
                if(key == pin):
                    print("Balance: ",bank[key]["balance"])
                else:
                    print("Incorrect")
            else:
                pass
       
    elif choice == 3:
        name = input("Enter name(first letter capital): ")
        for key in bank:
            if bank[key]["name"].lower() == name.lower():
                print("Account found")
                pin = int(input("Enter pin: "))
                if(pin == key):
                    dep=float(input("Enter amount to deposit: "))
                    bank[key]["balance"]+=dep
                else:
                    break
            else:
                pass

    elif choice == 4:
        name = input("Enter name: ")
        for key in bank:
            if name == bank[key]["name"]:
                print("Account found")
                pin = int(input("Enter pin: "))
                if(pin == key):
                    print("Current balance: ",bank[key]["balance"])
                    withdep=int(input("Enter amount to withdraw: "))
                    if bank[key]["balance"] < withdep:
                        print("Insufficient balance")
                    else:
                        bank[key]["balance"]-=withdep
                        print("Withdrawn. Remaining balance: ",bank[key]["balance"])
                else:
                    print("Incorrect")
            else:
                pass
    elif choice == 5:
        break
    else:
        print("Invalid option")
print("\n **Thank you for banking with us**")
                
