from user.models import users_new
from rest_framework import serializers

class OtpVerifyserializerClass(serializers.ModelSerializer):
    otp = serializers.CharField(required=True)
    #emailid = serializers.CharField(required=False)

    class Meta:
        model= users_new
        fields= list([('otp')])