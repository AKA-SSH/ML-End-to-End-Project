# End-to-End Machine Learning Project

This repository showcases a comprehensive machine learning project, guiding you through the entire workflow, from data preprocessing and model training to deployment and inference. The project's primary goal is to address a regression problem, predicting students' math scores based on various demographic and academic features.

### Table of Contents

1. [Introduction](#end-to-end-machine-learning-project)
   - [Overview](#overview)

2. [Dataset Features](#dataset-features)
   - [Categorical Features](#categorical-features)
   - [Numerical Features (Target Variable in Bold)](#numerical-features-target-variable-in-bold)

3. [Libraries Used](#libraries-used)
   - [Data Download](#data-download)
   - [Notebook](#notebook)
   - [Data Manipulation](#data-manipulation)
   - [Data Representation](#data-representation)
   - [Machine Learning](#machine-learning)
   - [Hyperparameter Tuning](#hyperparameter-tuning)

4. [Models Used](#models-used)

5. [Project Structure](#project-structure)
   - [data_ingestion.py](#data_ingestionpy)
   - [data_transformation.py](#data_transformationpy)
   - [model_training.py](#model_trainingpy)
   - [logger.py](#loggerpy)
   - [exception.py](#exceptionpy)
   - [utilities.py](#utilitiespy)

6. [Key Components](#key-components)
   - [data Directory](#data-directory)
   - [notebooks Directory](#notebooks-directory)


## Overview

Welcome to our end-to-end machine learning project, centered around predicting students' math scores based on demographic and academic features. The dataset includes essential information such as gender, race/ethnicity, parental level of education, lunch, test preparation course, and numerical scores for math, reading, and writing.

## Dataset Features

- **Categorical Features:**
  - gender
  - race/ethnicity
  - parental level of education
  - lunch
  - test preparation course

- **Numerical Features (Target Variable in Bold):**
  - **math score**
  - reading score
  - writing score

## Libraries Used

### Data Download
- dill
- opendatasets

### Notebook
- jupyter

### Data Manipulation
- numpy
- scipy
- pandas

### Data Representation
- tabulate
- seaborn
- matplotlib

### Machine Learning
- xgboost
- catboost
- lightgbm
- scikit-learn

### Hyperparameter Tuning
- optuna

## Models Used

```python
models = {
    'Linear Regression': LinearRegression(),
    'Lasso': Lasso(),
    'Ridge': Ridge(),
    'Random Forest Regressor': RandomForestRegressor(),
    'XGBoost': XGBRegressor(verbosity=0),
    'LGBM Regressor': LGBMRegressor(verbosity=-1),
    'CatBoost Regressor': CatBoostRegressor(verbose=False),
    'AdaBoost Regressor': AdaBoostRegressor()
}
```
## Project Structure

1. **data_ingestion.py**
   - Responsible for handling the data ingestion process, including functions or classes for downloading data and reading data files.

2. **data_transformation.py**
   - Focuses on processing and transforming raw data for analysis or model training. Tasks include cleaning, handling missing values, and encoding categorical variables.

3. **model_training.py**
   - Dedicated to training machine learning models, defining, training, and evaluating models, possibly involving hyperparameter tuning.

4. **logger.py**
   - Manages project logging, tracking code execution, capturing events, and debugging. Includes functions or classes for setting up logging configurations.

5. **exception.py**
   - Handles custom exceptions for error handling. Provides a mechanism for dealing with unexpected situations during code execution.

6. **utilities.py**
   - Contains utility functions or helper functions used across different parts of the project. Serves as a central place for commonly used functionality.

## Key Components

1. **data Directory**
   - **raw:** Contains raw, unprocessed data.
   - **processed:** Stores cleaned and processed data.

2. **notebooks Directory**
   - Holds Jupyter notebooks for exploratory data analysis (EDA) and experimentation.
