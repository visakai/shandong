from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def sound(request):
    print('request={}'.format(request))
    m = request.GET.get('msg', '')
    print('m={}'.format(m))
    words = m.split(',')
    sentense = ''
    for word in words:
        if word is '0':
            print('converting non-hanzi to pause')
            sentense += "<break time='0.5s'/>"
        else:
            sentense += "<phoneme alphabet='x-amazon-pinyin' ph='{}'></phoneme>".format(word)
    print('sentense={}'.format(sentense))

    url = "https://ttsmp3.com/makemp3.php"
    myobj = {'lang': 'Zhiyu', 'source':'ttsmp3', 'msg':sentense}
    x = requests.post(url, data = myobj, headers = {"Referer": "https://ttsmp3.com/"})
    print(x.status_code)
    print(x.text)
    mp3 = x.json().get('MP3')
    response = HttpResponse(mp3)
    response["Access-Control-Allow-Origin"] = "*"
    return response

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
