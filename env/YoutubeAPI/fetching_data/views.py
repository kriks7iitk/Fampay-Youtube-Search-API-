from django.shortcuts import render
import requests
from django.conf import settings
from isodate import parse_duration
from django.http import JsonResponse
import datetime
from rest_framework.views import APIView
from fetching_data.models import video_data
from fetching_data.serializers import video_data_Serializer
from rest_framework.response import Response


# function to render index.html for search---------------------------------------------------------------
class videos_detail(APIView):
    def get(self, request, format=None):
        return render(request,'dashboard/index.html')





#function to return Json Response on get request------------------------------------

class data_interval(APIView):
    def get(self,request):
        get_data()
        videos = video_data.objects.all()
        serializer = video_data_Serializer(videos, many=True)
        return Response(serializer.data)




def get_data():

    youtube_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
#paraemters for Youtube Search API---------------------------------------

    d = datetime.datetime.now();
    d = d.isoformat('T')+'Z';
    print(d)

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
    print(r.text)
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
        serializer = video_data_Serializer(data=video_data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            # videos.append(video_data)

        # context = {
        #     'videos' : videos
        # }
        # return JsonResponse(context)
