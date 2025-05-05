from fastapi import FastAPI

app = FastAPI()

UNITS = {
    
    101: {"area": "FinTech", "manager": "Mustafa Buyukdereli", "number of employees": 12, "location": "x city"},
    321 : {"area": "Sales", "manager": "Aygun Arslan", "number of employees": 7, "location": "istanbul"},
    122: {"area": "Marketing", "manager": "Bilge Kağan", "number of employees": 4, "location": "istanbul"},
    712: {"area": "Finance", "manager": "Bengü Bilici", "number of employees": 3, "location": "istanbul"},
    543: {"area": "Operations", "manager": "Kutluk Gokturk", "number of employees": 3, "location": "x city"},
    661: {"area": "Audit", "manager": "Kultigin Yapici", "number of employees": 2, "location": "x city"},
}
    

@app.get("/departments")
async def company_units():
    return UNITS


@app.get("/departments/{id}")
async def get_dep_by_id(id: int):
    
    department = UNITS.get(id)
    
    if department is None:
        
        return {"error": "The department not found"}, 404
    
    return department



