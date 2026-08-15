from fastapi import FastAPI


app = FastAPI(
    title="HireCraft API",
    version="1.0.0",
    description="AI-powered career optimization platform"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to HireCraft API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }