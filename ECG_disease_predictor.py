
import pandas as pd
import joblib


model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')  

disease_map = {
    0: "Normal",
    1: "Supraventricular Arrhythmia",
    2: "Ventricular Arrhythmia",
    3: "Fusion Beat",
    4: "Unknown Disease"
}


def predict_disease(file_path):
    try:
        
        input_data = pd.read_csv(file_path, header=None)
        
        
        if input_data.shape[1] > 187:
            print("Warning: Extra features detected. Trimming to 187 features.")
            input_data = input_data.iloc[:, :187]
        elif input_data.shape[1] < 187:
            print("Error: Insufficient features. File must contain 187 features.")
            return

        
        input_data_scaled = scaler.transform(input_data)


        predictions = model.predict(input_data_scaled)
        
        
        print("\nPrediction Results:")
        for i, pred in enumerate(predictions, start=1):
            print(f"{i}: {disease_map.get(pred, 'Unknown Disease')}")

    except Exception as e:
        print(f"Error: {e}. Please check the file and ensure it contains valid numerical data.")


input_file = 'Try1.csv'  # Replace with your input file
predict_disease(input_file)

