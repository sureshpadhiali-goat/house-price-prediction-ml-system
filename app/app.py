import streamlit as st
import requests

st.title("🏠 House Price Prediction")

st.write("Enter house details below:")

# Inputs (keep simple first)
overall_qual = st.number_input("Overall Quality (1-10)", min_value=1, max_value=10, value=5)
gr_liv_area = st.number_input("Living Area (sq ft)", value=1500)
garage_cars = st.number_input("Garage Capacity", value=2)
total_bsmt_sf = st.number_input("Basement Area", value=800)

# Button
if st.button("Predict Price"):
    
    data = {
        "data": {
            "OverallQual": overall_qual,
            "GrLivArea": gr_liv_area,
            "GarageCars": garage_cars,
            "TotalBsmtSF": total_bsmt_sf
        }
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        result = response.json()

        if "predicted_price" in result:
            st.success(f"Predicted Price: ₹ {result['predicted_price']:.2f}")
        else:
            st.error(result)

    except Exception as e:
        st.error(f"Error connecting to API: {e}")