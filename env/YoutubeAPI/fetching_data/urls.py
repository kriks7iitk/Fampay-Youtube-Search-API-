
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.videos_detail.as_view(),name='index'),
    path('refresh',views.data_interval.as_view() , name = 'YTapi'),
    path('videolist',views.videos_list.as_view() , name = 'videolist')
]
