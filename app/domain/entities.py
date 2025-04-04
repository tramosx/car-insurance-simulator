class Car:
    def __init__(self, make: str, model: str, year: int, value: float):
        self.make = make
        self.model = model
        self.year = year
        self.value = value

class Insurance:
    def __init__(self, deductible_percentage: float, broker_fee: float):
        self.deductible_percentage = deductible_percentage
        self.broker_fee = broker_fee
