from fastapi import FastAPI
app = FastAPI(title="ToBox Service", version="0.1.0")


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to ToBox Service"}


@app.get("/hello")
async def hello():
    """Simple hello endpoint"""
    return {"message": "Hello, World!"}


@app.get("/hello/{name}")
async def hello_name(name: str):
    """Hello endpoint with name parameter"""
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
