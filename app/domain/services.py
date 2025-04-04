from app.domain.interfaces import IInsuranceService
from app.domain.entities import Car, Insurance
from app.utils.datetime_helpers import get_current_year
from app.config.config import (
    COVERAGE_PERCENTAGE,
    AGE_RATE_FACTOR,
    VALUE_RATE_STEP,
    VALUE_RATE_FACTOR
)


class InsuranceService(IInsuranceService):
    def calculate_insurance(self, car: Car, insurance: Insurance):
        current_year = get_current_year()
        age_rate = (current_year - car.year) * AGE_RATE_FACTOR
        value_rate = (car.value // VALUE_RATE_STEP) * VALUE_RATE_FACTOR
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
