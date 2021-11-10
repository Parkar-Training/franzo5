from AllImports import *
from Friend.AddFriendSerialization import *
from chat.NewChatSerialization import *
from chat.getChatSerialization import *
from chat.models import *


class GetChat(APIView):
    def get(self,request):
        print(request.data)
        print("inside get of chat ")
        #getChatQuery= {}
        #getChatQuery['from_id']=4
        #getChatQuery['to_id']=6

        model= ChatModel.objects.all().filter(**request.data)

        #swapping from and to id values to get both side conversations
        tmp= request.data['from_id']
        request.data['from_id']=request.data['to_id']
        request.data['to_id']=tmp
        #getChatQuery['from_id']=6
        #getChatQuery['to_id']=4
        model= model | ChatModel.objects.all().order_by('chat_created').filter(**request.data)
        print("model chat : ", model)
        #serializer= getChatSerializerClass(model,many=True)
        serializer= getChatSerializerClass(model, many=True)
        #print("s2: ",type(serializer2.data))
        return Response(serializer.data,status=status.HTTP_200_OK)

