# === BACKEND: backend/main.py ===
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class LoanInput(BaseModel):
    principal: float
    rate: float
    years: int
    extra_payment: float = 0.0

@app.post("/calculate")
def calculate_loan(data: LoanInput):
    monthly_rate = data.rate / 100 / 12
    months = data.years * 12
    monthly_payment = (
        data.principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    )
    return {"monthly_payment": round(monthly_payment, 2)}

@app.post("/schedule")
def amortization_schedule(data: LoanInput):
    monthly_rate = data.rate / 100 / 12
    months = data.years * 12
    monthly_payment = (
        data.principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)
    )
    monthly_payment += data.extra_payment

    balance = data.principal
    schedule = []
    month = 0

    while balance > 0:
        month += 1
        interest = balance * monthly_rate
        principal_payment = monthly_payment - interest
        if balance < monthly_payment:
            principal_payment = balance
            monthly_payment = principal_payment + interest
        balance -= principal_payment
        schedule.append({
            "Month": month,
            "Payment": round(monthly_payment, 2),
            "Principal": round(principal_payment, 2),
            "Interest": round(interest, 2),
            "Balance": round(balance, 2)
        })

    df = pd.DataFrame(schedule)
    return df.to_dict(orient="records")
