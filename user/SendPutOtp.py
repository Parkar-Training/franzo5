import random
import smtplib
import json

from django.views.decorators.http import require_http_methods
from requests import post,put
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

from user.emailOtpSerialization import *
from user.models import users_new

#self.get_user


class emailOtp(APIView):

    print("\nclass email otp\n\n")

#------------otp store KB start--------------
    def put(self, request):
        print("----inside put-----")
        get_qs= self.request.data
        print("get qs done type ",type(get_qs))
        #emailid='naman8mar1999@gmail.com'
        course_qs= users_new.objects.filter(emailid=get_qs['emailid'])
        print("cour qus --- ", course_qs)
        print("type cour qs", type(course_qs))
        if course_qs.exists():
            print("if exists")


            print("inside try1------->>>")
            sample = list(course_qs.values_list()[0])
            print("type------>", type(sample),"---- value", sample)
            model = users_new.objects.get(userId=sample[0])
           # print("----------userID: ", userid)
            print("inside try1")
            print("model get user ", model)




            #except users_new.DoesNotExist:
             #   print("get user id ", userid)
              #  return Response(f'User with employee id {userid} is not found in Database',
               #                 status=status.HTTP_404_NOT_FOUND)
            print("before serializer")
            serializer = emailOtpClass(model, data=request.data)
            print("serializer made")

            number = random.randint(1111, 9999)  # otp generration

            # -----email setup and login---------------------

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.login('franzosocialmedia@gmail.com', 'apurva87654321')
            print(s.login('franzosocialmedia@gmail.com', 'apurva87654321'))

            print("otp generate: ", number)
            # if not self.get_user(userid):
            # return Response(f'User with{userid}is Not Found in Database', status=status.HTTP_404_NOT_FOUND)
            # print("inside put")

            # users_new.objects.filter(pk=request.data.otp).update(userId=number)

            print("update done")

            print("req data: ", request.data)
            request.data['otp'] = number
            requestDataValues = request.data.values()
            requestDataList = list(requestDataValues)
            print("req data: ", request.data)
            print("req data list: ", requestDataList[0])
            print("req data type: ", type(request.data))
            # print(serializer.errors)
            # print(serializer.error_messages())
            if serializer.is_valid():
                serializer.save()
                s.sendmail('franzosocialmedia@gmail.com', requestDataList[0], str(number))
                #  print()
                print("serializer value:", serializer.data)
                print("serializer value type:", type(serializer.data))
                # "OTP "+number+" sent successfully to "+ request.data['emailid'] +" " return
                return Response("otp sent", status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Email not found: ", status=status.HTTP_404_NOT_FOUND)

