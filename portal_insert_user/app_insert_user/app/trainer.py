from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = "en_core_web_sm"

######### Definindo o nome do meu ChatBot #################
chatbot = ChatBot("Sully", tagger_language = ENGSM)

######### Definindo a lista de treinamento ################
listTrainer = [
    "Olá",
    "Olá, tudo bem?",
    "Tudo bem e com você?",
    "Tudo ótimo, obrigado por perguntar!",
    "Pode me ajudar ?",
    "Como posso te ajudar?",
]

######### Carregando a lista de treinamento ###############
trainer = ListTrainer(chatbot)
trainer.train(listTrainer)

chatbot.get_response("Passe a mensagem") #- #Esse comando permite que mandemos a mensagem a o chatbot.
#chatbot.storage.drop #- #Esse comando zera a base de dados para que o chatbot possa ser treinado novamente.



