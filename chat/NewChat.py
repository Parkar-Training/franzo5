from AllImports import *
from chat.NewChatSerialization import NewChatSerializerClass
from chat.models import *
from Friend.models import *


class NewChat(APIView):
    def get(self,request):
        print("inside get of caht ")
        serializer= NewChatSerializerClass(ChatModel.objects.all(), many=True)
        return Response(serializer.data)

    def post(self,request):

        print("inside post of new chat")
        getQstring= self.request.data
        print("get q sting data ",getQstring)
       # print("get q sting type ",type(getQstring),"\n to id ",getQstring['to_id'])

        #-------------check id is integer or not
        try:
            int(self.request.data['to_id'])
            int(self.request.data['from_id'])

            # -------check sender id if present
            checkUserId = {}

            checkUserId['userId'] = self.request.data['to_id']
            print("type search data: ", type(checkUserId), "value ", checkUserId)
            checkQstring = users_new.objects.all().filter(**checkUserId)  # 'userId'=='2'
            print("check q string ", checkQstring)

            if checkQstring.exists():
                receiver = list(checkQstring.values_list()[0])  # receiver details list
                #print("sample:----->>>s ", sample)
                checkUserId['userId'] = self.request.data['from_id']
                print("type search data: ", type(checkUserId), "value ", checkUserId)
                checkQstring = users_new.objects.all().filter(**checkUserId)  # 'userId'=='2'

                if checkQstring.exists():
                    sender = list(checkQstring.values_list()[0]) #sender details list

                    #checking if they are friends or not----------------------
                    checkFriends1= {}

                    checkFriends1["FriendId"]=request.data['from_id']
                    checkFriends1["FuserId"]= request.data['to_id']
                    checkFriends1["Status"]= "1"

                    checkQstring1= friendModel.objects.all().filter(**checkFriends1)
                    print("check friend dictionary 1: ", checkFriends1)
                    print("check if friends or not 1: ", checkQstring1)

                    #CHECK VICE versa friends or not
                    checkFriends2 = {}

                    checkFriends2["FriendId"] = request.data['to_id']
                    checkFriends2["FuserId"] = request.data['from_id']
                    checkFriends2["Status"] = "1"

                    checkQstring2 = friendModel.objects.all().filter(**checkFriends2)
                    print("check friend dictionary 2: ", checkFriends2)
                    print("check if friends or not 2: ", checkQstring2)

                    if (checkQstring1.exists() or checkQstring2.exists()):
                        serializer = NewChatSerializerClass(data=request.data)
                        if serializer.is_valid():
                            serializer.save()
                            # serializer.validated_data['msg'] = "Conversation Started"
                            serializer.validated_data['status'] = status.HTTP_200_OK
                            serializer.validated_data['timestamp'] = datetime.now()
                            serializer.validated_data['sender name'] = sender[1]
                            serializer.validated_data['receiver name'] = receiver[1]
                            serializer.validated_data['msg code']= "message sent!"


                        return Response(serializer.validated_data, status=status.HTTP_200_OK)
                    return Response("You cannot send message to "+str(receiver[1])+ " as you both are not friends.", status=status.HTTP_400_BAD_REQUEST)
                return Response("sender doesnt exists", status=status.HTTP_404_NOT_FOUND)

            return Response("receiver doesnt exists", status=status.HTTP_404_NOT_FOUND)


        except ValueError:
            return Response("ID value is not integer",status=status.HTTP_400_BAD_REQUEST)




        #serializer= NewChatSerializerClass(data= request.data)
