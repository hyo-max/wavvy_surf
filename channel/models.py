# video/models.py
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    video_key = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=500)
    video_desc = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-id'] # 정렬기준