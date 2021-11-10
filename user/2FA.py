from AllImports import *
from makePrivateSerialization import *
class TwoFA(APIView):
    def put(self,request,userId):
        serializer= makePrivateSerializerClass(users_new.objects.get(userId=userId), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Changed Successfully!!!", status=status.HTTP_201_CREATED)

        return Response("Serializer invalid: \n" + serializer.errors, status=status.HTTP_400_BAD_REQUEST)


