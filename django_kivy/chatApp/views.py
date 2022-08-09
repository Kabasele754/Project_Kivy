from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *
from .models import *


@api_view(['GET'])
def all_friend(request):
    friend = Friend.objects.all()
    serializer = ChatSerializer(friend, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_friend(request):
    data = request.data
    serializer =ChatSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
