from fastapi import APIRouter

router = APIRouter(prefix="/demo", tags=["Demo APIs"])

@router.get("/hello")
def say_hello():
    return {"message": "Hello! Welcome to your first FastAPI app."}

@router.get("/json-example")
def json_example():
    return {
        "student": {"name": "Kousalya", "course": "FastAPI Basics"},
        "topics": ["Request", "Response", "JSON", "API Testing"]
    }
