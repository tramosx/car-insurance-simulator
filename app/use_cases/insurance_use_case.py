from app.domain.entities import Car, Insurance
from app.domain.interfaces import IInsuranceService
from app.api.schemas import InsuranceRequestDTO, InsuranceResultDTO, CarDTO

class InsuranceUseCase:
    def __init__(self, insurance_service: IInsuranceService):
        self.insurance_service = insurance_service

    def execute(self, request: InsuranceRequestDTO) -> InsuranceResultDTO:
        car = Car(**request.car.dict())
        insurance = Insurance(**request.insurance.dict())

        result = self.insurance_service.calculate_insurance(car, insurance)

        return InsuranceResultDTO(
            car=CarDTO(**result["car"].__dict__),
            applied_rate=result["applied_rate"],
            policy_limit=result["policy_limit"],
            calculated_premium=result["calculated_premium"],
            deductible_value=result["deductible_value"],
        )
