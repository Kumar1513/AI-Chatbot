from flask import Flask, request, jsonify
from chatbot import chatbot_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_message = chatbot_response(user_message)
    return jsonify({'response': bot_message})

if __name__ == "__main__":
    app.run(debug=True)