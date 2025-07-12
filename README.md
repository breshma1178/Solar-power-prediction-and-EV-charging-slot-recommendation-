# Solar-power-prediction-and-EV-charging-slot-recommendation-using AIML
# 🔆 Solar Power Prediction & EV Charging Slot Recommendation

##  Project Overview
This project predicts **solar radiation** using hourly weather data and recommends the best time slots to charge **Electric Vehicles (EVs)** efficiently.  
It uses **Machine Learning (Random Forest Regressor)** to forecast solar power and a simple threshold logic to advise charging time based on predicted availability.

---

## ⚙️ Tech Stack
- **Language:** Python  
- **Libraries:** Pandas, Scikit-Learn, Streamlit, Matplotlib, Seaborn, Joblib  
- **Model:** Random Forest Regressor  
- **Deployment:** Streamlit App

---

## 🗂️ Dataset
- **Source:** NASA POWER Point Hourly Data *(My Own Dataset Of A location at Central India (approx. 22°N, 77°E) Madhya Pradesh)*  
- **Duration:** Hourly data for the year 2023–2024 for a specific location.
- **Features Used:**
  - `ALLSKY_SFC_SW_DWN`: Solar radiation at surface
  - `T2M`: Temperature at 2 meters
  - `RH2M`: Relative Humidity at 2 meters
  - `ALLSKY_SFC_SW_DWN_lag1`, `lag2`: Lag features for time series pattern

---

##  Steps Involved

### 1️ Load Dataset
- Load `.xlsx` file.
- Inspect columns, shape, datatypes.
- Check for missing values.

### 2️ Data Preprocessing
- Drop or fill missing rows.
- Create lag features for time-series forecasting.

### 3️ Exploratory Data Analysis (EDA)
- Check unique values and counts for each column.
- Correlation heatmap.
- Pairplots for multivariate relationships.
- Boxplots for outlier detection.
- Distribution plots.

### 4️ Feature Engineering
- `lag1` and `lag2` created for solar radiation to capture past trends.

### 5️ Train/Test Split
- Split dataset (70% train, 30% test).
- Scale features using `StandardScaler`.

### 6️ Model Training
- Train **Random Forest Regressor**.
- Evaluate using:
  - RMSE
  - MAE
  - R² score

### 7️ Save Artifacts
- Save trained model: `rf_model.pkl`
- Save scaler: `scaler.pkl`

### 8️ Deploy with Streamlit
- Build a web app that:
  - Takes user input for lags, temperature, humidity.
  - Predicts solar radiation.
  - Recommends whether to charge EV based on threshold logic.
  - Shows time slot for charging.

### Results
- **RMSE:** ~31.04  
- **MAE:** ~17.10  
- **R² Score:** ~0.99  
#### These scores show the model fits well for this dataset and location.


## 🚀 How to Run
1. Clone this repo.
2. Install requirements: `pip install -r requirements.txt`
3. Run the Streamlit app:
   ```bash
   streamlit run solarapp.py

