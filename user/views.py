
#----api.py code----
import hashlib

from django.http import QueryDict
from django.views.decorators.http import require_http_methods
from requests import post
from rest_framework.decorators import renderer_classes, api_view
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

import json
from socialmedia import *
from .loginSerialization import *
from .serialization import *
from .user_serialization import *
from .OtpSerialization import *
from .OtpVerify import *

import random,smtplib


#-----------------signup get post put delete-----------------

email=""
@api_view(['GET','POST'])
#@csrf_exempt


def users_new2(request):
    print("----------inside user new function")

    form = serializerClass()
    if(request.method == 'GET'):
        print("get getting called")
    #if request.method == 'POST':
        #form = serializerClass(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return redirect('users_new')
    #if request.is_ajax():
    #user_post_data = JSONParser().parse(request)
    #user_serializer = user_Serialization_Class(data=user_post_data)


    print("req meth: ",request.method,"\nreq post value",request.POST)
    print("req data: ",request.data)
    if request.method=='POST':
        global email
        # -----email setup and login---------------------
        number = random.randint(1111, 9999)  # otp generration
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login('franzosocialmedia@gmail.com', 'apurva87654321')
        print(s.login('franzosocialmedia@gmail.com', 'apurva87654321'))

        print("inside ajax if")
        print("req data post print ----- ",(request.data))
        #print("req data post print iterate ----- ", (request.data['emailid']))    #fetching email id from query dictionary
        copy_GET = QueryDict('a=1&a=2&a=3', mutable=True)
        print("PASS COPYget")
        #l = copy_GET.getlist('a')
        #l.append(u'4')
        #copy_GET.setlist('a', l)
        form = serializerClass(data=request.POST)
        #print("data form variable: ---", type(form))
        #print("type req post ", type(request.POST))
        data_dict = request.data.dict()   #converting query dict to dictionary
        print("type:---------", type(request.POST))
        print("data dict: ",data_dict)
        email = data_dict['emailid']
        print("email globalllllllll ",email)

        request.data._mutable = True
        request.data['otp'] = number
        request.data['password']= hashlib.md5(request.data['password'].encode()).hexdigest()
        print("serializer value: ", request.data)

        print("add otp: ", request.data['otp'])

        #serializer = OtpserializerClass(request.POST, data=request.data)
        print("serializer called-------------------------------------")

        if form.is_valid():
            print("inside valid form---###")

            form.save()
            s.sendmail('franzosocialmedia@gmail.com', request.data['emailid'], str(number))

            #print("data form variable: ---", (form))
            #email= request.data['emailid']
            print("email globalllllllll 2222222 ", email)

            return Response(form.data, status=status.HTTP_201_CREATED)

            #print("errors serializer: ",form.errors)
        return Response(form.errors,status=status.HTTP_400_BAD_REQUEST)
    print("\nif not post ")
    return render(request, 'users_new.html', {'form': form})

@api_view(['GET','POST'])
def otp(request):
    #getQueryString = request.data.get('emailid')
    #rint("type get qs ", type(getQueryString), "value ", getQueryString)
    #request.data._mutable=True
    if request.method=='POST':
        print("req data otp ---------->  ", request.data)
        # print("otp from otp class: ",request.data['otp'])

        print("added email and otp in reqq data: ", request.data)
        check = {}
        check['emailid'] = email
        check['otp'] = request.data['otp']
        print("value: ", check, " type : ", type(check))
        serializer = OtpVerifyserializerClass(request.POST, data=request.data)
        verifyOtpQs = users_new.objects.all().filter(**check)
        print(verifyOtpQs)
        if verifyOtpQs.exists():
            print("##########_-------existss--#######", verifyOtpQs)
            if serializer.is_valid():
                print("otp serializer: ", serializer.validated_data)
                print("inside valid form---###")

                # s.sendmail('franzosocialmedia@gmail.com', request.data['emailid'], str(number))

                # print("data form variable: ---", (form))

                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return render(request, 'signup_otp.html')


#------signup fetch end


@api_view(['GET','POST'])
def signIn(request):
    if request.method=='POST':
        print("received value", request.data)
        #getQueryString = request.data
        #print("get query string: ", getQueryString)
        print("type pf get query1 : ", type(request.data))
        request.data._mutable=True
        request.data['password'] = hashlib.md5(request.data['password'].encode()).hexdigest()
        # print("** query: ", type(**getQueryString))
        print("after hash: ", request.data)
        checkQs={}
        checkQs['mobilenumber']= request.data['mobilenumber']
        checkQs['password']= request.data['password']
        course_qs = users_new.objects.filter(**checkQs)
        print("course qs: ", course_qs)
        print("type of course qs 2: ", type(course_qs))
        if (course_qs.exists()):
            print("\n\n query set: ", course_qs)
            model = None
            for course in course_qs:
                model = course
            sample = list(course_qs.values_list()[0])
            print("get start function and sample value: ", sample)

            s = serializerClass(data=request.data)
            if s.is_valid():
                s.validated_data['msg'] = "login success!!"
                s.validated_data['status'] = status.HTTP_200_OK
                s.validated_data['userId'] = sample[0]
                s.validated_data['name'] = sample[1]
                s.validated_data['emailid'] = sample[4]
                #s.validated_data['timestamp'] = datetime.now
                print(sample)  # has the data of the logged in user as a list
                return Response(s.validated_data, status=status.HTTP_200_OK)
            return Response(s.errors)
        else:
            return Response("credentials doesn't match", status=status.HTTP_400_BAD_REQUEST)
    return render(request,'sign_in.html')


def Homepage(request):

    return render(request, 'combine_profile.html')