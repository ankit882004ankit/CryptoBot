from rest_framework import serializers
from .models import Alert
from django.contrib.auth.models import User  

class AlertSerializer(serializers.ModelSerializer):
  class Meta:
    model = Alert
    fields = ['id', 'cryptocurrency','target_price','status','created_at']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
       model = User
       fields = ['id','username','email','password']
      
    def create(self, validated_data):
       user = User(
          email = validated_data['email'],
          username = validated_data['username']
       )
       user.set_password(validated_data['password'])
       user.save()
       return user
       