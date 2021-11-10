from rest_framework import serializers
from Friend.models import friendModel

class AddFriendSerializerClass(serializers.ModelSerializer):
    class Meta:
        model= friendModel
        fields= ('__all__')