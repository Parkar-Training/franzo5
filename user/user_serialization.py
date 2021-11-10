from rest_framework import serializers
from user.models import users_new

class user_Serialization_Class(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    mobilenumber = serializers.CharField(required=False)
    private = serializers.BooleanField(required=False)
    acc_created= serializers.DateTimeField(required=False)
    userId= serializers.IntegerField(required=False)
    friendslist= serializers.CharField(required=False)
    otp= serializers.CharField(required=False)
    password= serializers.CharField(required=False)
    #private = serializers.CharField(required=False)

    class Meta:
        model= users_new
        fields="__all__"