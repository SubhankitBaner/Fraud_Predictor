import streamlit as st 
import pandas as pd
import joblib
import time 
model = joblib.load("model/fraud_detection.pkl")
#st.title("Fraud Detection Predictor")
col1, col2 = st.columns([4, 6])
with col1:
    st.image("Images/fraudshield.png", width=230)
with col2:
    st.markdown("<h1 style='padding-top: 35px;'>FraudShield</h1>", unsafe_allow_html=True)
st.set_page_config(page_title="FraudShield", page_icon="🕵️", layout="centered")

st.divider()

st.write("Welcome to the FraudShield! This tool leverages machine learning to evaluate financial transactions and identify those that may be potentially fraudulent. By analyzing features such as transaction type, amount, and changes in account balances, the model assesses the risk of each transaction. Built on real-world transaction data, this app offers insights into fraud detection using AI, ideal for educational and demonstration purposes.")

st.sidebar.title("ℹ️ About This App")
st.sidebar.markdown("This application is designed to predict the likelihood of fraud in a financial transaction using key input features like transaction type, transaction amount, and sender/receiver account balances. It provides a real-time fraud risk assessment powered by a classification model trained on publicly available datasets.\n\n"

"\n\n Please note that this tool is intended solely for educational use and should not be relied upon for actual financial decisions.")

st.divider()

st.markdown("<h2 style='color:teal;'>Enter Transaction Details Below</h2>", unsafe_allow_html=True)

st.divider()


transaction_type=st.selectbox("Transaction Type",['PAYMENT','TRANSFER','CASH_OUT','CASH_IN','DEBIT'])
amount = st.number_input("Amount",min_value=0.0,value=1000.0)
oldbalanceOrg=st.number_input("Old Balance(Sender)",min_value=0.0,value=10000.0)
newbalanceOrig=st.number_input("New Balance(Sender)",min_value=0.0,value=9000.0)
oldbalanceDest=st.number_input("Old Balance(Reciever)",min_value=0.0,value=0.0)
newbalanceDest=st.number_input("New Balance(Reciever)",min_value=0.0,value=0.0)

input_df = pd.DataFrame([[transaction_type,amount,oldbalanceOrg, newbalanceOrig, oldbalanceDest,newbalanceDest]],
                        columns=['type','amount','oldbalanceOrg','newbalanceOrig','oldbalanceDest','newbalanceDest'])

if st.button("Predict"):
    with st.spinner('Predicting.....'):
            time.sleep(2)
            prediction = model.predict(input_df)[0]
            #st.subheader(f"Prediction : '{int(prediction)}'")
            if prediction ==1:
                st.error("⚠️This transaction has been flagged as potentially fraudulent based on model analysis.")
            else:
                st.success("✅This transaction appears to be legitimate based on the current model evaluation")
            st.markdown(
                    "<p style='font-size: 1.00em; color: #999;'>⚠️ This tool is for educational purposes only and may not reflect real-world fraud accurately.Do not use it for actual financial decisions or risk assessment.</p>",
                    unsafe_allow_html=True
                )

st.markdown("---")
st.markdown("Created with ❤️ by Subhankit (https://github.com/SubhankitBaner)")
