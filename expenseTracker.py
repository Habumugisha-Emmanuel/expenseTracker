expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("✅ Expense added!")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
        return

    print("\n--- Your Expenses ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['amount']} - {exp['category']} - {exp['description']}")

def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice!")

main()