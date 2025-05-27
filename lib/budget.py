
from db.models import Budget

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
