from fastapi import FastAPI

app = FastAPI()

UNITS = [
    {"id": "1", "area": "FinTech", "manager": "Mustafa Buyukdereli", "number of employees": 12},
    {"id": "2", "area": "Sales", "manager": "Aygun Arslan", "number of employees": 7},
    {"id": "6", "area": "Marketing", "manager": "Bilge Kağan", "number of employees": 4},
    {"id": "8", "area": "Finance", "manager": "Bengü Bilici", "number of employees": 3},
    {"id": "3", "area": "Operations", "manager": "Kutluk Gokturk", "number of employees": 3},
    {"id": "5", "area": "Audit", "manager": "Kultigin Yapici", "number of employees": 2},
]

@app.get("/departments")
async def company_units():
    return UNITS

# @app.get("/departments/{dep_id}")
# async def return_department_by_id(dep_id: str):
#     for unit in UNITS:
#         if unit["id"].casefold() == dep_id.casefold():
#             return unit
        
@app.get("/departments/{manager}")
async def get_department_by_manager(manager: str):
    for unit in UNITS:
        if unit["manager"].casefold() == manager.casefold():
            return unit
