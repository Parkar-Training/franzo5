from AllImports import *
from Friend.AddFriendSerialization import *
from Friend.models import *

class AddFriend(APIView):
    def get(self,request):
        print("inside get of caht ")
        serializer= AddFriendSerializerClass(friendModel.objects.all(), many=True)
        return Response(serializer.data)

    def post(self,request):
        print("inside post of new chat")
        getQstring= self.request.data
        print("get q sting data ",getQstring)
       # print("get q sting type ",type(getQstring),"\n to id ",getQstring['to_id'])

        #-------------check id is integer or not
        try:
            int(self.request.data['FriendId'])
            int(self.request.data['FuserId'])

            # -------check if users exists or not
            checkIdSender = {}

            checkIdSender['userId'] = self.request.data['FriendId']
            print("type search data1: ", type(checkIdSender), "value 1 ", checkIdSender)
            checkQstringSender = users_new.objects.all().filter(**checkIdSender)
            print("check q string ", checkQstringSender)

            if checkQstringSender.exists():
                checkIdReceiver={}
                checkIdReceiver['userId'] = self.request.data['FuserId']
                sender = list(checkQstringSender.values_list()[0])

                print("type search data 2: ", type(checkIdReceiver), "value 2 ", checkIdReceiver,"\nsender",sender)
                checkQstringReceiver = users_new.objects.all().filter(**checkIdReceiver)
                print("2nd checkqstring", checkQstringReceiver)
                if checkQstringReceiver.exists():
                    print("found revceiver")
                    receiver = list(checkQstringReceiver.values_list()[0])

                    #------check if they are friends or not---------
                    #checkId['FriendId'] = self.request.data['FuserId']
                    '''getQstring = self.request.data
                    print("getq String: ", getQstring)
                    print("type search data 3: ", type(getQstring), "value 3 ", getQstring)
                    checkQstring = friendModel.objects.all().filter(**getQstring)
                    print("check q string: ", checkQstring)
                    print("status value: ", request.data['Status'], "type ", type(request.data['Status']))
                    '''
                    print(request.data['Status'])
                    checkFriends = friendModel.objects.all().filter(**request.data)
                    print("req data----> ", request.data, "check friends data ",checkFriends)

                    if(request.data['Status']==str(0)): #add friend code
                        #checkFriends= friendModel.objects.all().filter(**request.data)

                        if(checkFriends.exists()):
                            return Response("Already pending req", status=status.HTTP_400_BAD_REQUEST)


                        serializer= AddFriendSerializerClass(data=request.data)
                        if serializer.is_valid():
                            serializer.save()

                            serializer.validated_data['sender name'] = sender[1]
                            serializer.validated_data['sender userId']=sender[0]
                            serializer.validated_data['receiver userId']=receiver[1]
                            serializer.validated_data['receiver name']=receiver[0]
                            serializer.validated_data['status code']=status.HTTP_200_OK
                            serializer.validated_data['timestamp']=datetime.now()
                            serializer.validated_data['msg']="Friend Requet Sent!!!!"
                            return Response(serializer.validated_data,status=status.HTTP_200_OK)
                        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

                        #return Response("save reject reqs=2",status=status.HTTP_200_OK)
                    #tmp= request.data['FriendId']

                    #getQstring['FriendId'] = self.request.data['FuserId']
                    #getQstring['FuserId']= self.request.data[tmp]
                    #checkQstring2 = friendModel.objects.all().filter(**getQstring)
                    #print("check 2 string: ", checkQstring2)
                    '''
                    if checkQstring.exists():# and checkQstring2.exists()):
                        return Response("Already friends or Pending Request!!!!!!", status=status.HTTP_404_NOT_FOUND)

                    '''
                    #serializer= AddFriendSerializerClass(data=self.request.data)

                    #if serializer.is_valid():
                    #    serializer.save()
                    #    serializer.validated_data['sender name']=sender[1]
                    #    serializer.validated_data['sender userId']=sender[0]
                    #    serializer.validated_data['receiver userId']=receiver[1]
                    #    serializer.validated_data['receiver name']=receiver[0]
                    #    serializer.validated_data['status code']=status.HTTP_200_OK
                    #    serializer.validated_data['timestamp']=datetime.now()
                    #    return Response(serializer.validated_data,status=status.HTTP_200_OK)

                    #return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

            return Response("FriendId doesnt exists", status=status.HTTP_404_NOT_FOUND)


        except ValueError:
            return Response("ID value is not integer",status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        getQstring = self.request.data
        print("get q sting data ", getQstring)

        try:
            int(self.request.data['FriendId'])
            int(self.request.data['FuserId'])

            # -------check if users exists or not
            checkIdSender = {}

            checkIdSender['userId'] = self.request.data['FriendId']
            print("type search data1: ", type(checkIdSender), "value 1 ", checkIdSender)
            checkQstringSender = users_new.objects.all().filter(**checkIdSender)
            print("check q string ", checkQstringSender)

            if checkQstringSender.exists():
                checkIdReceiver = {}
                checkIdReceiver['userId'] = self.request.data['FuserId']
                sender = list(checkQstringSender.values_list()[0])

                print("type search data 2: ", type(checkIdReceiver), "value 2 ", checkIdReceiver, "\nsender", sender)
                checkQstringReceiver = users_new.objects.all().filter(**checkIdReceiver)
                print("2nd checkqstring", checkQstringReceiver)
                if checkQstringReceiver.exists():
                    print("found revceiver")
                    receiver = list(checkQstringReceiver.values_list()[0])


                    print(request.data['Status'])
                    checkFriends = friendModel.objects.all().filter(**request.data)



                    print("req data----> ", request.data, "check friends data ", checkFriends)


                    if (request.data['Status'] == str(1)):  # friends or accept friend req
                        print("found status=1")
                        if (checkFriends.exists()):
                            return Response("Already accepted or friends", status=status.HTTP_400_BAD_REQUEST)



                        # -----accept req changes------------------------------------

                        request.data['Status']='0'

                        checkReqSent = friendModel.objects.all().filter(**request.data)

                        if(checkReqSent.exists()): #to avoid list out of index of chec req sent list
                            checkReqSentList = list(checkReqSent.values_list()[0])
                            print("check req sent data: ", checkReqSentList, "check req sent lit: ", checkReqSentList)

                            # -------------serialiazer--------------------
                            #model=friendModel.objects.get
                            request.data['Status']="1"  #changing status back to accept mode
                            serializer = AddFriendSerializerClass(friendModel.objects.get(FId=checkReqSentList[0]),
                                                                  data=request.data)

                            if serializer.is_valid():
                                serializer.save()
                                serializer.validated_data['sender name'] = sender[1]
                                serializer.validated_data['sender userId'] = sender[0]
                                serializer.validated_data['receiver userId'] = receiver[1]
                                serializer.validated_data['receiver name'] = receiver[0]
                                serializer.validated_data['status code'] = status.HTTP_200_OK
                                serializer.validated_data['timestamp'] = datetime.now()
                                serializer.validated_data['msg'] = "Friend Requet Accepted!!!!"
                                return Response(serializer.validated_data, status=status.HTTP_200_OK)
                            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                        return Response("No such pending Request to accept ",status=status.HTTP_404_NOT_FOUND)


                        # return Response("save accept req s=2",status=status.HTTP_200_OK)
                    elif (request.data['Status'] == str(2)):  # reject friend req

                        print("found status=2")
                        if (checkFriends.exists()):
                            return Response("Already rejected", status=status.HTTP_400_BAD_REQUEST)

                        # -----reject req changes------------------------------------

                        request.data['Status'] = '0'

                        checkReqSent = friendModel.objects.all().filter(**request.data)

                        if (checkReqSent.exists()):  # to avoid list out of index of chec req sent list
                            checkReqSentList = list(checkReqSent.values_list()[0])
                            print("check req sent data: ", checkReqSentList, "check req sent lit: ", checkReqSentList)

                            # -------------serialiazer--------------------

                            serializer = AddFriendSerializerClass(friendModel.objects.get(FId=checkReqSentList[0]),
                                                                  data=request.data)

                            request.data['Status']="2"  #changing status back to reject mode
                            if serializer.is_valid():
                                serializer.save()
                                serializer.validated_data['sender name'] = sender[1]
                                serializer.validated_data['sender userId'] = sender[0]
                                serializer.validated_data['receiver userId'] = receiver[1]
                                serializer.validated_data['receiver name'] = receiver[0]
                                serializer.validated_data['status code'] = status.HTTP_200_OK
                                serializer.validated_data['timestamp'] = datetime.now()
                                serializer.validated_data['msg'] = "Friend Requet Rejected!!!!"
                                return Response(serializer.validated_data, status=status.HTTP_200_OK)
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        return Response("No such pending Request to reject ", status=status.HTTP_404_NOT_FOUND)
                return Response("No such user exists Fuserid", status=status.HTTP_404_NOT_FOUND)
            return Response("No such user exists Fiendidd", status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response("ID value is not integer", status=status.HTTP_400_BAD_REQUEST)
