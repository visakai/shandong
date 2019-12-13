from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def sound(input):
# curl -X POST -H "Referer: https://ttsmp3.com/" -H "Access-Control-Request-Method: POST" -H "Host:ttsmp3.com" -H "Origin: https://ttsmp3.com" -d "msg=%E5%8E%BF%E8%89%B3%E9%AB%93%E5%90%81%E9%83%A8%E5%92%AC%E6%B1%9F%20%0A%E6%A0%87%E4%BB%A5%E6%A0%87%E8%92%BF%E5%96%8A%E4%B9%8C%E8%80%B3%E6%B5%AA%0A&lang=Zhiyu&source=ttsmp3" "https://ttsmp3.com/makemp3.php"
    print('input={}'.format(input))

    url = "https://ttsmp3.com/makemp3.php"
    myobj = {'lang': 'Zhiyu', 'source':'ttsmp3', 'msg':'hahaha'}
    x = requests.post(url, data = myobj, headers = {"Referer": "https://ttsmp3.com/"})
    print(x.status_code)
    print(x.text)
    mp3 = x.json().get('MP3')

    return HttpResponse(mp3)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
