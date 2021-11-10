from django.db import models
class advertise(models.Model):
    id = models.AutoField(primary_key=True)
    ad_name = models.CharField(max_length=20)
    ad_content = models.CharField(max_length=20,unique=True,error_messages={"unique" :"This  content is already"
                                                                                       " exists. Please  enter different content"})
    ad_created = models.CharField(max_length=20,blank=True)
