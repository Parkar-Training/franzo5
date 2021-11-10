from django.db import models

# Create your models here.



class Post(models.Model):

    PostId = models.AutoField
    Post_Time = models.DateTimeField(auto_now=True)
    Like_count = models.IntegerField()
    Comment = models.CharField(max_length=40)
    Post_data = models.CharField(max_length=80, blank=False)