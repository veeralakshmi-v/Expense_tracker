from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, database

router = APIRouter(prefix="/expenses", tags=["Expense Tracker"])

@router.post("/", response_model=schemas.Expense)
def add_expense(expense: schemas.ExpenseCreate, db: Session = Depends(database.get_db)):
    return crud.create_expense(db=db, expense=expense)

@router.get("/", response_model=List[schemas.Expense])
def get_all_expenses(db: Session = Depends(database.get_db)):
    return crud.get_expenses(db=db)

@router.get("/highest", response_model=schemas.Expense)
def get_highest_expense(db: Session = Depends(database.get_db)):
    highest = crud.get_highest_expense(db=db)
    if not highest:
        raise HTTPException(status_code=404, detail="No expenses found")
    return highest
