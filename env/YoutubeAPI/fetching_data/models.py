from django.db import models

class video_data(models.Model):
    id = models.CharField(max_length=100000, blank=False,primary_key=True)
    publishtime = models.DateTimeField(default='')
    title = models.TextField(blank=False, default='')
    description = models.TextField()
    duration = models.IntegerField(default=False)
    thumbnail = models.CharField(default='', max_length=10000)
    url = models.CharField( default='', max_length=100000)
    class Meta:
        ordering = ['-publishtime']
