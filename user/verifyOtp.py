

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

from user.models import users_new


class verifyOtp(APIView):
    #print("\n\ninside userD\n\n")
    def post(self,request):
           # print("received value",self.request.data)
            getQueryString = self.request.data
            print("get query string verify : ",getQueryString)
           # print("type pf get query: ",type(getQueryString))
            #print("** query: ", type(**getQueryString))
            course_qs = users_new.objects.filter(**getQueryString)
            print("course qs: ", course_qs)
            #print("type of course qs: ", type(course_qs))
            if (course_qs.exists()):
                print("\n\n query set verify: ", course_qs)
                model = None
                for course in course_qs:
                    model = course
                sample = list(course_qs.values_list()[0])
                print("verify sample: ")

                print(sample) # has the data of the logged in user as a list
                return Response("OTP verified: ", status=status.HTTP_200_OK)

            else:
                return Response("Otp verification fail",status=status.HTTP_400_BAD_REQUEST)

# ---------verify otp done-----------------------------