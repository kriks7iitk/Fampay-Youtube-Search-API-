from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.
def index(request):
    youtube_url = 'https://www.googleapis.com/youtube/v3/search'

    params = {
        'part' : 'snippet',
        'q' : 'songs',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 9,
        'order' : 'date'
    }
    r = requests.get(youtube_url,params = params)
    print(r.text)
    return render(request,'dashboard/index.html')
