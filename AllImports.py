#---------------This file has all the imports which we need --------------

import random
import smtplib

from django.http import QueryDict
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
from user.serialization import serializerClass
from user.passwdserialization import *
import hashlib

#---------datetime-------
from datetime import datetime