# 🔐 ML Password Security Checker

🚀 Live Demo: ML Password Security Checker(https://ml-password-security-checker.onrender.com/)

# 🔥 Overview

Ever wondered how strong your password really is? 🤔 This ML-powered Password Strength Checker 🔍 analyzes your password and gives instant feedback on its security level. No more 123456 or password1, okay? 😏

# 🛠 Features

✅ Machine Learning Powered - Uses RandomForestClassifier to predict password strength.✅ Live Strength Prediction - Instantly checks if your password is Weak, Medium, or Strong.✅ Interactive UI - A sleek, animated interface that reacts to password strength.✅ Emoji Feedback - Because why not? 🎉😐😢✅ Fun & Engaging - We make security exciting! 🤩

# 📸 Screenshots

1️⃣ Landing Page
![image](https://github.com/user-attachments/assets/0b4b38f1-2247-4671-93a0-6991f43512d8)

2️⃣ Weak Password Result
![image](https://github.com/user-attachments/assets/eb72c30d-f5f3-4a22-9914-72c27b1d4b80)

3️⃣ Medium Password Result
![image](https://github.com/user-attachments/assets/0a461d6f-dd7b-404e-a83b-623694fd5bd8)

4️⃣ Strong Password Result
![image](https://github.com/user-attachments/assets/81743f7a-c2c5-4843-a446-1967313fd303)


#🏗 How It Works

# Extract password features
def extract_features(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_special = any(not c.isalnum() for c in password)
    length = len(password)
    return [int(has_lower), int(has_upper), int(has_special), length]

# Make a prediction
predicted_label = clf.predict([extract_features("P@ssw0rd123")])[0]
prediction = label_encoder.inverse_transform([predicted_label])[0]
print(prediction)  # Output: 'Strong' 💪

# 🤝 Contributing

Got ideas? Found a bug? PRs are totally welcome! 🍕
Let's collaborate..
