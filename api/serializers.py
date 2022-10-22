
from rest_framework import serializers
from .models import Board
from django.contrib.auth.models import User
import string, random


class BoardSerializer(serializers.ModelSerializer):
    game_str = serializers.CharField(max_length = 1)
    class Meta:
        model = Board
        fields = ['id', 'game_id', 'created_at', 'created_by', 'game_str', 'complete', 'is_palindrome']
        read_only_fields = [ 'game_id', 'created_at', 'created_by']
    
    def update(self, instance, validated_data):
        game_str = (instance.game_str)
        if not (instance.complete):            
            game_str += validated_data['game_str']
            game_str += ''.join(random.choices(string.digits, k = 1))
            validated_data['game_str'] = game_str
            return super().update(instance, validated_data)
        



class UserSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}   

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user





