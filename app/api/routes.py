from fastapi import APIRouter, Depends
from app.api.schemas import InsuranceRequestDTO, InsuranceResultDTO
from app.use_cases.insurance_use_case import InsuranceUseCase
from app.config.dependencies import get_insurance_use_case


router = APIRouter()

@router.post("/calculate", response_model=InsuranceResultDTO)
def calculate(
    request: InsuranceRequestDTO, 
    insurance_use_case: InsuranceUseCase = Depends(get_insurance_use_case)
):
    return insurance_use_case.execute(request)