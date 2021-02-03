from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Blog(models.Model): 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    