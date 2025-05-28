from db.models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lib.category import category_menu
from lib.transaction import transaction_menu
from lib.budget import budget_menu

engine = create_engine("sqlite:///db/budget.db")
Session = sessionmaker(bind=engine)
session = Session()

user = session.query(User).filter_by(username="salman").first()

def main_menu():
    while True:
        print("\nBudget Tracker CLI")
        print("1. Manage Categories")
        print("2. Manage Transactions")
        print("3. Manage Budgets")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            category_menu(session, user)
        elif choice == "2":
            transaction_menu(session, user)
        elif choice == "3":
            budget_menu(session, user)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")
