from fastapi import APIRouter
from utils.helpers import simple_nlp_response

router = APIRouter()

@router.post("/ask")
def ask_question(query: dict):
    question = query.get("question", "")
    answer = simple_nlp_response(question)
    return {"answer": answer}
