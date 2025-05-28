from db.models import Transaction, TransactionType, Category
from datetime import date

def transaction_menu(session, user):
    while True:
        print("\nTransaction Management")
        print("1. View Transactions")
        print("2. Add Transaction")
        print("3. Edit Transaction")
        print("4. Delete Transaction")
        print("5. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == "1":
            view_transactions(session, user)
        elif choice == "2":
            add_transaction(session, user)
        elif choice == "3":
            edit_transaction(session, user)
        elif choice == "4":
            delete_transaction(session, user)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
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

def edit_transaction(session, user):
    view_transactions(session, user)
    tx_id = input("Enter the ID of the transaction to edit: ")
    tx = session.query(Transaction).filter_by(id=tx_id, user_id=user.id).first()
    if not tx:
        print("Transaction not found.")
        input("Press Enter to continue...")
        return

    tx.title = input(f"New title [{tx.title}]: ") or tx.title
    tx.description = input(f"New description [{tx.description}]: ") or tx.description
    tx.amount = float(input(f"New amount [{tx.amount}]: ") or tx.amount)
    
    type_input = input(f"New type (income/expense) [{tx.type.value}]: ").lower() or tx.type.value
    if type_input in ["income", "expense"]:
        tx.type = TransactionType.income if type_input == "income" else TransactionType.expense

    categories = session.query(Category).filter_by(user_id=user.id).all()
    for idx, cat in enumerate(categories, start=1):
        print(f"{idx}. {cat.name}")
    cat_choice = input("Enter new category number (or leave blank to keep current): ")
    if cat_choice:
        try:
            tx.category = categories[int(cat_choice) - 1]
        except (IndexError, ValueError):
            print("Invalid selection. Category unchanged.")

    session.commit()
    print("Transaction updated.")
    input("Press Enter to continue...")

def delete_transaction(session, user):
    view_transactions(session, user)
    tx_id = input("Enter the ID of the transaction to delete: ")
    tx = session.query(Transaction).filter_by(id=tx_id, user_id=user.id).first()
    if tx:
        session.delete(tx)
        session.commit()
        print("Transaction deleted.")
    else:
        print("Transaction not found.")
    input("Press Enter to continue...")
