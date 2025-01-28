import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load your pre-trained model
model = joblib.load('C:/Users/HP/OneDrive/Documents/DS_data/models/model.pkl')   # Replace with your actual model path

# Function to make predictions
def predict(input_data):
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.title("Employee Attrition Prediction")
st.write("This app predicts employee attrition based on various features.")

# Input fields for continuous features (scaled)
age = st.number_input("Age")
daily_rate = st.number_input("Daily Rate")
distance_from_home = st.number_input("Distance From Home (miles)")
hourly_rate = st.number_input("Hourly Rate")
monthly_income = st.number_input("Monthly Income")
monthly_rate = st.number_input("Monthly Rate")
num_companies_worked = st.number_input("Number of Companies Worked")
percent_salary_hike = st.number_input("Percent Salary Hike")
total_working_years = st.number_input("Total Working Years")
training_times_last_year = st.number_input("Training Times Last Year")
years_at_company = st.number_input("Years at Company")
years_in_current_role = st.number_input("Years in Current Role")
years_since_last_promotion = st.number_input("Years Since Last Promotion")
years_with_curr_manager = st.number_input("Years with Current Manager")

# Dummy variable inputs
overtime = st.selectbox("Overtime", ["No", "Yes"])
job_role = st.selectbox("Job Role", [
    "HumanResources",
    "LaboratoryTechnician",
    "Manager",
    "ManufacturingDirector",
    "ResearchDirector",
    "ResearchScientist",
    "SalesExecutive",
    "SalesRepresentative"
    "HealthcareRepresentative"
])
job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
stock_option_level = st.selectbox("Stock Option Level", [0, 1, 2, 3])
marital_status = st.selectbox("Marital Status", ["Divorced", "Married", "Single"])
job_involvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
business_travel = st.selectbox("Business Travel", ["Travel_Frequently", "Travel_Rarely", "Non-Travel"])
environment_satisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
job_satisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
work_life_balance = st.selectbox("Work Life Balance", [1, 2, 3, 4])
department = st.selectbox("Department", ["HumanResources", "Research&Development", "Sales"])
education_field = st.selectbox("Education Field", [
    "LifeSciences",
    "Marketing",
    "Medical",
    "Other",
    "TechnicalDegree",
    "HumanResources"
])

