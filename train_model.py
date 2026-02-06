import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1️⃣ Load dataset
df = pd.read_csv("beauty_product_data.csv")

# 2️⃣ Encode categorical columns
label_encoders = {}

for col in df.columns:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

# 3️⃣ Split features & target
X = df.drop("recommended_product", axis=1)
y = df["recommended_product"]

# 4️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5️⃣ Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6️⃣ Test accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# 7️⃣ Save model & encoders
joblib.dump(model, "beauty_model.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

print("Model and encoders saved successfully")
