from fastapi import FastAPI

app = FastAPI(
    title="Twitter Clone API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "ok"}
