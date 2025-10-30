# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age: int

# def hello(input:User):
#     return f"Hello {input.name} with age of {input.age}"

# # m = User(
# #     name = "sajeel",
# #     age = 24
# # )

# # m = {
# #     "name": "sajeel",
# #     "age": 24
# # }

# # print(hello(m))



# # ===============

# # Api End Point

# from fastapi import FastAPI

# # app

# app = FastAPI()

# # Endpoint ( Get / Post )

# @app.post("/get_info")
# def hello(input:User):
#     return f"Hello {input.name} with age of {input.age}"

from predict import prediction


from pydantic import BaseModel
class Person(BaseModel):
    Genre:str
    Age:int
    Annual_Income:int
    Spending_Score:int
def Hi(input:Person):
    return f"Hi {input.Genre} your  Age  is {input:Age} and your Spending Score is {input:Annual_Income} and your Spending Score is {input:Spending_Score}"
from fastapi import FastAPI
app = FastAPI()
@app.post("/get info")
def Hi(input:Person):
    #  data = ["Male", 24, 100000, 80]
    data = [input.Genre, input.Age, input.Annual_Income, input.Spending_Score]
    output = prediction(data)
    return {
        "output": int(output[0])
    } 