# Prepare the input data for prediction
input_data = {
    'Age': age,
    'DailyRate': daily_rate,
    'DistanceFromHome': distance_from_home,
    'HourlyRate': hourly_rate,
    'MonthlyIncome': monthly_income,
    'MonthlyRate': monthly_rate,
    'NumCompaniesWorked': num_companies_worked,
    'PercentSalaryHike': percent_salary_hike,
    'TotalWorkingYears': total_working_years,
    'TrainingTimesLastYear': training_times_last_year,
    'YearsAtCompany': years_at_company,
    'YearsInCurrentRole': years_in_current_role,
    'YearsSinceLastPromotion': years_since_last_promotion,
    'YearsWithCurrManager': years_with_curr_manager,
    
    # Dummy variables encoded as per selection
    'OverTime_No': 1 if overtime == "No" else 0,
    'OverTime_Yes': 1 if overtime == "Yes" else 0,

    
    # Job Role encoding
     
    'JobRole_HealthcareRepresentative': 1 if job_role == "HealthcareRepresentative" else 0,
    'JobRole_HumanResources': 1 if job_role == "HumanResources" else 0,
    'JobRole_LaboratoryTechnician': 1 if job_role == "LaboratoryTechnician" else 0,
    'JobRole_Manager': 1 if job_role == "Manager" else 0,
    'JobRole_ManufacturingDirector': 1 if job_role == "ManufacturingDirector" else 0,
    'JobRole_ResearchDirector': 1 if job_role == "ResearchDirector" else 0,
    'JobRole_ResearchScientist': 1 if job_role == "ResearchScientist" else 0,
    'JobRole_SalesExecutive': 1 if job_role == "SalesExecutive" else 0,
    'JobRole_SalesRepresentative': 1 if job_role == "SalesRepresentative" else 0,

    # Job Level encoding
    
    'JobLevel_1': 1 if job_level == 1 else 0,
    'JobLevel_2': 1 if job_level == 2 else 0,
    'JobLevel_3': 1 if job_level == 3 else 0,
    'JobLevel_4': 1 if job_level == 4 else 0,
    'JobLevel_5': 1 if job_level == 5 else 0,

    # Stock Option Level encoding   
    
    'StockOptionLevel_0': 1 if stock_option_level == 0 else 0,
    'StockOptionLevel_1': 1 if stock_option_level == 1 else 0,
    'StockOptionLevel_2': 1 if stock_option_level == 2 else 0,
    'StockOptionLevel_3': 1 if stock_option_level == 3 else 0,

    # Marital Status encoding
    
    'MaritalStatus_Divorced': 1 if marital_status == "Divorced" else 0,
    'MaritalStatus_Married': 1 if marital_status == "Married" else 0,
    'MaritalStatus_Single': 1 if marital_status == "Single" else 0,

    # Job Involvement encoding
    
    'JobInvolvement_1': 1 if job_involvement == 1 else 0,
    'JobInvolvement_2': 1 if job_involvement == 2 else 0,
    'JobInvolvement_3': 1 if job_involvement == 3 else 0,
    'JobInvolvement_4': 1 if job_involvement == 4 else 0,

    # Business Travel encoding
    'BusinessTravel_Non-Travel': 1 if business_travel == "Non-Travel" else 0,
    'BusinessTravel_Travel_Frequently': 1 if business_travel == "Travel_Frequently" else 0,
    'BusinessTravel_Travel_Rarely': 1 if business_travel == "Travel_Rarely" else 0,
   


    # Environment Satisfaction encoding
     
    'EnvironmentSatisfaction_1': 1 if environment_satisfaction == 1 else 0,
    'EnvironmentSatisfaction_2': 1 if environment_satisfaction == 2 else 0,
    'EnvironmentSatisfaction_3': 1 if environment_satisfaction == 3 else 0,
    'EnvironmentSatisfaction_4': 1 if environment_satisfaction == 4 else 0,

    # Job Satisfaction encoding
     
    'JobSatisfaction_1': 1 if job_satisfaction == 1 else 0,
    'JobSatisfaction_2': 1 if job_satisfaction == 2 else 0,
    'JobSatisfaction_3': 1 if job_satisfaction == 3 else 0,
    'JobSatisfaction_4': 1 if job_satisfaction == 4 else 0,

    # Work Life Balance encoding
     
    'WorkLifeBalance_1': 1 if work_life_balance == 1 else 0,
    'WorkLifeBalance_2': 1 if work_life_balance == 2 else 0,
    'WorkLifeBalance_3': 1 if work_life_balance == 3 else 0,
    'WorkLifeBalance_4': 1 if work_life_balance == 4 else 0,

    # Department encoding
     
    'Department_HumanResources': 1 if department == "HumanResources" else 0,
    'Department_Research&Development': 1 if department == "Research&Development" else 0,
    'Department_Sales': 1 if department == "Sales" else 0,

    # Education Field encoding
    
    'EducationField_HumanResources': 1 if education_field == "HumanResources" else 0,
    'EducationField_LifeSciences': 1 if education_field == "LifeSciences" else 0,
    'EducationField_Marketing': 1 if education_field == "Marketing" else 0,
    'EducationField_Medical': 1 if education_field == "Medical" else 0,
    'EducationField_Other': 1 if education_field == "Other" else 0,
    'EducationField_TechnicalDegree': 1 if education_field == "TechnicalDegree" else 0,
}

# Convert input data to DataFrame for prediction
input_df = pd.DataFrame(input_data, index=[0])

if st.button("Predict"):
    prediction = predict(input_df)
    
    # Display the prediction result
    st.write(f"Prediction: {'Employee will leave' if prediction == 1 else 'Employee will stay'}")
