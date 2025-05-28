from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date, Enum, DECIMAL
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    categories = relationship("Category", back_populates="user", cascade="all, delete")
    transactions = relationship("Transaction", back_populates="user", cascade="all, delete")
    budgets = relationship("Budget", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="categories")
    transactions = relationship("Transaction", back_populates="category", cascade="all, delete")
    budgets = relationship("Budget", back_populates="category", cascade="all, delete")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', user_id={self.user_id})>"

class TransactionType(enum.Enum):
    income = "income"
    expense = "expense"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    amount = Column(DECIMAL, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    user = relationship("User", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, title='{self.title}', amount={self.amount}, type={self.type})>"

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)
    amount = Column(DECIMAL, nullable=False)
    period = Column(String, nullable=False)  # e.g., 'monthly' or 'yearly'
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    user = relationship("User", back_populates="budgets")
    category = relationship("Category", back_populates="budgets")

    def __repr__(self):
        return f"<Budget(id={self.id}, amount={self.amount}, period='{self.period}')>"
