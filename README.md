🚲 Bike Sharing Demand Prediction
This project focuses on predicting the total rental count from the Capital Bikeshare system using a custom-built regression model and benchmarking it against standard Scikit-learn models. A Streamlit dashboard is also included to interactively explore data insights and model comparisons.

📊 Dataset
Source: Bike Sharing - UCI Machine Learning Repository

The dataset contains hourly and daily count of rental bikes along with corresponding weather and seasonal information.

📌 Problem Statement
Objective:
To identify key features influencing the bike rental count and to build regression models to accurately predict the number of rentals based on historical data.

🛠️ Project Structure
eda/ - Jupyter notebook(s) for Exploratory Data Analysis

models/

custom_regression.py - A custom regression model built from scratch

metrics.py - Custom implementations of MSE, RMSE, MAE, and R²

tuner.py - Hyperparameter tuning script for learning rate exploration

tester.ipynb - Notebook to test the custom model with metrics

comparison/ - Jupyter notebook comparing custom model with Scikit-learn models

app/

streamlit_app.py - Streamlit dashboard for interactive visualizations and model comparison

📈 Models Trained
✅ Custom Regression Model (from scratch)

✅ Scikit-learn Linear Regression

✅ Scikit-learn Decision Tree Regressor

✅ Scikit-learn Random Forest Regressor

Each model was trained and evaluated on the dataset using common metrics.

📊 Exploratory Data Analysis (EDA)
Key insights were derived from:

Seasonality trends

Weather conditions

Temporal features (hour, day, holiday, working day)

Correlation heatmaps and visual distributions

The findings are also embedded into the Streamlit dashboard for easy interpretation.

⚙️ Custom Regression Model
This project includes a hand-crafted regression model trained using gradient descent and evaluated using custom metric implementations:

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

Mean Absolute Error (MAE)

Coefficient of Determination (R²)

A hyperparameter tuning script (tuner.py) is included to find optimal learning rates.

🧪 Model Evaluation
Models were evaluated and compared using:

Training error

Testing error

Visual plots of predicted vs actual values

Metric scores (MSE, RMSE, MAE, R²)

🚀 Deployment
The following models are deployed using Streamlit:

Custom Regression Model

Random Forest Regressor

Streamlit features include:

Model performance comparison

Visual EDA summary

Interactive parameter insights

