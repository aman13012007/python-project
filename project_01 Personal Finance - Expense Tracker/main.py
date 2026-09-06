# Expense Tracker Project

expensesList = [] #list of expensesList in form of dictionary

print("Welcome to Expense Tracker : ")

while True:
    print("====MENU====")
    print("1. Add expensesList")
    print("2. View All expensesList")
    print("3. View All purchases")
    print("4.Exit")

    choice = int(input("Please Enter Your Choice: "))

    # 1. Add Expense
    if (choice == 1):
        date= input("Enter the date of purchase?: ")
        category= input("purchases Type? ( Food , Travel , Makeup, Books ):")
        description=input("give any other detail : ")
        amount= float(input("Enter the amount: "))


        expense= {
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expensesList.append(expense)
        print("\n  Done. Expense is added succesfully")

    # 2. VIEW ALL expensesList

    elif(choice==2):
        if (len(expensesList)==0):
            print(" No expensesList Added. Jao pahle karcha karo. ")
        else:
            print("==== your expense ====")
            count=1
            for eachpurchase in expensesList:
                print(f"purchase Number {count} -> {eachpurchase["date"]}, {eachpurchase["category"]}, {eachpurchase["description"]}, {eachpurchase["amount"]} ")
                count+=1

    # 3. VIEW TOTAL SPENDING

    elif(choice ==3):
        total=0
        for eachpurchase in expensesList:
            total = total + eachpurchase["amount"]

        print("\n Total Purchase = ",total)


    # 4. EXIT

    elif(choice==4):
        print("Thank you for use our system ")
        break

    else:
        print(" INVALID CHOICE. TRY AGAIN ")






