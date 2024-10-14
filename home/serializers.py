from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from home.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields= ['username', 'password', 'email', 'phonenumber', 'location']
    
