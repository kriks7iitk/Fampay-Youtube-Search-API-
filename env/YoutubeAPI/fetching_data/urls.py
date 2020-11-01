
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.videos_detail,name='index'),
    path('refresh',views.data_interval , name = 'YTapi'),
]
