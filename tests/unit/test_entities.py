import pytest
from app.domain.entities import Car, Insurance

def test_car_creation():
    car = Car(make="Toyota", model="Corolla", year=2025, value=80000.0)
    
    assert car.make == "Toyota"
    assert car.model == "Corolla"
    assert car.year == 2025
    assert car.value == 80000.0

def test_insurance_creation():
    insurance = Insurance(deductible_percentage=0.1, broker_fee=150.0)
    
    assert insurance.deductible_percentage == 0.1
    assert insurance.broker_fee == 150.0
