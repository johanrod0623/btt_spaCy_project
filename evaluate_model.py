# Import required modules
import spacy
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

# Load test data
df = pd.read_csv("test.csv")
texts = df["text"].tolist()
true_labels = df["label"].tolist()

# Load the model
nlp = spacy.load("text_classifier_model")

# Predict labels
predicted_labels = []
for text in texts:
    doc = nlp(text)
    pred_label = max(doc.cats, key=doc.cats.get)
    predicted_labels.append(pred_label)

# Print evaluation metrics
print("\n=== Classification Report ===")
print(classification_report(true_labels, predicted_labels, digits=3))
accuracy = accuracy_score(true_labels, predicted_labels)
print(f"\nOverall Accuracy: {accuracy:.2f}")
