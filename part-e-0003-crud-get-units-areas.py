from fastapi import FastAPI

app = FastAPI()

AREAS = [
    {"area": "FinTech", "manager": "Mustafa Buyukdereli", "number of employees": 12},
    {"area": "Sales", "manager": "Aygun Arslan", "number of employees": 7},
    {"area": "Marketing", "manager": "Bilge Kağan", "number of employees": 4},
    {"area": "Finance", "manager": "Bengü Bilici", "number of employees": 3},
    {"area": "Operations", "manager": "Kutluk Gokturk", "number of employees": 3},
    {"area": "Audit", "manager": "Kultigin Yapici", "number of employees": 2},
]

@app.get("/departments")
async def company_units():
    return AREAS
