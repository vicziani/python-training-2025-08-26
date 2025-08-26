from fastapi import FastAPI
from datetime import datetime


from pydantic import BaseModel, Field
from typing import Union

from app import service

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")
app = FastAPI()


class Employee(BaseModel):
    id: Union[int, None] = None
    name: str = Field(min_length=1, max_length=255)


@app.get("/api/status")
def info():
    return {"status": "on", "time": str(datetime.now())}


@app.get("/api/employees")
def list_employees() -> list[Employee]:
    logging.info("List employees")
    return [Employee(**e) for e in service.list_employees()]


@app.post("/api/employees")
def save_employee(employee: Employee) -> Employee:
    logging.info(f"Create employee: {employee.name}")
    d = employee.model_dump()
    result = service.save_employee(d)
    return Employee(**result)
