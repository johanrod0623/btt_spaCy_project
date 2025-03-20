# Import spaCy and load the model
import spacy
nlp = spacy.load("text_classifier_model")

# Take user input in a loop
while True:
    user_input = input("\nEnter a sentence (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    doc = nlp(user_input)
    print("Prediction:")
    for label, score in doc.cats.items():
        print(f"{label}: {score:.2f}")
