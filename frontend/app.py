import streamlit as st
import pandas as pd
import requests

#  page configuration
st.set_page_config(page_title="Loan Calculator", page_icon="💰", layout="centered")

# Logo & Title
st.image("logo.png", width=120)  
st.title("💰 Smart Loan Calculator")
st.markdown(
    "<h4 style='color:#00FFAA;'>Plan your loan smarter, faster, and with clarity.</h4>",
    unsafe_allow_html=True
)

#  Input Form 
with st.form("loan_form"):
    principal = st.number_input("Loan Amount (UGX)", min_value=0.0, format="%.2f")
    rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, format="%.2f")
    years = st.number_input("Loan Term (years)", min_value=1, format="%d")
    extra = st.number_input("Extra Monthly Payment (UGX)", min_value=0.0, format="%.2f")
    submit = st.form_submit_button("📊 Calculate Loan")

#  Results 
if submit:
    payload = {"principal": principal, "rate": rate, "years": years, "extra_payment": extra}

    r1 = requests.post("http://backend:8000/calculate", json=payload)
    r2 = requests.post("http://backend:8000/schedule", json=payload)

    if r1.status_code == 200 and r2.status_code == 200:
        monthly_payment = r1.json()["monthly_payment"]
        schedule = pd.DataFrame(r2.json())

        st.success(f"Estimated Monthly Payment: UGX {monthly_payment:,.2f}")
        
        # Show schedule 
        with st.expander("📅 Show Amortization Schedule"):
            st.dataframe(schedule.style.format({"Payment": "UGX {:.2f}", "Balance": "UGX {:.2f}"}))

        # CSV download 
        csv = schedule.to_csv(index=False).encode()
        st.download_button("⬇️ Download Schedule as CSV", data=csv, file_name="loan_schedule.csv", mime="text/csv")

        #  Charts 
        st.subheader("📈 Loan Balance Over Time")
        st.line_chart(schedule.set_index("Month")[["Balance"]])

        st.subheader("📊 Principal vs Interest")
        st.area_chart(schedule.set_index("Month")[["Principal", "Interest"]])
    else:
        st.error("Error communicating with backend. Please try again.")
