from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Posts.postSerialization import *

class getpost(APIView):
    def get(self, request):
        model = Post.objects.all()
        print("get start function")
        # serializer = serializerClass(model,many=True)
        serializer = post_Class(model, many=True)
        return Response(serializer.data)