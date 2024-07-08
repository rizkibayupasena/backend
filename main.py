from flask import Flask, request, jsonify
from chatbot_logic import Chatbot
from flask_cors import CORS

app = Flask(__name__)

chatbot = Chatbot()
CORS(app, origins=['https://aimlchat.vercel.app', 'http://127.0.0.1:5500' , 'http://127.0.0.1:5501'])

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['message']
    bot_response = chatbot.get_bot_response(user_message)
    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)
