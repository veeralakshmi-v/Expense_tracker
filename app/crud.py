from sqlalchemy.orm import Session
from . import models, schemas

def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(title=expense.title, amount=expense.amount, category=expense.category)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session):
    return db.query(models.Expense).all()

def get_highest_expense(db: Session):
    return db.query(models.Expense).order_by(models.Expense.amount.desc()).first()
