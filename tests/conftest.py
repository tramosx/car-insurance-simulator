import pytest
from fastapi.testclient import TestClient
from main import app
from app.domain.services import InsuranceService
from app.use_cases.insurance_use_case import InsuranceUseCase


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def insurance_service():
    return InsuranceService()


@pytest.fixture
def insurance_use_case(insurance_service):
    return InsuranceUseCase(insurance_service)
