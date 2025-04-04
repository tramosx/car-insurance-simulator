from app.domain.entities import Car, Insurance
from app.domain.services import InsuranceService


def test_calculate_insurance_basic(insurance_service):
    car = Car(make="Honda", model="Civic", year=2015, value=60000)
    insurance = Insurance(deductible_percentage=0.1, broker_fee=100)

    service = InsuranceService()
    result = service.calculate_insurance(car, insurance)

    assert result["applied_rate"] > 0
    assert result["deductible_value"] == 6000 


def test_calculate_insurance_full_deductible():
    car = Car(make="BMW", model="X5", year=2019, value=200000)
    insurance = Insurance(deductible_percentage=1.0, broker_fee=500)

    service = InsuranceService()
    result = service.calculate_insurance(car, insurance)

    assert result["deductible_value"] == 200000