from django.db import models

from django.db import models

class Adv_prof(models.Model):
    userId = models.AutoField
    About_me = models.CharField(max_length=25)
    Interest = models.CharField(max_length=25)
    Hobbies = models.CharField(max_length=20)
    Activities = models.CharField(max_length=20)
    Location = models.CharField(max_length=20)


from django.db import models
