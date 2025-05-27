
from db.models import Transaction, TransactionType, Category
from datetime import date

def add_transaction(session, user):
    print("\nAdd a New Transaction")

    title = input("Title: ")
    description = input("Description: ")
    amount = float(input("Amount: "))
    type_input = input("Type (income/expense): ").lower()

    if type_input not in ["income", "expense"]:
        print("Invalid type. Must be 'income' or 'expense'.")
        input("Press Enter to continue...")
        return

    type_enum = TransactionType.income if type_input == "income" else TransactionType.expense

    categories = session.query(Category).filter_by(user_id=user.id).all()
    if not categories:
        print("You must create a category first.")
        input("Press Enter to continue...")
        return

    print("\nSelect a category:")
    for idx, cat in enumerate(categories, start=1):
        print(f"{idx}. {cat.name}")
    cat_choice = int(input("Enter category number: ")) - 1

    try:
        category = categories[cat_choice]
    except IndexError:
        print("Invalid category selection.")
        input("Press Enter to continue...")
        return

    tx = Transaction(
        title=title,
        description=description,
        amount=amount,
        type=type_enum,
        date=date.today(),
        user=user,
        category=category
    )

    session.add(tx)
    session.commit()
    print("Transaction added successfully.")
    input("Press Enter to continue...")

def view_transactions(session, user):
    txs = session.query(Transaction).filter_by(user_id=user.id).all()

    if txs:
        for t in txs:
            print(f"ID: {t.id}")
            print(f"Title: {t.title}")
            print(f"Amount: {t.amount}")
            print(f"Type: {t.type.value}")
            print(f"Category: {t.category.name}")
            print(f"Date: {t.date}")
            print("-" * 30)
    else:
        print("No transactions found.")
    input("Press Enter to continue...")