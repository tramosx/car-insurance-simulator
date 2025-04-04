import os
from dotenv import load_dotenv

load_dotenv()

COVERAGE_PERCENTAGE = float(os.getenv("COVERAGE_PERCENTAGE", 1.0))
CURRENT_YEAR = int(os.getenv("CURRENT_YEAR", 2024))
