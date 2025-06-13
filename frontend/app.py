import streamlit as st
import requests

st.title("Loan Calculator")

principal = st.number_input("Loan Amount", min_value=0.0, format="%.2f")
rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, format="%.2f")
years = st.number_input("Loan Term (years)", min_value=1, format="%d")

if st.button("Calculate"):
    response = requests.post(
        "http://backend:8000/calculate",  # This URL works in Docker
        json={"principal": principal, "rate": rate, "years": years}
    )
    if response.status_code == 200:
        result = response.json()
        st.success(f"Monthly Payment: ${result['monthly_payment']}")
    else:
        st.error("Error calculating loan.")
