# Shared utility functions (e.g., for NLP, validation, etc.)
def simple_nlp_response(query: str) -> str:
    # Placeholder for rule-based/NLP Q&A
    if "library" in query.lower():
        return "The library is open from 8am to 10pm."
    elif "cafeteria" in query.lower():
        return "The cafeteria serves food from 7am to 8pm."
    else:
        return "Sorry, I don't have an answer for that yet."
