from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .serializer import ProfilSerializer, FriendSerializer, ChatMessageSerializer
from .models import Profile, Friend, ChatMessage


# @api_view(['GET'])
class ProfiletViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfilSerializer
    
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     token = AuthToken.objects.create(user)
    #     return Response({
    #         "users": UserSerializer(user, context=self.get_serializer_context()).data,
    #         "token": token[1]
    #     })
    
  

#@api_view(['POST'])
class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
# def create_friend(request):
#     data = request.data
#     serializer =ChatSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer
