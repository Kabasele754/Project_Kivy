from rest_framework import serializers
from .models import *

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'