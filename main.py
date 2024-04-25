from pydantic import Field,BaseModel,model_validator,field_validator
from fastapi import FastAPI
from typing import Literal
from decimal import Decimal
import pickle

class Client(BaseModel):
    Spent:float=Field(ge=0.0)
    Age:float=Field(ge=0.0)
    Income:Decimal=Field(ge=0.0)
    Children:Decimal=Field(max_digits=2,decimal_places=1,ge=0.0)
    NumWebVisitsMonth:float=Field(ge=0.0) 
    NumWebPurchases:float=Field(ge=0.0)
    NumCatalogPurchases:float=Field(ge=0.0)
    NumStorePurchases:float=Field(ge=0.0)
    Education_Label:float
    Marital_Status_Divorced:float
    Marital_Status_Married:float
    Marital_Status_Single:float
  

    @field_validator("Marital_Status_Single","Marital_Status_Married","Marital_Status_Divorced")
    @classmethod
    def validate_marital(cls, v:float) -> float:
        if v not in [0.0,1.0]:
            raise ValueError("Value mustbe 0.0 or 1.0. Nothing else")
        
        return v
    @field_validator("Education_Label")
    def grade(cls,v:float)->float:
        if v not in [0.0,1.0,2.0]:
            raise ValueError("Bad Request: Values for 'grade_education' only admit 0.0, 1.0, 2.0")
    
        return v
    


app=FastAPI()

@app.get("/")
def home():
    return {"msg":"hello"}

@app.post("/v1/clients")
def fetch_inference(client:Client):
    values=[]
    client_dic=client.model_dump()
    for value in client_dic.values():
       values.append(value)
    model=pickle.load(open("./model/cluster_client_kmeans_neighbors.pkl","rb"))
    id2_labels={0:"high_spend",1:"very_low_spend",2:"low_spend",3:"moderate_spend",4:"very_high_spend"}
    id_predict=model.predict([values])
    return id2_labels[id_predict[0]]


    
        