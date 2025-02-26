import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load Dataset
data = pd.read_csv("passwords_dataset.csv")

# Ensure dataset has required columns
required_columns = {"Password", "Has Lowercase", "Has Uppercase", "Has Special Character", "Length", "Strength"}
if not required_columns.issubset(data.columns):
    raise ValueError(f"Dataset must contain columns: {required_columns}")

# Prepare Features (X) and Target (y)
X = data[["Has Lowercase", "Has Uppercase", "Has Special Character", "Length"]]
y = data["Strength"]

# Encode Strength Labels (e.g., Weak → 0, Medium → 1, Strong → 2)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Function to extract features from user input
def extract_features(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_special = any(not c.isalnum() for c in password)
    length = len(password)
    return [int(has_lower), int(has_upper), int(has_special), length]

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    message = ""
    emoji = ""
    if request.method == 'POST':
        user_password = request.form['password']
        features = extract_features(user_password)
        predicted_label = clf.predict([features])[0]
        prediction = label_encoder.inverse_transform([predicted_label])[0]  # e.g., 'Weak', 'Medium', 'Strong'
        
        # Set messages and emojis based on prediction
        if prediction.lower() == "weak":
            message = "You can do better! Try adding more variety!"
            emoji = "😢"  # Animated sad face can be achieved via CSS animation on this element
        elif prediction.lower() == "medium":
            message = "Not bad, but there's room for improvement!"
            emoji = "😐"  # Slightly satisfied face
        elif prediction.lower() == "strong":
            message = "Awesome! Your password is rock solid!"
            emoji = "🎉"  # Celebrating face
    return render_template('index.html', prediction=prediction, message=message, emoji=emoji)

if __name__ == "__main__":
    app.run(debug=True)
