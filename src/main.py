from src.data_preprocessing import load_data, preprocess_data
from src.eda import plot_correlation_matrix
from src.model import train_model


# Load data
data_path = 'C:\\Users\\kanag\\employee-attrition\\data\\WA_Fn-UseC_-HR-Employee-Attrition.csv'
df = load_data(data_path)

# Preprocess data
df_processed = preprocess_data(df)

# Perform EDA
plot_correlation_matrix(df_processed)

# Train model
model, accuracy = train_model(df_processed)

# Print results
print(f"Model Accuracy: {accuracy:.2f}")
