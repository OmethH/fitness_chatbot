import pickle

# Load model
with open("fitness_bot.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def chatbot_response(user_input):
    user_vec = vectorizer.transform([user_input])
    return model.predict(user_vec)[0]

print("💪 Fitness Chatbot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("Bot:", response)
