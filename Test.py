import pickle

# Load the saved model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the vectorizer
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Test the model with sample data
sample_text = ["Congratulations! You've won a free trip to Bahamas."]
transformed_text = vectorizer.transform(sample_text).toarray()

# Predict
result = model.predict(transformed_text)
print("Spam" if result[0] == 1 else "Ham")
