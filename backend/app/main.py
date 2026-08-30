from fastapi import FastAPI

from app.routers.analysis import router as analysis_router

from fastapi.middleware.cors import CORSMiddleware

from app.routers.linkedin import router as linkedin_router

app = FastAPI(
    title="HireCraft API",
    version="1.0.0",
    description="AI-powered career optimization platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis_router)
app.include_router(linkedin_router)


@app.get("/")
def root():
    return {
        "message": "HireCraft API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }