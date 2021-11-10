from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Posts.postSerialization import *

class dPost(APIView):
    def get_Post(self, id):
        print("inside getuser")
        try:
            model = Post.objects.get(id=id)
            print("inside try1")
            print("model get user ", model)
            return model



        except Post.DoesNotExist:
            print("get user id ", id)
            return Response(f'User with employee id {id} is not found in Database',
            status=status.HTTP_404_NOT_FOUND)



    print("\n\ninside userD\n\n")

    def delete(self, request, id):
        model = self.get_Post(id)
        model.delete()
        print("deleted user", id)
        return Response(status=status.HTTP_204_NO_CONTENT)