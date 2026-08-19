from fastapi import FastAPI
from app.api.routes import router
from app.scheduler import start_scheduler

app = FastAPI(title="AI LinkedIn Daily Post Agent", version="1.0.0")
app.include_router(router, prefix="/api")

@app.on_event("startup")
def startup_event():
    start_scheduler()

@app.get("/health")
def health():
    return {"status": "ok"}
