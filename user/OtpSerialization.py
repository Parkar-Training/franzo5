from user.models import users_new
from rest_framework import serializers

class OtpserializerClass(serializers.ModelSerializer):
    otp = serializers.CharField(required=False)
    emailid = serializers.CharField(required=False)

    class Meta:
        model= users_new
        fields= list(["emailid","otp"])