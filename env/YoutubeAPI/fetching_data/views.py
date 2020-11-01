from django.shortcuts import render
import requests
from django.conf import settings
from isodate import parse_duration

# Create your views here.
def index(request):
    if(request.method == 'GET'):
        youtube_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : 'songs',
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 9,
            'order' : 'date'
        }
        video_ids = []
        r = requests.get(youtube_url,params = search_params)
        results = r.json()['items']

        for result in results:
            video_ids.append(result['id']['videoId'])

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids)
        }
        r = requests.get(video_url,params = video_params)
        # print(r.text);
        results = r.json()['items']

        videos = []

        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'id': result['id'],
                'duration' : parse_duration(result['contentDetails']['duration']).total_seconds()//60,
                'thumbnail' : result['snippet']['thumbnails']['high']['url'],
                'publishtime' : result['snippet']['publishedAt'],
                'description' : result['snippet']['description']
                }
            videos.append(video_data)


        return render(request,'dashboard/index.html')
