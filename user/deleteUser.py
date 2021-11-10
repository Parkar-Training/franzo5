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


class deleteUser(APIView):
    # ----------------get user code-----------------------------------
    def get_user(self, userId):
        print("inside get user")
        try:
            print("inside try1")
            model = users_new.objects.get(userId=userId)
            print("model get user ", model)
            return model



        except users_new.DoesNotExist:
            print("get user id ", userId)
            return Response(f'User with employee id {userId} is not found in Database',
                            status=status.HTTP_404_NOT_FOUND)

    # --------------------delete user code--------------------
    def delete(self, request, userId):
        print("inside delete1")
        model = self.get_user(userId)
        print("inside delete2")
        model.delete()
        print("inside delete3")
        print("deleted user", userId)
        return Response("User Deleted ", status=status.HTTP_204_NO_CONTENT)
    # ----------delete user end--------------------------
