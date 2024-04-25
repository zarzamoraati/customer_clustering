# from pydantic import Field,BaseModel,model_validator,field_validator,ValidationError
# from enum import Enum
# from typing import Tuple
# from decimal import Decimal



# class Client(BaseModel):
#     single:float
#     married:float
#     divorced:float
#     grade_education:float 
#     children:Decimal=Field(max_digits=2,decimal_places=1,ge=0.0)
#     incomes:Decimal=Field(ge=0.0)

#     @field_validator("single","married","divorced")
#     @classmethod
#     def validate_marital(cls, v:float) -> float:
#         if v not in [0.0,1.0]:
#             raise ValueError("Value mustbe 0.0 or 1.0. Nothing else")
        
#         return v
#     @field_validator("grade_education")
#     def grade(cls,v:float)->float:
#         if v not in [0.0,1.0,2.0]:
#             raise ValueError("Bad Request: Values for 'grade_education' only admit 0.0, 1.0, 2.0")
    
#         return v

# client={"single":0.0,"married":1.0,"divorced":1.0,"grade_education":2.0,"children":9.0,"incomes":20970.12}

# try:
#     parse_client=Client(**client)
#     print(parse_client)
# except ValidationError as e:
#     print(e)


import pickle 

print(pickle.load(open("./model/cluster_client_kmeans_neighbors.pkl","rb")))
