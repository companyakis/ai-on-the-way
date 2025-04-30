from fastapi import FastAPI, Body

app = FastAPI()

UNITS = [
    {"id": "1A", "area": "FinTech", "manager": "Mustafa Buyukdereli", "number of employees": 12, "location": "x city"},
    {"id": "2Xy", "area": "Sales", "manager": "Aygun Arslan", "number of employees": 7, "location": "istanbul"},
    {"id": "6BC", "area": "Marketing", "manager": "Bilge Kağan", "number of employees": 4, "location": "istanbul"},
    {"id": "8Ky", "area": "Finance", "manager": "Bengü Bilici", "number of employees": 3, "location": "istanbul"},
    {"id": "3AQ", "area": "Operations", "manager": "Kutluk Gokturk", "number of employees": 3, "location": "x city"},
    {"id": "5uYh", "area": "Audit", "manager": "Kultigin Yapici", "number of employees": 2, "location": "x city"},
]

@app.get("/departments")
async def company_units():
    return UNITS

# delete a unit by id

@app.delete("/delete_unit/{id}")
async def delete_dep_by_id(id: str):
    for i in range(len(UNITS)):
        if UNITS[i]["id"].casefold() == id.casefold():
            del UNITS[i]
            break 

# update a department by id num 

@app.put("/update-department")
async def update_a_dep(updated_dep = Body()):
    for i in range(len(UNITS)):
        if UNITS[i]["id"].casefold() == updated_dep["id"].casefold():
            UNITS[i] = updated_dep


# add a new department

@app.post("/add-new-unit")
async def add_new_department(new_dep = Body()):
    UNITS.append(new_dep)

