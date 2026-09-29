print("==========================================")
print("            EXPENSE TRACKER")
print("==========================================")

expenses = []

while True:
    print("\n============== MENU ==============")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expense")
    print("4. Search Expense by Category")
    print("5. Delete Expense")
    print("6. Expense Summary")
    print("7. Exit")
    print("==================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date: ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        if amount > 0:
            expense = {
                "date": date,
                "category": category,
                "description": description,
                "amount": amount
            }

            expenses.append(expense)
            print("Expense added successfully.")
        else:
            print("Amount must be greater than zero.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\n========== ALL EXPENSES ==========")

            for index, expense in enumerate(expenses, start=1):
                print("\nExpense", index)
                print("Date        :", expense["date"])
                print("Category    :", expense["category"])
                print("Description :", expense["description"])
                print("Amount      : ₹", expense["amount"])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("\nTotal Expense: ₹", total)

    elif choice == "4":
        category = input("Enter category to search: ").lower()
        found = False
        category_total = 0

        print("\n========== SEARCH RESULTS ==========")

        for expense in expenses:
            if expense["category"].lower() == category:
                print("\nDate        :", expense["date"])
                print("Description :", expense["description"])
                print("Amount      : ₹", expense["amount"])

                category_total += expense["amount"]
                found = True

        if found:
            print("\nTotal for", category, ": ₹", category_total)
        else:
            print("No expenses found for this category.")

    elif choice == "5":
        if not expenses:
            print("No expenses available to delete.")
        else:
            print("\n========== EXPENSE LIST ==========")

            for index, expense in enumerate(expenses, start=1):
                print(
                    index,
                    "-",
                    expense["date"],
                    "-",
                    expense["category"],
                    "- ₹",
                    expense["amount"]
                )

            try:
                number = int(input("Enter expense number to delete: "))

                if 1 <= number <= len(expenses):
                    removed = expenses.pop(number - 1)
                    print(
                        "Deleted expense:",
                        removed["description"]
                    )
                else:
                    print("Invalid expense number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "6":
        if not expenses:
            print("No expenses available.")
        else:
            total = sum(expense["amount"] for expense in expenses)

            categories = {}

            for expense in expenses:
                category = expense["category"]

                if category in categories:
                    categories[category] += expense["amount"]
                else:
                    categories[category] = expense["amount"]

            print("\n========== EXPENSE SUMMARY ==========")
            print("Number of Expenses:", len(expenses))
            print("Total Expense: ₹", total)

            print("\nCategory-wise Expenses:")

            for category, amount in categories.items():
                print(category, ": ₹", amount)

    elif choice == "7":
        print("\nThank you for using the Expense Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")
