
from user import views
import admin as admin
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
#from user.views import User # emailOtp, OTP2
from user.logIn import login
from user.deleteUser import deleteUser
from user.verifyOtp import verifyOtp
from user.SendPutOtp import emailOtp
#from user.views import LogIn#User
#UserList, UserDetail, User
#from user.views import showData
from user.GetPutPublic import getPublic
from user.searchUser import searchUser
from user import SignUp

from user.SignUp import SignUp

#-----posts imports
from Posts.deletePost import dPost
from Posts.postPost import pPost
from Posts.putPost import putpost
from Posts.getPost import getpost


#----advance profile---------

from advanceProfile.views import *


#----advertise----------------

from advertise.views import *


#----friend list

from Friend.AddFriend import *


#----------chat---------------
from chat.NewChat import *
from chat.getChat import *

urlpatterns = [
    path('admin/', admin.site.urls),
   # url(r'^api/show/(?P<userId>\d+)/$', UserDetail.as_view(),name='user_list'),


  #  path('view/', showData(),name='show data')


#---------------------fromnt end naman ajax start--------------------------
    #-----apurva working signup code
    #-----integration signnup working path(r'api/sign_up', SignUp.signup, name='users_new'),
    path(r'api/sign_up/otp',views.otp, name='otp_verify'),
    path(r'api/sign_up/signIn',views.signIn, name='sign_in'),
    path(r'api/sign_up/combine_profile', views.Homepage, name='homepage'),

    #path(r'api/sign_up/otp', views.otp, name='otp'),
#--------user api---------------------
   # url(r'^api/show/$', UserList.as_view(), name='user_list'),
    url(r'^api/SignUp$', SignUp.as_view(),name="signup with pass encryp"),
    #url(r'^api/signup$',view=User),
    #url(r'^api/put$',view=User),
    url(r'^api/emailOtp2$',view=emailOtp),

    url(r'^api/otp$',emailOtp.as_view(),name = 'otp store'),
   # url(r'^api/otp$',view=OTP2.as_view()),
  #  url(r'^api/emailOtp$',emailOtp.as_view()),
    url(r'^api/delete/(?P<userId>\d+)/$',deleteUser.as_view(),name='delete user'),
    url(r'^api/delete/(?P<userId>\d+)/$',deleteUser.as_view(),name='delete user'),

    url(r'^api/login$', login.as_view()),


    url(r'^api/verify$', verifyOtp.as_view()),
    #url(r'^api/login$',view= LogIn)
    url(r'^api/showPublic$', getPublic.as_view()), # show only public url
    url(r'^api/putPublic/(?P<userId>\d+)/$', getPublic.as_view(),name='put user private mode'), #changes private or public

    url(r'^api/searchUser$',searchUser.as_view(),name='search_User'),


#----------------posts urls--------------------------
    url(r'^api/deletePost/(?P<id>\d+)/$', dPost.as_view(), name='delete Post'),
    url(r'^api/postPost$', pPost.as_view()),
    url(r'^api/getPost$', getpost.as_view()),
    url(r'^api/putPost(?P<id>\d+)/$', putpost.as_view(), name='put POST'),

#----------------advance profile-----------------

    url(r'^api/advProfile/delete/(?P<id>\d+)/$', Adv.as_view(), name='delete Post'),
    url(r'^api/advProfile/post$', Adv.as_view()),
    url(r'^api/advProfile/get$', Adv.as_view()),
    url(r'^api/advProfile/put(?P<id>\d+)/$', Adv.as_view(), name='put POST'),


#----------------Advertise--------------------------
url(r'^api/ads/delete/(?P<id>\d+)/$', AdvertiseList.as_view(), name='delete Post'),
    url(r'^api/ads/post$', AdvertiseList.as_view()),
    url(r'^api/ads/get$', AdvertiseList.as_view()),
    url(r'^api/ads/put/(?P<id>\d+)/$', AdvertiseList.as_view(), name='put POST'),

#------------------Prefrences------------------------to edit
url(r'^api/deletePost/(?P<id>\d+)/$', dPost.as_view(), name='delete Post'),
    url(r'^api/postPost$', pPost.as_view()),
    url(r'^api/getPost$', getpost.as_view()),
    url(r'^api/putPost(?P<id>\d+)/$', putpost.as_view(), name='put POST'),

#------------------chat----------------------
    url(r'^api/newchat/post$',NewChat.as_view()),
    url(r'^api/user/chat/get$', GetChat.as_view()),


#----------------friends----------------------------to edit
    #url(r'^api/friend/delete/(?P<id>\d+)/$', frnd.as_view(), name='delete Post'),
    url(r'^api/friend/post$', AddFriend.as_view()),
    url(r'^api/friend/get$', AddFriend.as_view())
    #url(r'^api/friend/put/(?P<id>\d+)/$', frnd.as_view(), name='put POST'),

]
