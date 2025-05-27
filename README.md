
# Budget Tracker CLI

A simple command-line Python application to help users manage their income, expenses, budgets, and spending categories using a local SQLite database and SQLAlchemy ORM.

## Features

- View categories created for a user
- Add new transactions with type, category, and amount
- View all budget entries per category and period
- View all recorded transactions
- View budget status: compare spending against budget and get status

## Technologies

- Python 3
- SQLAlchemy ORM
- Alembic for database migrations
- SQLite (local database)
- Pipenv for dependency management

## Project Structure

cli-budget-tracker/
├── lib/
│   ├── cli.py              # Main CLI menu and routing
│   ├── category.py         # View categories
│   ├── transaction.py      # Add and view transactions
│   └── budget.py           # View budgets and report status
├── db/
│   ├── models.py           # ORM models and relationships
│   ├── seed.py             # Pre-populates the database
│   └── migrations/         # Alembic migration files
├── main.py                 # Entry point to run the CLI
├── Pipfile                 # Pipenv dependencies
└── README.md               # Project documentation

## How to Run

1. Install dependencies:

    pipenv install

2. Initialize the database:

    alembic upgrade head

3. Seed sample data:

    pipenv run python -m db.seed

4. Launch the CLI:

    pipenv run python main.py

## CLI Menu Options

1. **View Categories** – Lists all categories associated with the user.
2. **Add Transaction** – Add an income or expense, assign it to a category.
3. **View Budgets** – Show all budget entries with category and amount.
4. **View Transactions** – Lists all user transactions with basic details.
5. **View Budget Reports** – Compares actual spending with the budget.
6. **Exit** – Ends the program.

## Sample CLI Output

Welcome to Budget Tracker CLI

1. View Categories
2. Add Transaction
3. View Budgets
4. View Transactions
5. View Budget Reports
6. Exit

Select an option: 1

Categories:
ID: 1 | Name: Groceries
ID: 2 | Name: Salary

Press Enter to return to the main menu...


LICENSE - MIT.
