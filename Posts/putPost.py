from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Posts.postSerialization import *


class putpost(APIView):
    def get_user(self, id):
        try:
            model = Post.objects.get(id=id)
            print("model get user ", model)
            return model

        except Post.DoesNotExist:
            print("get user id ", id)
            return Response(f'User with employee id {id} is not found in Database',
                            status=status.HTTP_404_NOT_FOUND)
    def put(self, request, id):
        serializer = post_Class(self.get_user(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Put successfull !!!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)