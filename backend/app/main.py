from fastapi import FastAPI

app = FastAPI(title="Product AI Assistant API")


@app.get("/")
def read_root():
    return {"message": "Product AI Assistant API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
