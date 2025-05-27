
from db.models import Budget
from db.models import Budget, Transaction, TransactionType

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
