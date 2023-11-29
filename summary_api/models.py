from django.db import models
from django.contrib.auth import get_user_model

class Summary(models.Model):
    video_id = models.CharField(max_length=100, unique=True)
    video_title = models.CharField(max_length=110)
    video_summary = models.TextField()

    def __str__(self):
        return self.video_title

class UserVideoSummary(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    summary = models.ForeignKey(Summary, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.summary.video_title}"
