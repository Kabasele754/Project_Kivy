from unicodedata import name
from rest_framework import serializers
from .models import *

class ProfilSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Profile
        fields = '__all__'
        
class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'

class ChatMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'