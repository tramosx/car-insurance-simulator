import os
from dotenv import load_dotenv

load_dotenv()

COVERAGE_PERCENTAGE = float(os.getenv("COVERAGE_PERCENTAGE", 1.0))
AGE_RATE_FACTOR = float(os.getenv("AGE_RATE_FACTOR", 0.005))
VALUE_RATE_STEP = int(os.getenv("VALUE_RATE_STEP", 10000))
VALUE_RATE_FACTOR = float(os.getenv("VALUE_RATE_FACTOR", 0.005))
