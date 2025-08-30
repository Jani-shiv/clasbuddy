from fastapi import FastAPI
from api import events, campus_map, academics, community, assistant

app = FastAPI(title="ClassBuddy: College Assistant")

# Include routers for each module
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(campus_map.router, prefix="/campus-map", tags=["Campus Map"])
app.include_router(academics.router, prefix="/academics", tags=["Academics"])
app.include_router(community.router, prefix="/community", tags=["Community"])
app.include_router(assistant.router, prefix="/assistant", tags=["AI Assistant"])

@app.get("/")
def root():
    return {"message": "Welcome to ClassBuddy!"}
