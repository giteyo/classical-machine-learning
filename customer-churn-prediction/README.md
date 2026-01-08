# Customer Churn Prediction

## Project Overview

This project predicts whether a customer will churn (leave a service) based on historical data. It demonstrates classical machine learning techniques, data preprocessing, model.

## Dataset Information

* **Source**: Kaggle
* **Size**: 7043 instances with 20 features and 1 target variable

### Features Description

The features names are the following: LoyaltyID, Customer ID, Senior Citizen, Partner, Dependents, Tenure, Phone Service, Multiple Lines, Internet Service, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV, Streaming Movies, Contract, Paperless Billing, Payment Method, Monthly Charges, Total Charges, Churn

## Project Structure

### 1\. Data Preprocessing

* **Missing Value Handling**: Identified and filled missing values using mean imputation
* **Label Encoding**: Converted categorical crop labels to numerical values using LabelEncoder
* **Data Exploration**: Analyzed feature distributions and correlations

### 2\. Key Steps Implemented

* Imported and loaded the dataset using pandas
* Generated statistical summaries of numerical columns
* Checked for missing values and handled them appropriately
* Encoded categorical target variable
* Performed correlation analysis between features and target
* Created correlation heatmap for visualization

### 3\. Technologies Used

* **Python**
* **pandas**: Data manipulation and analysis
* **scikit-learn**: Machine learning and preprocessing
* **Jupyter Notebook**: Development environment

### 4\. Data Quality

* Initial missing values detected and successfully handled
* All features converted to numerical format

### 5\. Crops Included

The dataset describes whether he leaves or stays.

## Next Steps

The notebook is prepared for model implementation including:

* Feature scaling and normalization
* Train-test split
* Model training and evaluation
* Performance comparison of different algorithms
* Deployment of the churn prediction

## Author

**Eyob Birhanu** **Haile**
MSc in Data Science and Analytics  
College of Informatics

Department of Information Science  
University of Gondar

**Date**: March, 2025

## Course

Introduction to data science and Analytics

