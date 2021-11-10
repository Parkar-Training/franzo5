from user.models import users_new
from rest_framework import serializers
from django.db import models

class serializerLoginClass(serializers.ModelSerializer):
   # acc_created = serializers.CharField(required=False)
    #userId = serializers.CharField(required=False)

    class Meta:
        model= users_new
        fields= ('mobilenumber','userId','emailid','msg','status')
        #fields = ('__all_')
      #  obj = users_new.objects.last()
       # print(type(obj))
      #  field_value = getattr(obj, 'mobilenumber')
       # print("field no.: ", field_value)
        #print("get attr: ",getattr(users_new,'mobilenumber'))
