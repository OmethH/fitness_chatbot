# 🏋️‍♂️ AI Fitness Chatbot

An intelligent chatbot trained to answer fitness-related questions — including exercise techniques, targeted muscle groups, and workout guidance.

## 🚀 Features
- AI model trained on 1000+ exercise Q&A pairs.
- Understands fitness questions like “How do I do a squat?” or “Which muscles does bench press work?”
- Flask API backend for easy integration.
- Lightweight and easy to train with your own dataset.

## 🧠 Dataset
The dataset was generated from a Kaggle Exercise Database and transformed into chatbot-friendly Q&A pairs:
- Each exercise includes "What is..." and "How do I perform..." questions.
- Covers full-body workouts.

## 🛠️ Technologies Used
- Python
- Flask
- Pandas
- scikit-learn
- TfidfVectorizer (for NLP)
- Pickle (for model persistence)

## ⚙️ How to Run
1. Clone this repo  
   ```bash
   git clone https://github.com/<your-username>/fitness_chatbot.git
