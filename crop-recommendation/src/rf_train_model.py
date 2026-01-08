
from sklearn.ensemble import RandomForestClassifier

# Initialize and train Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
