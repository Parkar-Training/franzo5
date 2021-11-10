from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Posts.postSerialization import *

class pPost(APIView):
    def post(self, request):
        serializer = post_Class(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            print("\n\n---------------------")
            print("data post: ", serializer.data)
            print("data post type : ", type(serializer.data))
            print("\n-----------------------")
            return Response("Operation successfull!!!", status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)