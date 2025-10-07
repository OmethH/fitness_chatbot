from flask import Flask, request, jsonify
import pickle

# Load trained model
with open("fitness_bot.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def chatbot_response(user_input):
    user_vec = vectorizer.transform([user_input])
    return model.predict(user_vec)[0]

# Initialize Flask app
app = Flask(__name__)

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = chatbot_response(user_message)
    return jsonify({"reply": response})

# Run the server
if __name__ == "__main__":
    app.run(port=5000, debug=True)
