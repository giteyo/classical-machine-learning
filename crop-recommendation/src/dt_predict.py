
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Predict and evaluate
dt_predictions = dt_model.predict(X_test)

# Confusion Matrix and Accuracy
cm = confusion_matrix(y_test, dt_predictions)
acc = accuracy_score(y_test, dt_predictions)

print("Confusion Matrix:\n", cm)
print("Decision Tree Accuracy:", acc)
print("Decision Tree Classification Report:\n", classification_report(y_test, dt_predictions))

# --- Plot and Save Confusion Matrix ---
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', cbar=False)
plt.title('Decision Tree Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.tight_layout()
plt.savefig('decision_tree_confusion_matrix.png', dpi=300)
plt.close()

# --- Plot and Save Accuracy Chart ---
plt.figure(figsize=(5, 4))
plt.bar(['Decision Tree'], [acc], color='orange')
plt.ylim(0, 1)
plt.title('Decision Tree Model Accuracy')
plt.ylabel('Accuracy')
plt.tight_layout()
plt.savefig('decision_tree_accuracy_chart.png', dpi=300)
plt.close()
