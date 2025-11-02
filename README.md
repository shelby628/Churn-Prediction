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

```bash
cd "Churn Prediction"
```


3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:


```
bash streamlit run app.py
```
<img width="748" height="439" alt="customer churn" src="https://github.com/user-attachments/assets/50ef96fb-cc6d-4fcc-9b80-1fe697423e4e" />

<img width="560" height="360" alt="customer churn 2" src="https://github.com/user-attachments/assets/c8def762-7a11-4031-9e5b-6e148552912c" />

