from fastapi import FastAPI

app = FastAPI(
    title="PulseIQ API",
    description="AI-powered Decision Intelligence Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to PulseIQ 🚀"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }