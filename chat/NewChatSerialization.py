from rest_framework import serializers
from chat.models import ChatModel

class NewChatSerializerClass(serializers.ModelSerializer):
    class Meta:
        model= ChatModel
        fields= ('__all__')