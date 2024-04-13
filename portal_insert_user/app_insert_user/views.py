from django.shortcuts import render
from chatterbot import ChatBot

#from spacy.cli import download

#download("en_core_web_sm")

#class ENGSM:
 #   ISO_639_1 = "en_core_web_sm"

#import chatBot
#from chatterbot.trainders import ChatterBotCorpusTrainer

# Create your views here.

def home(request):
    return render(request, 'appointments/index.html')

def form(request):
    return render(request, 'appointments/login.html')

##def chatterbot(request):
    ######### Definindo o nome do meu ChatBot #################
  ##  chatbot = ChatBot("Sully", tagger_language = ENGSM)
   ## if request.method == 'POST':
     ##   user_input = request.POST['user_input']
      ##  bot_response = chatbot.get_response(user_input)
       ## return render(request, 'appointments/chatbot_popup.html', {'response': bot_response})
    ## else:
      ##  return render(request, 'appointments/chatbot_popup.html')
