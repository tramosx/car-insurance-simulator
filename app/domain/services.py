from app.domain.interfaces import IInsuranceService
from app.config.config import COVERAGE_PERCENTAGE, CURRENT_YEAR
from app.domain.entities import Car, Insurance


class InsuranceService(IInsuranceService):
    def calculate_insurance(self, car: Car, insurance: Insurance):
        age_rate = (CURRENT_YEAR - car.year) * 0.005
        value_rate = (car.value // 10000) * 0.005
        applied_rate = age_rate + value_rate

        base_premium = car.value * applied_rate
        deductible_discount = base_premium * insurance.deductible_percentage
        final_premium = base_premium - deductible_discount + insurance.broker_fee

        base_policy_limit = car.value * COVERAGE_PERCENTAGE
        deductible_value = base_policy_limit * insurance.deductible_percentage
        final_policy_limit = base_policy_limit - deductible_value

        return {
            "car": car,
            "applied_rate": applied_rate,
            "policy_limit": final_policy_limit,
            "calculated_premium": final_premium,
            "deductible_value": deductible_value
        }
