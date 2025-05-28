from db.models import Budget, Transaction, TransactionType, Category

def budget_menu(session, user):
    while True:
        print("\nBudget Management")
        print("1. View Budgets")
        print("2. Add Budget")
        print("3. Edit Budget")
        print("4. Delete Budget")
        print("5. Report Budget Status")
        print("6. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            view_budgets(session, user)
        elif choice == "2":
            add_budget(session, user)
        elif choice == "3":
            edit_budget(session, user)
        elif choice == "4":
            delete_budget(session, user)
        elif choice == "5":
            report_budget_status(session, user)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

def view_budgets(session, user):
    budgets = session.query(Budget).filter_by(user_id=user.id).all()
    if budgets:
        for b in budgets:
            print(f"ID: {b.id}")
            print(f"Category: {b.category.name}")
            print(f"Amount: {b.amount}")
            print(f"Period: {b.period}")
            print("-" * 30)
    else:
        print("No budgets found.")
    input("Press Enter to continue...")

def add_budget(session, user):
    categories = session.query(Category).filter_by(user_id=user.id).all()
    if not categories:
        print("No categories found. Create a category first.")
        input("Press Enter to continue...")
        return

    print("Select category:")
    for idx, cat in enumerate(categories, start=1):
        print(f"{idx}. {cat.name}")
    choice = int(input("Enter category number: ")) - 1

    try:
        category = categories[choice]
    except IndexError:
        print("Invalid selection.")
        input("Press Enter to continue...")
        return

    amount = float(input("Enter budget amount: "))
    period = input("Enter period (e.g., monthly): ")

    new_budget = Budget(amount=amount, period=period, user=user, category=category)
    session.add(new_budget)
    session.commit()
    print("Budget added successfully.")
    input("Press Enter to continue...")

def edit_budget(session, user):
    view_budgets(session, user)
    budget_id = input("Enter the ID of the budget to edit: ")
    budget = session.query(Budget).filter_by(id=budget_id, user_id=user.id).first()

    if not budget:
        print("Budget not found.")
        input("Press Enter to continue...")
        return

    amount_input = input(f"New amount [{budget.amount}]: ")
    period_input = input(f"New period [{budget.period}]: ")

    if amount_input:
        budget.amount = float(amount_input)
    if period_input:
        budget.period = period_input

    session.commit()
    print("Budget updated.")
    input("Press Enter to continue...")

def delete_budget(session, user):
    view_budgets(session, user)
    budget_id = input("Enter the ID of the budget to delete: ")
    budget = session.query(Budget).filter_by(id=budget_id, user_id=user.id).first()
    if budget:
        session.delete(budget)
        session.commit()
        print("Budget deleted.")
    else:
        print("Budget not found.")
    input("Press Enter to continue...")

def report_budget_status(session, user):
    budgets = session.query(Budget).filter_by(user_id=user.id).all()
    if not budgets:
        print("No budgets set. Add budgets to use this feature.")
        input("Press Enter to continue...")
        return

    for budget in budgets:
        category = budget.category
        total_spent = sum(
            t.amount for t in session.query(Transaction)
            .filter_by(user_id=user.id, category_id=category.id, type=TransactionType.expense)
        )

        print(f"Category: {category.name}")
        print(f"Budget: {budget.amount}")
        print(f"Total Spent: {total_spent}")

        if total_spent > budget.amount:
            print("Status: OVER BUDGET")
        elif total_spent == budget.amount:
            print("Status: ON BUDGET")
        else:
            print(f"Status: UNDER BUDGET (Remaining: {budget.amount - total_spent})")

        print("-" * 40)

    input("Press Enter to continue...")
