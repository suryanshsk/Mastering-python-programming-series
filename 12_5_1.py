from chatterbot import ChatBot # type: ignore
from chatterbot.trainers import ChatterBotCorpusTrainer # type: ignore

# Creating a chatbot instance
chatbot = ChatBot('AI Assistant')
trainer = ChatterBotCorpusTrainer(chatbot)

# Training with the English corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
response = chatbot.get_response("Hello, how are you today?")
print(response)
