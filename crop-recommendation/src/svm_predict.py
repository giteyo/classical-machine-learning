
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Predict and evaluate
svm_predictions = svm_model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, svm_predictions)
acc = accuracy_score(y_test, svm_predictions)

print("Confusion Matrix:\n", cm)
print("SVM Accuracy:", acc)
print("SVM Classification Report:\n", classification_report(y_test, svm_predictions))

# --- Plot Confusion Matrix ---
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('SVM Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.tight_layout()
plt.savefig('svm_confusion_matrix.png', dpi=300)
plt.close()  # Close the plot

# --- Plot Accuracy Chart ---
plt.figure(figsize=(5, 4))
plt.bar(['SVM'], [acc], color='green')
plt.ylim(0, 1)
plt.title('SVM Model Accuracy')
plt.ylabel('Accuracy')
plt.tight_layout()
plt.savefig('svm_accuracy_chart.png', dpi=300)
plt.close()
