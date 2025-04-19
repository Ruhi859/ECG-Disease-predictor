ECG Disease Prediction Script
This repository contains a Python script for predicting heart diseases based on ECG data using a pre-trained Logistic Regression model. The script uses datasets (mitbih_train.csv, mitbih_test.csv, ptbdb_normal.csv, ptbdb_abnormal.csv) for training and testing, and supports file-based prediction for new data.

Features
- Model Training:- Logistic Regression model trained on the MIT-BIH dataset.
- Preprocessing of data using StandardScaler to normalize features.
- Model saved as model.pkl and scaler saved as scaler.pkl.

- File-Based Disease Prediction:- Supports .csv and .xlsx input files for predictions.
- Automatically maps predictions to disease names.
- Outputs predictions serially for easy readability.

- Disease Categories:- Normal
- Supraventricular Arrhythmia
- Ventricular Arrhythmia
- Fusion Beat
- Unknown Disease
Requirements
- Python 3.11 or higher
- Libraries:- pandas
- joblib
- sklearn


Install the required libraries using:
pip install pandas joblib scikit-learn



How to Use
Training the Model
- Place the required datasets (mitbih_train.csv, mitbih_test.csv, ptbdb_normal.csv, ptbdb_abnormal.csv) in the same directory as the script.
- Run the training script to generate the model (model.pkl) and scaler (scaler.pkl):python train_model.py

Predicting Disease 
- Place your input file (e.g., ptbdb_abnormal.csv) in the same directory as the script.
- Update the input_file variable in the script with the name of your file.
- Run the script to print predictions serially:python predict_disease.py


Output Example:
Prediction Results:
1: Normal
2: Ventricular Arrhythmia
3: Unknown Disease



File Format for Input
Ensure the input file contains only the feature columns without headers.




