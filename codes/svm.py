# Using Support Vector Machine model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

print("Using Support Vector Machine (SVM): ")

# Load the data
data = pd.read_csv('penguins.csv')

# Select relevant features and target variable
features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex', 'island']
target = 'species'

# Encode the target variable, sex feature, and island feature
le = LabelEncoder()
data[target] = le.fit_transform(data[target])
data['sex'] = data['sex'].fillna('Unknown')
sex_encoder = LabelEncoder()
data['sex'] = sex_encoder.fit_transform(data['sex'])
island_encoder = LabelEncoder()
data['island'] = island_encoder.fit_transform(data['island'])

# Drop rows with missing values in the features
data = data.dropna(subset=features)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=42)

# Initialize the SVM model
model = SVC(kernel='linear', C=1.0, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Compute accuracy on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on the test set: {accuracy:.2f}")

# Get user input
bill_length_mm = float(input("Enter bill length (mm): "))
bill_depth_mm = float(input("Enter bill depth (mm): "))
flipper_length_mm = float(input("Enter flipper length (mm): "))
body_mass_g = float(input("Enter body mass (g): "))
sex = input("Enter sex (Male/Female/Unknown): ")
island = input("Enter island (Torgersen/Biscoe/Dream): ")

# Encode sex and island inputs
sex_encoded = sex_encoder.transform([sex.capitalize()])
if len(sex_encoded) == 0:
    sex_encoded = sex_encoder.transform(['Unknown'])
island_encoded = island_encoder.transform([island.capitalize()])

# Create a new DataFrame with user input
user_input = pd.DataFrame({
    'bill_length_mm': [bill_length_mm],
    'bill_depth_mm': [bill_depth_mm],
    'flipper_length_mm': [flipper_length_mm],
    'body_mass_g': [body_mass_g],
    'sex': sex_encoded,
    'island': island_encoded
})

# Make prediction
prediction = model.predict(user_input[features])
predicted_species = le.inverse_transform(prediction)[0]
print(f"Predicted species: {predicted_species}")
