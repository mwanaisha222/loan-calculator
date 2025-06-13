from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanInput(BaseModel):
    principal: float
    rate: float  # Annual interest rate in percent
    years: int

@app.post("/calculate")
def calculate_loan(data: LoanInput):
    monthly_rate = data.rate / 100 / 12
    months = data.years * 12
    monthly_payment = (
        data.principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    )
    return {"monthly_payment": round(monthly_payment, 2)}
