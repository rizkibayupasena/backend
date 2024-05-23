
import aiml

class Chatbot:
    def __init__(self):
        # Inisialisasi AIML Interpreter
        self.kernel = aiml.Kernel()
        # Memuat file AIML
        self.kernel.learn('chatbot.aiml')
        self.kernel.learn('training.aiml')

    def get_bot_response(self, user_input):
        # Mengembalikan respons dari chatbot berdasarkan input pengguna
        return self.kernel.respond(user_input)
