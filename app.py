import streamlit as st
import pandas as pd
import numpy as np

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Churn Prediction System",
    page_icon="📊",
    layout="wide"
)

# ==============================
# CUSTOM CSS
# ==============================
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #1f4e79;
}
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #555;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.result-yes {
    color: red;
    font-size: 22px;
    font-weight: bold;
}
.result-no {
    color: green;
    font-size: 22px;
    font-weight: bold;
}
.footer {
    background-color: #1f4e79;
    padding: 25px;
    border-radius: 12px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# TITLE
# ==============================
st.markdown("<div class='main-title'>Customer Churn Prediction</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Predict whether a customer is likely to churn (Yes / No)</div>", unsafe_allow_html=True)
st.markdown("---")

# ==============================
# TABS
# ==============================
tab1, tab2 = st.tabs(["🔍 Individual Prediction", "📁 Bulk Prediction"])

# ==============================
# TAB 1: INDIVIDUAL PREDICTION
# ==============================
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Individual Customer Details")

    col1, col2 = st.columns(2)

    with col1:
        tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)
        monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
        total_charges = st.number_input("Total Charges", min_value=0.0, value=840.0)

    with col2:
        contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
        internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

    if st.button("Predict Churn"):
        # ---- Dummy prediction logic (replace with model.predict) ----
        churn_prediction = np.random.choice(["Yes", "No"])

        if churn_prediction == "Yes":
            st.markdown("<p class='result-yes'>🔴 Churn Prediction: YES</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='result-no'>🟢 Churn Prediction: NO</p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# TAB 2: BULK PREDICTION
# ==============================
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Bulk Customer Churn Prediction")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("📄 Uploaded Dataset Preview:")
        st.dataframe(df.head())

        if st.button("Run Bulk Prediction"):
            # ---- Dummy predictions (replace with model.predict) ----
            df["Churn Prediction"] = np.random.choice(["Yes", "No"], size=len(df))

            st.success("Bulk churn prediction completed!")
            st.dataframe(df)

            st.download_button(
                label="📥 Download Predictions",
                data=df.to_csv(index=False),
                file_name="churn_predictions.csv",
                mime="text/csv"
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# BUSINESS IMPACT SECTION
# ==============================
st.markdown("---")
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.subheader("📈 Business Impact of Churn Prediction")

st.markdown("""
1. **Reduction in customer churn rates** by proactively addressing risks.  
2. **Enhanced customer loyalty** through data-driven engagement strategies.  
3. **Optimized retention costs** by prioritizing critical customer segments.  
4. **Long-term business growth** through improved customer retention strategies.
""")

st.markdown("</div>", unsafe_allow_html=True)
