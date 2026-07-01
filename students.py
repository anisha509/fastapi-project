from fastapi import FastAPI
app = FastAPI()
students = [
    {"id": 1 , "Name": "Annie"},
    {"id": 2 , "Name": "Leo"}
]
@app.get("/students")
def get_students():
    return students
