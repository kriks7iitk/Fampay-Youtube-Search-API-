from django.shortcuts import render
import requests
from django.conf import settings
from isodate import parse_duration
from django.http import JsonResponse
import datetime


# function to render index.html for search---------------------------------------------------------------

def index(request):
    if(request.method=='GET'):
        return render(request,'dashboard/index.html')





#function to return Json Response on get request------------------------------------


def refresh(request):

    if(request.method == 'GET'):
        youtube_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'
#paraemters for Youtube Search API---------------------------------------

        d = datetime.datetime.now();
        d = d.isoformat('T');

        search_params = {
            'part' : 'snippet',
            'q' : 'news india hindi',
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 15,
            'order' : 'date',
            'publishedAfter' : d
        }

# getting seaerch vidoe ids---------------------------
        video_ids = []
        r = requests.get(youtube_url,params = search_params)
        # print(r.text)
        results = r.json()['items']


        for result in results:
            video_ids.append(result['id']['videoId'])
# getting  vidoe details from video ids---------------------------

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids)
        }
        r = requests.get(video_url,params = video_params)
        results = r.json()['items']
        videos = []

        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'id': result['id'],
                'duration' : parse_duration(result['contentDetails']['duration']).total_seconds()//60,
                'thumbnail' : result['snippet']['thumbnails']['high']['url'],
                'publishtime' : result['snippet']['publishedAt'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'description' : result['snippet']['description']
                }
            print(video_data)
            videos.append(video_data)

        context = {
            'videos' : videos
        }
        return JsonResponse(context)
