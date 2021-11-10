from django.db import models

# Create your models here.
class friendModel(models.Model):
    FId = models.AutoField(primary_key=True)

    FriendId = models.IntegerField(blank=False, null=False)
    FuserId = models.IntegerField(blank=False, null=False)
    Status= models.IntegerField(blank=False, null=False)
    Friends_created= models.DateTimeField(auto_now_add=True)
    #FuserId = models.CharField(max_length=3)