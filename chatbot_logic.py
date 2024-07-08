
import aiml

class Chatbot:
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn('chatbot.aiml')
        self.kernel.learn('training.aiml')

    def get_bot_response(self, user_input):
        return self.kernel.respond(user_input)
