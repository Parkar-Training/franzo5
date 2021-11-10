from django.db import models

# Create your models here.

class Users(models.Model):
    userId= models.IntegerField(max_length=10, primary_key=True)
    Name= models.CharField(max_length=20)
    Mobile_Number= models.CharField(max_length=20)
    Password= models.CharField(max_length=20)
    EmailId= models.CharField(max_length=20)
    AccCreated= models.DateTimeField()
    FriendsList= models.JSONField()
    Private= models.BooleanField()
    class Meta:
        db_table= 'mydb'
