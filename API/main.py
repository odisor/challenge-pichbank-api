from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel, validator
import logging


app = FastAPI()

class Item(BaseModel):
    message: str
    to: str
    from_: str
    timeToLifeSec: int

    @validator("message")
    def message_check(cls, value):
        if value != "This is a test":
            raise ValueError("value != This is a test")
        return value
      
    @validator("to")
    def to_check(cls, value):
        if value != "Juan Perez":
            raise ValueError("value != Juan Perez")
        return value

    @validator("from_")
    def from_check(cls, value):
        if value != "Rita Asturia":
            raise ValueError("value != Rita Asturia")
        return value

    @validator("timeToLifeSec")
    def timeToLifeSec_check(cls, value):
        if int(value) != 45:
            raise ValueError("value != 45")
        return value        


@app.post("/DevOps/")
async def create_item(item: Item):
    try:
        item.validate(item.dict())
    except Exception as e:
        logging.error("Validation error: %s", str(e))
        raise HTTPException(status_code=400, detail="Invalid payload")
    return {'message': 'Hello Juan Perez your message will be send'}
