import pickle

# Load model
with open("fitness_bot.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def chatbot_response(user_input):
    user_vec = vectorizer.transform([user_input])
    return model.predict(user_vec)[0]

# Test
print(chatbot_response("What’s a good chest workout?"))
print(chatbot_response("How do I lose belly fat?"))
print(chatbot_response("What should I eat after gym?"))
