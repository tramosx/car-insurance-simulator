from app.domain.services import InsuranceService
from app.use_cases.insurance_use_case import InsuranceUseCase

def get_insurance_service():
    return InsuranceService()

def get_insurance_use_case() -> InsuranceUseCase:
    insurance_service = get_insurance_service()
    return InsuranceUseCase(get_insurance_service())
