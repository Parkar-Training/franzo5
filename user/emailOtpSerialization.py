from user.models import users_new
from rest_framework import serializers

class emailOtpClass(serializers.ModelSerializer):
    #otp = serializers.CharField(required=False)
    emailid = serializers.CharField(required=True)
    name = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    #acc_created = serializers.CharField(required=False)
    #friendslist = serializers.CharField(required=False)
    mobilenumber = serializers.CharField(required=False)
   # private = serializers.CharField(required=False)
   # userId = serializers.CharField(required=False)




    class Meta:
        model = users_new
        #fields= list(["emailid","otp"])
        fields= '__all__'