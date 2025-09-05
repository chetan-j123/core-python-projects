def noting(date, category, amount, note):
    with open("expensetracker.txt", "a") as file:
        file.write(f"{date},{category},{amount},{note}\n")

def main():
    print("=================== Expense Tracker App ===============")
    print("1. Add expense") 
    print("2. View expense by date")
    print("3. View expense by category")
    print("4. Show all expenses")
    print("5. Exit")

    userchoice = input("Enter the choice= ")

    # ---------- Add Expense ----------
    if userchoice == "1":
        date = input("Enter the date= ")
        category = input("Enter the category of expense= ")
        amount = input("Enter the amount= ")
        note = input("Enter the note= ")
        noting(date, category, amount, note)
        print("✅ Expense added successfully!")
        main()

    # ---------- Load File Data ----------
    try:
        with open("expensetracker.txt", "r") as file:
            lines = [line.strip().split(",") for line in file if line.strip()]
    except FileNotFoundError:
        lines = []

    # ---------- View by Date ----------
    if userchoice == "2":
        date = input("Enter the date= ")
        found = False
        for row in lines:
            if row[0] == date:
                print("Expense found:", row)
                found = True
        if not found:
            print("❌ No expenses found for date =", date)
        main()

    # ---------- View by Category ----------
    if userchoice == "3":
        cate = input("Enter the category (food, bike, car, etc)= ")
        found = False
        for row in lines:
            if row[1] == cate:
                print("Expense found:", row)
                found = True
        if not found:
            print("❌ No expenses found for category =", cate)
        main()

    # ---------- Show All Expenses ----------
    if userchoice == "4":
        if not lines:
            print("No expenses recorded yet.")
        else:
            for row in lines:
                print(row)
        main()

    # ---------- Exit ----------
    if userchoice == "5":
        print("👋 Exiting... Goodbye!")

main()

  


