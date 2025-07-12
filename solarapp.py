import streamlit as st
import joblib
from datetime import datetime, timedelta

# Load trained model & scaler
rf_model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🔆 Solar Power Prediction & EV Charging Advice")

# Inputs for prediction
ALLSKY_SFC_SW_DWN_lag1 = st.number_input("ALLSKY_SFC_SW_DWN_lag1")
ALLSKY_SFC_SW_DWN_lag2 = st.number_input("ALLSKY_SFC_SW_DWN_lag2")
T2M = st.number_input("Temperature at 2m")
RH2M = st.number_input("Relative Humidity at 2m")

# Optional: input current time for realistic prediction window
current_time = st.time_input("Current Hour", value=datetime.now().time())

if st.button("Predict"):
    X_new = [[ALLSKY_SFC_SW_DWN_lag1, ALLSKY_SFC_SW_DWN_lag2, T2M, RH2M]]
    X_new_scaled = scaler.transform(X_new)
    y_pred = rf_model.predict(X_new_scaled)
    predicted_power = y_pred[0]

    st.write(f"🔆 **Predicted Solar Radiation:** {predicted_power:.2f} W/m²")

    # Charging recommendation logic
    threshold = 0.7 * 1000  # Example: 70% of max possible radiation

    # Calculate recommended time slot
    now = datetime.combine(datetime.today(), current_time)
    next_slot = now + timedelta(hours=1)
    next_slot_str = next_slot.strftime("%Y-%m-%d %H:%M")

    if predicted_power > threshold:
        st.success(f" Good time to charge your Electric Vehicle!")
        st.success(f" Recommended next slot:{next_slot_str}")
    else:
        st.warning(f" Not Recommended to charge your Electric Vehicle!")
        st.warning(f" Next slot:{next_slot_str}")
