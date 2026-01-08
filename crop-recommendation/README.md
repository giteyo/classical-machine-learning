# Crop Recommendation System Using Machine Learning

## Project Overview
This project implements a **Crop Recommendation System** using machine learning techniques. The system analyzes various environmental and soil parameters to recommend the most suitable crop for cultivation.

## Dataset Information
- **Source**: Kaggle
- **Size**: 2200 instances with 7 features and 1 target variable
- **URL**: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset

### Features Description
- **N**: Ratio of Nitrogen content in soil
- **P**: Ratio of Phosphorous content in soil
- **K**: Ratio of Potassium content in soil
- **temperature**: Temperature in degree Celsius
- **humidity**: Relative humidity in %
- **ph**: pH value of the soil
- **rainfall**: Rainfall in mm
- **label**: Crop name for recommendation (target variable)

## Project Structure

### 1. Data Preprocessing
- **Missing Value Handling**: Identified and filled missing values using mean imputation
- **Label Encoding**: Converted categorical crop labels to numerical values using LabelEncoder
- **Data Exploration**: Analyzed feature distributions and correlations

### 2. Key Steps Implemented
- Imported and loaded the dataset using pandas
- Generated statistical summaries of numerical columns
- Checked for missing values and handled them appropriately
- Encoded categorical target variable
- Performed correlation analysis between features and target
- Created correlation heatmap for visualization

### 3. Technologies Used
- **Python**
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning and preprocessing
- **Jupyter Notebook**: Development environment

### 4. Data Quality
- Initial missing values detected and successfully handled
- All features converted to numerical format
- Balanced dataset with 100 instances per crop (22 different crops)

### 5. Crops Included
The dataset contains 22 different crops including:
- Rice, Maize, Jute, Cotton, Coconut, Papaya, Orange, Apple, Muskmelon, Watermelon, Grapes, Mango, Banana, Pomegranate, Lentil, Blackgram, Mungbean, Mothbeans, Pigeonpeas, Kidneybeans, Chickpea, Coffee

## Next Steps
The notebook is prepared for model implementation including:
- Feature scaling and normalization
- Train-test split
- Model training and evaluation
- Performance comparison of different algorithms
- Deployment of the recommendation system

## Author
**Eyob Birhanu**  
MSc in Data Science and Analytics  
Department of Information Science  
College of Informatics  
University of Gondar

**Date**: January 17, 2025

## Course
Advanced Data Mining and Machine Learning Project 2