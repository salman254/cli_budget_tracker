from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, User, Category, Transaction, Budget, Note, TransactionType
from datetime import date

engine = create_engine("sqlite:///db/budget.db")
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data
session.query(Note).delete()
session.query(Transaction).delete()
session.query(Budget).delete()
session.query(Category).delete()
session.query(User).delete()

# Add Users
user1 = User(username="salman", email="salman@example.com")
session.add(user1)
session.commit()

# Add Categories
cat_food = Category(name="Groceries", user=user1)
cat_salary = Category(name="Salary", user=user1)
session.add_all([cat_food, cat_salary])
session.commit()

# Add Budget
budget_food = Budget(amount=300, period="monthly", user=user1, category=cat_food)
session.add(budget_food)
session.commit()

# Add Transactions
tx1 = Transaction(
    title="Weekly groceries",
    description="Bought vegetables and rice",
    amount=50,
    type=TransactionType.expense,
    date=date.today(),
    user=user1,
    category=cat_food
)
tx2 = Transaction(
    title="Monthly Salary",
    description="Received from employer",
    amount=1000,
    type=TransactionType.income,
    date=date.today(),
    user=user1,
    category=cat_salary
)
session.add_all([tx1, tx2])
session.commit()

# Add Notes
note1 = Note(content="Used discount voucher", transaction=tx1)
session.add(note1)

session.commit()
print("✅ Seed data inserted.")
