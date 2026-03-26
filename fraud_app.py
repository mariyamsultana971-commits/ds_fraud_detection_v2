import streamlit as st
import pandas as pd
import joblib

# Load your model
model = joblib.load('fraud_detection_model.pkl')

st.title("🛡️ Fraud Detection AI")

# Input fields for the user
amt = st.number_input("Amount", value=100.0)
old_bal = st.number_input("Sender Old Balance", value=100.0)
new_bal = st.number_input("Sender New Balance", value=0.0)
type_select = st.selectbox("Type", ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])

if st.button("Predict"):
    # Create the data row (matching your 10-feature X_train)
    # Based on your screenshots, we need to match the 'step' and 'type' columns
    data = pd.DataFrame([[1, amt, old_bal, new_bal, 0, 0, 
                         1 if type_select == 'CASH_OUT' else 0,
                         1 if type_select == 'DEBIT' else 0,
                         1 if type_select == 'PAYMENT' else 0,
                         1 if type_select == 'TRANSFER' else 0]], 
                       columns=['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 
                                'oldbalanceDest', 'newbalanceDest', 'type_CASH_OUT', 
                                'type_DEBIT', 'type_PAYMENT', 'type_TRANSFER'])
    
    result = model.predict(data)
    if result[0] == 1:
        st.error("Fraud Detected!")
    else:
        st.success("Transaction Safe")