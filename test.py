bank ={"John":14000,"Ron":15000}
print("Bank. We Judge you")
while(True):
    print('''\t1.Create an account\n\t2.Check Balance\n\t3.Deposit Money\n\t4.Withdraw money\n\t5.Exit''')
    choice = int(input("Enter your choice(1/2/3/4/5): "))
    if choice ==  1:
        name = input("Enter name: ")
        dep = int(input("Enter deposit amount: "))
        bank[name] = dep
        print("Account created. Here comes tax, 0 is our limit. Enjoy")
        print(bank)
    elif choice == 2:
        name = input("Enter name (first letter capital): ")
        flag=1
        for key in bank:
            if name.lower() == key.lower():
                print("Account found")
                print("Balance: ",bank[name])
                flag=1
                break
            else:
                flag=0
        if flag == 0:
            print("Not a customer here. We still judge you.")
    elif choice == 3:
        name = input("Enter name: ")
        flag=1
        for key in bank:
            if name == key:
                print("Account found ; Current Balance: ",bank[name])
                todep=int(input("Enter amount to deposit: "))
                bank[name]+=todep
                print(bank)
                print("Deposit complete. Here comes more tax.")
                flag=1
                break
            else:
                flag=0
        if flag == 0:
            print("Not a customer here. ")

    elif choice == 4:
        name = input("Enter name: ")
        flag=1
        for key in bank:
            if name == key:
                print("Account found : Current Balance: ",bank[name])
                withdep=int(input("Enter amount to withdraw if you have any left: "))
                if bank[name] < withdep:
                    print("Insufficient balance / Broke")
                else:
                    bank[name]-=withdep
                    print("Withdrawn. You will be less taxed.")
                    print(bank)
                flag=1
                break
            else:
                flag=0
        if flag == 0:
            print("Not a customer here. ")
    elif choice == 5:
        break
    else:
        print("Invalid option")
print("\n **Thank you for banking with us**")
                
