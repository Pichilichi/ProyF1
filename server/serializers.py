from rest_framework import serializers
from django.contrib.auth.models import User

# Transform User into JSON data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        
