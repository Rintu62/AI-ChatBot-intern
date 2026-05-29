from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot():

    user_message = request.form["message"].lower()

    # Greetings
    if "hello" in user_message or "hi" in user_message:
        reply = "Hello there! 👋"

    elif "hey" in user_message:
        reply = "Hey  How can I help you?"

    elif "good morning" in user_message:
        reply = "Good Morning "

    elif "good afternoon" in user_message:
        reply = "Good Afternoon "

    elif "good evening" in user_message:
        reply = "Good Evening "

    elif "good night" in user_message:
        reply = "Good Night 😴"

    # Basic conversation
    elif "how are you" in user_message:
        reply = "I am fine  What about you?"

    elif "i am fine" in user_message:
        reply = "That's great "

    elif "what are you doing" in user_message:
        reply = "I am chatting with you "

    elif "who are you" in user_message:
        reply = "I am your AI Chatbot "

    elif "what is your name" in user_message:
        reply = "My name is AI Chatbot "

    elif "who made you" in user_message:
        reply = "Rigu created me "

    # AI / Tech
    elif "ai" in user_message:
        reply = "AI means Artificial Intelligence "

    elif "python" in user_message:
        reply = "Python is an awesome programming language "

    elif "flask" in user_message:
        reply = "Flask is a Python web framework "

    elif "html" in user_message:
        reply = "HTML is used to create webpages "

    elif "css" in user_message:
        reply = "CSS is used for webpage styling "

    elif "javascript" in user_message:
        reply = "JavaScript makes websites interactive "

    # Personal questions
    elif "your age" in user_message:
        reply = "I don't have an age "

    elif "where are you from" in user_message:
        reply = "I live inside your computer "

    elif "do you love me" in user_message:
        reply = "Of course ❤️"

    # Time / Date
    elif "time" in user_message:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        reply = f"Current time is {current_time} "

    elif "date" in user_message:
        from datetime import datetime
        current_date = datetime.now().strftime("%d-%m-%Y")
        reply = f"Today's date is {current_date} "

    # Fun
    elif "joke" in user_message:
        reply = "Why do programmers love Python? Because it's easy to understand "

    elif "motivate me" in user_message:
        reply = "Keep learning and never give up "

    elif "tell me something" in user_message:
        reply = "Did you know? AI is changing the world "

    # Bye
    elif "bye" in user_message:
        reply = "Goodbye 👋 Have a great day!"

    elif "thank you" in user_message or "thanks" in user_message:
        reply = "You're welcome "

    # Default
    else:
        reply = "Sorry, I don't understand that "

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
