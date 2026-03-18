from django.db import models
from django.contrib.auth.models import User

# NOTICE THIS LINE IS FIXED:
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=128)
    content = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True) 
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp'] 

    def __str__(self):
        return f"{self.user.username}: {self.content}"