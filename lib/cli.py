from db.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.category import view_categories
from lib.transaction import add_transaction, view_transactions
from lib.budget import view_budgets
from lib.budget import report_budget_status


engine = create_engine("sqlite:///db/budget.db")
Session = sessionmaker(bind=engine)
session = Session()

user = session.query(User).filter_by(username="salman").first()

def main_menu():
    while True:
        print("\nBudget Tracker CLI")
        print("1. View Categories")
        print("2. Add Transaction")
        print("3. View Budgets")
        print("4. View Transactions")
        print("5. View Budget Reports")
        print("6. Exit")


        choice = input("Select an option: ")

        if choice == "1":
            view_categories(session, user)
        elif choice == "2":
            add_transaction(session, user)
        elif choice == "3":
            view_budgets(session, user)
        elif choice == "4":
            view_transactions(session, user)
        elif choice == "5":
                report_budget_status(session, user)
        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
