from pydantic import BaseModel
from typing import Annotated

class CarDTO(BaseModel):
    make: str
    model: str
    year: int
    value: float

class InsuranceParametersDTO(BaseModel):
    deductible_percentage: float
    broker_fee: float

class InsuranceRequestDTO(BaseModel):
    car: CarDTO
    insurance: InsuranceParametersDTO

class InsuranceResultDTO(BaseModel):
    car: CarDTO
    applied_rate: float
    policy_limit: float
    calculated_premium: float
    deductible_value: float
