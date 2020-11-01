from rest_framework import serializers
from fetching_data.models import video_data

class video_data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = video_data
        fields = ['id', 'title', 'publishtime', 'description', 'duration', 'url','thumbnail']
