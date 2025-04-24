from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_msg():
    return {"content": "Areas will be added!"}


@app.get("/year-endpoint")
async def year_info():
    return {"year": 2025}
