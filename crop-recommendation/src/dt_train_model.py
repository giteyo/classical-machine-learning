
from sklearn.tree import DecisionTreeClassifier

# Initialize and train Decision Tree
dt_model = DecisionTreeClassifier(max_depth=10)
dt_model.fit(X_train, y_train)
