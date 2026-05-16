from fastapi import FastAPI

app = FastAPI(title="Ticket Agent")

@app.get("/")
def root():
    return {"message": "Ticket Agent is running"}
