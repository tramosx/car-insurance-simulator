from app.api.schemas import InsuranceRequestDTO, CarDTO, InsuranceParametersDTO

def test_use_case_execution(insurance_use_case):
    request = InsuranceRequestDTO(
        car=CarDTO(make="Toyota", model="Corolla", year=2010, value=50000),
        insurance=InsuranceParametersDTO(deductible_percentage=0.2, broker_fee=80)
    )

    result = insurance_use_case.execute(request)
    assert result.calculated_premium > 0
    assert result.policy_limit > 0
