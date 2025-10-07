import tkinter as tk
from tkinter import scrolledtext
import pickle

# Load your trained chatbot model
with open("fitness_bot.pkl", "rb") as f:
    vectorizer, model = pickle.load(f)

def chatbot_response(user_input):
    user_vec = vectorizer.transform([user_input])
    return model.predict(user_vec)[0]

def send_message(event=None):
    msg = entry.get().strip()
    if msg:
        # Show user bubble
        chat_box.config(state="normal")
        chat_box.insert(tk.END, "\n", "margin")  # spacing
        chat_box.insert(tk.END, f"You: {msg}\n", "user")
        
        # Bot reply
        reply = chatbot_response(msg)
        chat_box.insert(tk.END, f"Bot: {reply}\n", "bot")
        
        chat_box.config(state="disabled")
        chat_box.yview(tk.END)  # Auto-scroll
        entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("💪 Fitness Chatbot")
root.geometry("500x500")
root.configure(bg="#ece5dd")

# Chat Area
chat_box = scrolledtext.ScrolledText(root, state="disabled", wrap="word", bg="#ffffff", font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill="both", expand=True)

# Add styles (tags for formatting)
chat_box.tag_configure("user", foreground="white", background="#25D366", justify="right", spacing1=5, lmargin1=80, rmargin=5)
chat_box.tag_configure("bot", foreground="black", background="#e5e5ea", justify="left", spacing1=5, lmargin1=5, rmargin=80)
chat_box.tag_configure("margin", spacing1=10)

# Entry + Send Button
frame = tk.Frame(root, bg="#ece5dd")
frame.pack(padx=10, pady=10, fill="x")

entry = tk.Entry(frame, font=("Arial", 12))
entry.pack(side="left", padx=(0,10), expand=True, fill="x")
entry.bind("<Return>", send_message)  # Press Enter to send

send_btn = tk.Button(frame, text="Send", command=send_message, bg="#25D366", fg="white", font=("Arial", 10, "bold"))
send_btn.pack(side="right")

root.mainloop()
