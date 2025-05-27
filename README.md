
# Budget Tracker CLI

A command-line budget tracking application built with Python. It helps users manage expenses and income, categorize financial activities, set budgets, and track spending against set limits — all from the terminal.

---

## Setup Instructions

1. **Clone the repository** 
    
    git clone git@github.com:salman254/cli_budget_tracker.git
    cd budget-tracker-cli
    

2. **Install dependencies using Pipenv**:
    
    pipenv install
    pipenv shell
    

3. **Run database migrations**:
    
    alembic upgrade head
    

4. **Seed the database with sample data**:
    
    pipenv run python -m db.seed
    

5. **Run the CLI app**:
    
    pipenv run python main.py
    

---

## Features

- View all spending categories
- Add new transactions (income or expense)
- View all recorded transactions
- Set and view budgets by category and period
- Compare spending vs. budget with reporting
- Local database powered by SQLite

---

## Technologies Used

- Python 3
- SQLAlchemy (ORM)
- Alembic (Migrations)
- SQLite (Local storage)
- Pipenv (Virtual environment and package manager)

---

## Support / Contact

For issues, questions, or suggestions, feel free to reach out:

- Email: Salmaanmohamed700@gmail.com
- GitHub: Salmaanmohamed700@gmail.com

---

## License

This project is licensed under the MIT License.


