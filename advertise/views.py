from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .adversiteserializers import *
from advanceProfile.models import *

class AdvertiseList(APIView):

    def get_advertise(self, id):

        try:
            model = Adv_prof.objects.get(id=id)
            print("model get user ", model)
            return model

        except Adv_prof.DoesNotExist:
            print("get user id ", id)
            return Response(f'User with employee id {id} is not found in Database',
                            status=status.HTTP_404_NOT_FOUND)






    def get(self, request):
        model = Adv_prof.objects.all()
        print("get start function")
        #serializer = serializerClass(model,many=True)
        serializer=AdvertiseSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AdvertiseSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            print("\n\n---------------------")
            print("data post: ",serializer.data)
            print("data post type : ", type(serializer.data))
            print("\n-----------------------")
            #return "SignUp successfull!!!"
            return Response("Operation successfull!!!", status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        model = self.get_advertise(id)
        model.delete()
        print("deleted user",id)
        return Response(status=status.HTTP_204_NO_CONTENT)