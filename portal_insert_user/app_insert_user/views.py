from django.shortcuts import render
#import chatBot
#from chatterbot.trainders import ChatterBotCorpusTrainer

# Create your views here.

def home(request):
    return render(request, 'appointments/index.html')

def form(request):
    return render(request, 'appointments/form.html')
