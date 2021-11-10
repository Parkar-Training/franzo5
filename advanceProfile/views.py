# -----------Advance Profile---------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from advanceProfile.AdvSerialization import *

class Adv(APIView):
    def get(self, request):
        model = Adv_prof.objects.all()
        print("get start function")
        # serializer = serializerClass(model,many=True)
        serializer = Adv_profClass(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Adv_profClass(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            print("\n\n---------------------")
            print("data post: ", serializer.data)
            print("data post type : ", type(serializer.data))
            print("\n-----------------------")
            return Response("Operation successfull!!!", status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Please add put opertaion


    def get_user(self, id):
            try:
                model = Adv_prof.objects.get(id=id)
                print("model get user ", model)
                return model

            except Adv_prof.DoesNotExist:
                print("get user id ", id)
                return Response(f'User with employee id {id} is not found in Database',
                                    status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        serializer = Adv_profClass(self.get_user(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Put successfull !!!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



