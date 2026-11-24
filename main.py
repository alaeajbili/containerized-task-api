from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, DevOps!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
