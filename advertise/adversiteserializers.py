from rest_framework import  serializers
from advertise.models import *
class AdvertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = advertise
        fields = '__all__'