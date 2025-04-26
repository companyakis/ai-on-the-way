from fastapi import FastAPI, Body

app = FastAPI()

UNITS = [
    {"id": "1", "area": "FinTech", "manager": "Mustafa Buyukdereli", "number of employees": 12, "location": "x city"},
    {"id": "2", "area": "Sales", "manager": "Aygun Arslan", "number of employees": 7, "location": "istanbul"},
    {"id": "6", "area": "Marketing", "manager": "Bilge Kağan", "number of employees": 4, "location": "istanbul"},
    {"id": "8", "area": "Finance", "manager": "Bengü Bilici", "number of employees": 3, "location": "istanbul"},
    {"id": "3", "area": "Operations", "manager": "Kutluk Gokturk", "number of employees": 3, "location": "x city"},
    {"id": "5", "area": "Audit", "manager": "Kultigin Yapici", "number of employees": 2, "location": "x city"},
]

@app.get("/departments")
async def company_units():
    return UNITS


# add a new department

@app.post("/add-new-unit")
async def add_new_department(new_dep = Body()):
    UNITS.append(new_dep)

