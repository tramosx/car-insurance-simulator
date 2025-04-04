from abc import ABC, abstractmethod
from app.domain.entities import Car, Insurance

class IInsuranceService(ABC):
    @abstractmethod
    def calculate_insurance(self, car: Car, insurance: Insurance):
        pass