from rest_framework import serializers
from chat.models import ChatModel

class getChatSerializerClass(serializers.ModelSerializer):
    class Meta:
        model= ChatModel
        fields= ('__all__')