import requests

# URL of your running Flask API
url = "http://127.0.0.1:5000/chat"

# Example question to send to the bot
data = {"message": "How do I lose belly fat?"}

# Send POST request
response = requests.post(url, json=data)

# Print the bot's reply
if response.status_code == 200:
    print("Bot reply:", response.json()["reply"])
else:
    print("Error:", response.status_code, response.text)
