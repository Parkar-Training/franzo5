from django.views.decorators.http import require_http_methods
from requests import post
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from user.models import users_new
from user.makePrivateSerialization import *
from user.user_serialization import *


class getPublic(APIView):
    print("Inside get public class")
    def get(self, request):
        
        #model = users_new.objects.all()
        print("Get only public data only function")
        #print("model type:",type(model))
        #print("model data: ", model)
        #print("model iterate: ",model[0])
        #filter= users_new.objects.values('private')
        filter=users_new.objects.all().filter(**{"private":"False"})
        #filter= users_new.objects.all().values_list('private','name')
        print("\nfilter print :", filter)
        print("\nfilter print :", type(filter))
        print("\nfilter print type:", (filter[0]))
        # serializer = serializerClass(model,many=True)
        serializer = user_Serialization_Class(filter, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def get_user(self, userId):
        print("inside getuser")
        try:
            model = users_new.objects.get(userId=userId)
            print("inside try1")
            print("model get user ", model)
            return model



        except users_new.DoesNotExist:
            print("get user id ", userId)
            return Response(f'User with employee id {userId} is not found in Database',
            status=status.HTTP_404_NOT_FOUND)



    print("\n\ninside userD\n\n")

    def put(self, request, userId):
        if not self.get_user(userId):
            return Response(f'User with{userId}is Not Found in Database', status=status.HTTP_404_NOT_FOUND)
            #print("inside put")
        serializer = makePrivateSerializerClass(self.get_user(userId), data=request.data)
        print("self get uid -----",self.get_user(userId))
        print("req data: ", request.data)

        #requestDataValues= request.data.values()
        #requestDataList= list(requestDataValues)
        print("req data: ", request.data)
        #print("req data list: ", requestDataList[0])
        print("req data type: ", type(request.data))
        #print(serializer.errors)
        #print(serializer.error_messages())
        if serializer.is_valid():
            serializer.save()

            print("serializer value:", serializer.data)
            print("serializer value type:", type(serializer.data))
            #"OTP "+number+" sent successfully to "+ request.data['emailid'] +" " return
            return Response("Changed Successfully!!!", status=status.HTTP_201_CREATED)

        return Response("Serializer invalid: \n"+serializer.errors, status=status.HTTP_400_BAD_REQUEST)
