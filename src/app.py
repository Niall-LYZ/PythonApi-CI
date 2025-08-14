from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, DevSecOps!"}


@app.get("/health")
def health():
    return {"status": "healthy"}
