from unicodedata import name
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class MainRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfilSerializer(serializers.HyperlinkedModelSerializer):
    register = MainRegisterSerializer()
    
    class Meta:
        model = Profile
        fields = ('register' ,'name','pic') 
        
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], validated_data['file'])
        return user
        
class FriendSerializer(serializers.HyperlinkedModelSerializer):
    prof = ProfilSerializer()
    class Meta:
        model = Friend
        fields = '__all__'
    
        
        

class ChatMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'