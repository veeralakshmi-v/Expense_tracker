from fastapi import FastAPI
from . import models, database
from .routes import demo_routes, expense_routes

models.Base.metadata.create_all(bind=database.engine)   # creates your database tables.

app = FastAPI(title="FastAPI Expense Tracker")

app.include_router(demo_routes.router)
app.include_router(expense_routes.router)       # connects your expense routes (the actual API functions).

@app.get("/show")
def root():
    return {"message": "Welcome to FastAPI Expense Tracker API"}
