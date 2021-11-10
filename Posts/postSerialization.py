from rest_framework import serializers
from Posts.models import Post



class post_Class(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'