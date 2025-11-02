#  Customer Churn Prediction App

This project is a **Machine Learning web application** built using **Streamlit** that predicts whether a customer is likely to **churn** (leave) or **stay** based on their demographic and account information.

---

 ##  Features
- Interactive **Streamlit web interface** for user input  
- Real-time churn prediction using a trained **Machine Learning model**  
- Model built and trained using **Scikit-learn**  
- User-friendly design with clear results and balloon animation on prediction 🎈

---

##  Tech Stack
- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **Streamlit**
- **Joblib**

---

##  Model Details
- **Algorithm:** Logistic Regression (or whichever model you used)
- **Features Used:**
  - `Age`
  - `Gender` (1 = Female, 0 = Male)
  - `MonthlyCharges`
  - `Tenure`
- **Output:**  
  - `1` → Customer will churn  
  - `0` → Customer will not churn  

---

##  How to Run the App Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/shelby628/Churn-Prediction.git


2. Navigate to the project directory:

cd "Churn Prediction"


3. Install dependencies:

pip install -r requirements.txt


4. Run the Streamlit app:

streamlit run app.py
