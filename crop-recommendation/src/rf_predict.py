
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Make predictions
rf_pred = model.predict(X_test)

# Confusion Matrix and Accuracy
cm = confusion_matrix(y_test, rf_pred)
acc = accuracy_score(y_test, rf_pred)

print("Confusion Matrix:\n", cm)
print("Random Forest Accuracy:", acc)
print("Random Forest Classification Report:\n", classification_report(y_test, rf_pred))

# --- Plot and Save Confusion Matrix ---
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', cbar=False)
plt.title('Random Forest Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.tight_layout()
plt.savefig('random_forest_confusion_matrix.png', dpi=300)
plt.close()

# --- Plot and Save Accuracy Chart ---
plt.figure(figsize=(5, 4))
plt.bar(['Random Forest'], [acc], color='purple')
plt.ylim(0, 1)
plt.title('Random Forest Model Accuracy')
plt.ylabel('Accuracy')
plt.tight_layout()
plt.savefig('random_forest_accuracy_chart.png', dpi=300)
plt.close()
