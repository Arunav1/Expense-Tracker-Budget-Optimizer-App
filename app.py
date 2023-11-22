class ExpenseCategory:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append({"description": description, "amount": amount})

    def calculate_remaining_budget(self):
        total_expenses = sum(expense["amount"] for expense in self.expenses)
        remaining_budget = self.budget - total_expenses
        return remaining_budget

def print_categories(categories):
    for category in categories:
        print(f"{category.name} Budget: Rs{category.budget} | Remaining Budget: ${category.calculate_remaining_budget()}")

def add_expense(categories, category_name, description, amount):
    for category in categories:
        if category.name == category_name:
            category.add_expense(description, amount)
            print(f"Expense added to {category_name} category.")
            return
    print(f"Category {category_name} not found.")

def optimize_budget(categories):
    total_remaining_budget = sum(category.calculate_remaining_budget() for category in categories)

    for category in categories:
        remaining_budget_ratio = category.calculate_remaining_budget() / total_remaining_budget
        for expense in category.expenses:
            expense["amount"] += remaining_budget_ratio * expense["amount"]

def main():
    # Create expense categories
    categories = [
        ExpenseCategory("Food", 1000),
        ExpenseCategory("Entertainment", 3000),
        ExpenseCategory("Utilities", 5000),
    ]

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Categories and Budgets")
        print("3. Optimize Budget")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category_name = input("Enter the category name: ")
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(categories, category_name, description, amount)
        elif choice == "2":
            print_categories(categories)
        elif choice == "3":
            optimize_budget(categories)
            print("Budget optimized.")
        elif choice == "4":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
